#!/usr/bin/env python3
"""
Convert a Freshdesk Solutions.xml export into a Docusaurus docs/ tree.
"""
import re
import json
import html
from pathlib import Path
from lxml import etree
from markdownify import markdownify as md

SCRIPT_DIR = Path(__file__).resolve().parent
SRC = SCRIPT_DIR / "source" / "Solutions.xml"
DOCS_DIR = SCRIPT_DIR / "docs"

SKIP_FOLDER_NAMES = {"Drafts"}  # empty placeholder folder, not real content


def slugify(text: str) -> str:
    text = html.unescape(text or "").strip().lower()
    text = re.sub(r"[''\"`]", "", text)
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text).strip("-")
    return text or "untitled"


def unique_slug(base: str, used: set) -> str:
    slug = base
    i = 2
    while slug in used:
        slug = f"{base}-{i}"
        i += 1
    used.add(slug)
    return slug


def clean_title(t: str) -> str:
    t = html.unescape(t or "").strip()
    t = re.sub(r"\s+", " ", t)
    return t


def esc_frontmatter(s: str) -> str:
    s = (s or "").replace("\\", "\\\\").replace('"', '\\"')
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    tree = etree.parse(str(SRC))
    root = tree.getroot()

    categories = root.findall("solution-category")

    # ---- Pass 1: collect folders/articles, build slugs + id->path map ----
    folder_records = []  # list of dicts: name, slug, position, description, articles[]
    used_folder_slugs = set()
    id_to_path = {}     # article id (str) -> relative docs path (no leading slash, no .md)
    folder_id_to_path = {}  # folder id (str) -> relative docs path (folder index)

    for cat in categories:
        cat_name = cat.findtext("name") or ""
        folders = cat.find("all-folders").findall("solution-folder")
        for f in folders:
            fname = clean_title(f.findtext("name"))
            if fname in SKIP_FOLDER_NAMES:
                continue
            articles_el = f.find("articles")
            arts = articles_el.findall("solution-article") if articles_el is not None else []
            if not arts:
                continue  # skip folders with no published articles

            fslug = unique_slug(slugify(fname), used_folder_slugs)
            fdesc = html.unescape(f.findtext("description") or "").strip()
            fposition = int(f.findtext("position") or "0")
            fid = f.findtext("id")

            article_records = []
            used_article_slugs = set()
            for a in arts:
                title = clean_title(a.findtext("title"))
                aid = a.findtext("id")
                aposition = int(a.findtext("position") or "0")
                aslug = unique_slug(slugify(title), used_article_slugs)
                desc_html = a.findtext("description") or ""
                article_records.append({
                    "id": aid,
                    "title": title,
                    "slug": aslug,
                    "position": aposition,
                    "html": desc_html,
                })
                id_to_path[aid] = f"{fslug}/{aslug}"

            folder_records.append({
                "id": fid,
                "name": fname,
                "slug": fslug,
                "position": fposition,
                "description": fdesc,
                "articles": article_records,
            })
            folder_id_to_path[fid] = f"{fslug}/"

    # ---- Helper: rewrite internal freshdesk/hqtelecom links to relative docs paths ----
    article_link_re = re.compile(
        r'href="(https?://[^"]*?/(?:solutions|a/solutions)?/?(?:articles)/(\d+)[^"]*)"'
    )
    folder_link_re = re.compile(
        r'href="(https?://[^"]*?/solutions/folders/(\d+)[^"]*)"'
    )

    def rewrite_links(html_str: str) -> str:
        def repl_article(m):
            full, aid = m.group(1), m.group(2)
            if aid in id_to_path:
                return f'href="/{id_to_path[aid]}"'
            return m.group(0)

        def repl_folder(m):
            full, fid = m.group(1), m.group(2)
            if fid in folder_id_to_path:
                return f'href="/{folder_id_to_path[fid]}"'
            return m.group(0)

        html_str = article_link_re.sub(repl_article, html_str)
        html_str = folder_link_re.sub(repl_folder, html_str)
        return html_str

    # ---- Pass 2: write files ----
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    # intro / landing page
    folder_records.sort(key=lambda r: r["position"])
    intro_lines = [
        "---",
        "id: intro",
        'title: "Welcome to HQ Telecom Support"',
        "slug: /",
        "sidebar_position: 1",
        "sidebar_label: Welcome",
        "format: md",
        "---",
        "",
        "# HQ Telecom Help Center",
        "",
        "Find setup guides, troubleshooting steps, and frequently asked questions "
        "for your HQ Telecom product below. Choose a product category to get started.",
        "",
    ]
    for rec in folder_records:
        intro_lines.append(f"- **[{rec['name']}](/{rec['slug']}/)** &mdash; {len(rec['articles'])} article(s)")
    intro_lines.append("")
    intro_lines.append(
        "If you can't find what you're looking for, "
        "[contact our support team](https://www.hqtelecom.com/pages/contact)."
    )
    intro_lines.append("")
    (DOCS_DIR / "intro.md").write_text("\n".join(intro_lines), encoding="utf-8")

    total_articles = 0
    for rec in folder_records:
        folder_dir = DOCS_DIR / rec["slug"]
        folder_dir.mkdir(parents=True, exist_ok=True)

        category_json = {
            "label": rec["name"],
            "position": rec["position"] + 1,  # +1 because intro takes position 1
            "link": {
                "type": "generated-index",
                "description": rec["description"] or f"FAQs and guides for {rec['name']}.",
            },
        }
        (folder_dir / "_category_.json").write_text(
            json.dumps(category_json, indent=2), encoding="utf-8"
        )

        for art in sorted(rec["articles"], key=lambda a: a["position"]):
            total_articles += 1
            raw_html = rewrite_links(art["html"])
            try:
                body_md = md(raw_html, heading_style="ATX", bullets="-", strip=["script"])
            except Exception as e:
                body_md = f"<!-- conversion error: {e} -->\n\n" + raw_html

            # Collapse excessive blank lines left over from messy source HTML
            body_md = re.sub(r"\n{3,}", "\n\n", body_md).strip() + "\n"

            title_escaped = esc_frontmatter(art["title"])
            fm = [
                "---",
                f'title: "{title_escaped}"',
                f"sidebar_position: {art['position']}",
                "format: md",
                "---",
                "",
            ]
            content = "\n".join(fm) + "\n" + body_md
            out_path = folder_dir / f"{art['slug']}.md"
            out_path.write_text(content, encoding="utf-8")

    print(f"Wrote {len(folder_records)} folders and {total_articles} articles.")


if __name__ == "__main__":
    main()

// @ts-check
const { themes: prismThemes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'HQ Telecom Support',
  tagline: 'Help Center & Product FAQs',
  favicon: 'img/favicon.ico',

  // Set your production site URL here
  url: 'https://alfredopurrinos.github.io',
  baseUrl: '/hqtelecom-docs/',

  // GitHub pages deployment config (update if you deploy there)
  organizationName: 'alfredopurrinos',
  projectName: 'hqtelecom-docs',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/', // Serve docs at the site root
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: undefined,
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/social-card.png',
      navbar: {
        title: 'HQ Telecom Support',
        logo: {
          alt: 'HQ Telecom Logo',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'supportSidebar',
            position: 'left',
            label: 'Help Center',
          },
          {
            href: 'https://www.hqtelecom.com',
            label: 'Main Website',
            position: 'right',
          },
          {
            href: 'https://www.hqtelecom.com/pages/contact',
            label: 'Contact Us',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Help Center',
            items: [
              {
                label: 'All Products',
                to: '/',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'Main Website',
                href: 'https://www.hqtelecom.com',
              },
              {
                label: 'Contact Support',
                href: 'https://www.hqtelecom.com/pages/contact',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} HQ Telecom. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

module.exports = config;

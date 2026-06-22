// @ts-check
const { themes: prismThemes } = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'HQ Telecom Support',
  tagline: 'Help Center & Product FAQs',
  favicon: 'img/favicon.ico',

  url: 'https://alfredopurrinos.github.io',
  baseUrl: '/hqtelecom-docs/',

  organizationName: 'alfredopurrinos',
  projectName: 'hqtelecom-docs',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  markdown: {
    format: 'md',
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      ({
        docs: {
          routeBasePath: '/',
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
    ({
      image: 'img/social-card.png',
      navbar: {
        title: 'HQTelecom Support',       
     logo: {
  alt: 'HQ Telecom Logo',
  src: 'https://www.hqtelecom.com/cdn/shop/files/hqt-logo.png?v=1725858112&width=180',
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

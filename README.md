# LunaDash documentation site

This repository contains the Astro site used by LunaDash. The integration repository pins this project as the `site/` submodule.

## Local development

```sh
npm ci --include=dev --ignore-scripts
npm run check
npm run build
```

The site is deployed from the integration repository's selected commit. Update its pinned submodule revision there after reviewing a site change.

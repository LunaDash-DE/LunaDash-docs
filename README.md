# LunaDash documentation site

This repository contains the independent Astro website for LunaDash. Its source stays here and is cloned separately by the integration repository's validation and Pages workflows.

## Local development

```sh
npm ci --include=dev --ignore-scripts
npm run check
npm run build
```

Website CI validates each change in this repository. The integration repository's Pages workflow fetches the current `main` revision when it runs; it does not include this source in its checkout.

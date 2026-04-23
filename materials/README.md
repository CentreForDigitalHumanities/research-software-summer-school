# Documentation and materials
This directory contains the materials in MarkDown format, and the infrastructure required to generate a static website from them using [mkdocs][mkdocs].

## Installation
- Install [uv][uv] package and project manager

## Usage
To serve a local version of the website:
```
uvx --with mkdocs-material mkdocs serve --livereload
```
To generate a new version of the website:
```
uvx --with mkdocs-material mkdocs build
```

## CI/CD
The website is automatically built and deployed the repositoriy GitHub page. See [the workflow file](../.github/workflows/ci.yml) for details.
View the built site at [the GitHub pages adress][pages].

## Theming
For now, the website is generated using the default *material* theme by [mkdocs-material][mkdocs-material]. See documentation on customization.


[mkdocs]: https://www.mkdocs.org/
[mkdocs-material]: https://squidfunk.github.io/mkdocs-material/
[uv]: https://docs.astral.sh/uv/
[pages]: centrefordigitalhumanities.github.io/research-software-summer-school
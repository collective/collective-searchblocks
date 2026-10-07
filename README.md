# Search blocks 🚀

[![Built with Cookieplone](https://img.shields.io/badge/built%20with-Cookieplone-0083be.svg?logo=cookiecutter)](https://github.com/plone/cookieplone-templates/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CI](https://github.com/collective/collective-searchblocks/actions/workflows/main.yml/badge.svg)](https://github.com/collective/collective-searchblocks/actions/workflows/main.yml)

A comprehensive solution for searching and managing content that uses specific blocks in Plone and Volto.

## Features ✨

- **Search Blocks**: Search for content using specific block types
- **Search page**: Dedicated page for searching blocks, linked from the user menu of the toolbar
- **Pagination**: Navigate through search results with configurable page sizes
- **Multilingual Support**: Support for multiple languages (Italian included)
- **Error Handling**: Comprehensive error handling and user feedback
- **REST API**: RESTful endpoint for programmatic access to block search functionality

## Quick Start 🏁

### Prerequisites ✅

-   An [operating system](https://6.docs.plone.org/install/create-project-cookieplone.html#prerequisites-for-installation) that runs all the requirements mentioned.
-   [uv](https://6.docs.plone.org/install/create-project-cookieplone.html#uv)
-   [nvm](https://6.docs.plone.org/install/create-project-cookieplone.html#nvm)
-   [Node.js and pnpm](https://6.docs.plone.org/install/create-project.html#node-js) 22
-   [Make](https://6.docs.plone.org/install/create-project-cookieplone.html#make)
-   [Git](https://6.docs.plone.org/install/create-project-cookieplone.html#git)
-   [Docker](https://docs.docker.com/get-started/get-docker/) (optional)


### Installation 🔧

1.  Clone this repository, then change your working directory.

    ```shell
    git clone git@github.com:collective/collective-searchblocks.git
    cd collective-searchblocks
    ```

2.  Install this code base.

    ```shell
    make install
    ```


### Fire Up the Servers 🔥

1.  Create a new Plone site on your first run.

    ```shell
    make backend-create-site
    ```

2.  Start the backend at http://localhost:8080/.

    ```shell
    make backend-start
    ```

3.  In a new shell session, start the frontend at http://localhost:3000/.

    ```shell
    make frontend-start
    ```

Voila! Your Plone site should be live and kicking! 🎉

### Local Stack Deployment 📦

Deploy a local Docker Compose environment that includes the following.

- Docker images for Backend and Frontend 🖼️
- A stack with a Traefik router and a PostgreSQL database 🗃️
- Accessible at [http://collective-searchblocks.localhost](http://collective-searchblocks.localhost) 🌐

Run the following commands in a shell session.

```shell
make stack-create-site
make stack-start
```

And... you're all set! Your Plone site is up and running locally! 🚀

## Project structure 🏗️

This monorepo consists of the following distinct sections:

- **backend**: Houses the API and Plone installation, utilizing pip instead of buildout, and includes a policy package named collective.searchblocks.
- **frontend**: Contains the React (Volto) package.
- **devops**: Encompasses Docker stack, Ansible playbooks, and cache settings.
- **docs**: Scaffold for writing documentation for your project.

### Why this structure? 🤔

- All necessary codebases to run the site are contained within the repository (excluding existing add-ons for Plone and React).
- Specific GitHub Workflows are triggered based on changes in each codebase (refer to .github/workflows).
- Simplifies the creation of Docker images for each codebase.
- Demonstrates Plone installation/setup without buildout.

## Code quality assurance 🧐

To check your code against quality standards, run the following shell command.

```shell
make check
```

### Format the codebase

To format and rewrite the code base, ensuring it adheres to quality standards, run the following shell command.

```shell
make format
```

| Section | Tool | Description | Configuration |
| --- | --- | --- | --- |
| backend | Ruff | Python code formatting, imports sorting  | [`backend/pyproject.toml`](./backend/pyproject.toml) |
| backend | `zpretty` | XML and ZCML formatting  | -- |
| frontend | ESLint | Fixes most common frontend issues | [`frontend/.eslintrc.js`](.frontend/.eslintrc.js) |
| frontend | prettier | Format JS and Typescript code  | [`frontend/.prettierrc`](.frontend/.prettierrc) |
| frontend | Stylelint | Format Styles (css, less, sass)  | [`frontend/.stylelintrc`](.frontend/.stylelintrc) |

Formatters can also be run within the `backend` or `frontend` folders.

### Linting the codebase
or `lint`:

 ```shell
make lint
```

| Section | Tool | Description | Configuration |
| --- | --- | --- | --- |
| backend | Ruff | Checks code formatting, imports sorting  | [`backend/pyproject.toml`](./backend/pyproject.toml) |
| backend | Pyroma | Checks Python package metadata  | -- |
| backend | check-python-versions | Checks Python version information  | -- |
| backend | `zpretty` | Checks XML and ZCML formatting  | -- |
| frontend | ESLint | Checks JS / Typescript lint | [`frontend/.eslintrc.js`](.frontend/.eslintrc.js) |
| frontend | prettier | Check JS / Typescript formatting  | [`frontend/.prettierrc`](.frontend/.prettierrc) |
| frontend | Stylelint | Check Styles (css, less, sass) formatting  | [`frontend/.stylelintrc`](.frontend/.stylelintrc) |

Linters can be run individually within the `backend` or `frontend` folders.

## Internationalization 🌐

Generate translation files for Plone and Volto with ease:

```shell
make i18n
```

## Release 📦

```shell
make release
```

It asks for the next version, then updates versions and changelogs of backend
and frontend and creates the git tag. **It publishes nothing**: pushing the tag
starts two GitHub workflows, `pypi.yml` (backend to PyPI) and `npm.yml`
(frontend to npm), that run lint and tests and then publish via trusted
publishing (OIDC). No PyPI or npm token is needed locally; `GITHUB_TOKEN` is
optional, only to create the GitHub release.

The frontend is **staged**, not published: the new version goes live on npm
only after a maintainer approves it with 2FA, from npmjs.com (package →
*Staged Packages*) or with `npm stage list volto-searchblocks` and
`npm stage approve <stage-id>`.

The npm dist-tag comes from the version: `1.0.0-alpha.1` goes to `alpha`,
`1.0.0` to `latest`.

The steps are not atomic: if the tag exists but one of the two publishes
failed, **do not release again**. Re-run the failed workflow from GitHub
Actions ("Release latest version on PyPI" or "... on npm"), passing the tag.

### One-off setup

Both registries must trust the workflows of `collective/collective-searchblocks`:

- **npm**: on the `volto-searchblocks` package, Settings → *Trusted Publisher* →
  GitHub Actions, repository `collective/collective-searchblocks`, workflow
  `npm.yml`, with only the *stage publish* permission enabled (a direct
  publish from CI is then refused). `make bootstrap-npm` prints the exact
  values (the package already exists, so it does not publish again).
- **PyPI**: on the `collective.searchblocks` project, *Publishing* → add a
  GitHub publisher with repository `collective/collective-searchblocks` and
  workflow `pypi.yml`.

## Credits and acknowledgements 🙏

Generated using [Cookieplone (0.9.10)](https://github.com/plone/cookieplone) and [cookieplone-templates (060fbeb)](https://github.com/plone/cookieplone-templates/commit/060fbeb6a3c9ff8ebfd8cc1e9f4bc61d0feefcf1) on 2026-01-14 15:28:35.708948. A special thanks to all contributors and supporters!

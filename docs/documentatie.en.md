---
description: "Editing the documentation of the Delft Municipal Data Model (GGM): deployment process from XMI source to published site."
---

# Deployment

This guide describes how to publish a new version of the **Delft Municipal Data Model** (Dutch: *Gemeentelijk Gegevensmodel*, abbreviated **GGM**) starting from an XMI file. The process automatically generates:

- a new Excel specification,
- a set of translated `.qea` files (for Enterprise Architect),
- a complete set of Markdown documentation,
- a published version of the documentation on GitHub Pages.

> The process is automated using [Taskfile](https://taskfile.dev/), `crunch_uml`, `mkdocs`, `mike` and other tools.

There are also utility tasks that can be used to make automated changes in the GGM repository. The most important utility writes Excel changes back into the repository.

---

## What does this deployment do?

Once you have a new version of the model in XMI format, you want to automatically generate all the output needed for publication and use:

1. **Validation** — are all tools and settings correct?
2. **Import** — the XMI file is imported into a local Crunch UML database.
3. **Documentation** — Markdown files are generated from the model.
4. **Excel** — an Excel specification is automatically created.
5. **Translations** — for each language in the i18n file, a `.qea` is generated.
6. **Publication** — the documentation is published via GitHub Pages with version management through `mike`.

---

## Prerequisites

To run the deployment automatically you need [Taskfile](https://taskfile.dev/) installed, as well as MkDocs with a number of extensions. You can install MkDocs with the required extensions with:

```bash
pip install mkdocs mkdocs-material mike \
    pymdown-extensions \
    markdown-include \
    mkdocs-git-revision-date-plugin \
    mkdocs-git-authors-plugin \
    mkdocs-glightbox \
    mkdocs-minify-plugin \
    typing_extensions \
    mkdocs-glightbox
```

### Required files under the version directory

| File                | Required? | Description                                                       |
|---------------------|-----------|-------------------------------------------------------------------|
| `model.xmi`         | ✅        | The information model in XMI format                                |
| `model.qea`         | ✅        | The `.qea` version of the model, used for generating translations |
| `translations.json` | ✅        | An i18n file with translations per language                        |

For the example `.env` file, you would have a directory called `v1.0.0` containing the files above.

## Step 1 — configure `.env`

For each new version, edit the existing `.env` file so it reflects the version being deployed. This file also determines which files and directories are used. It is important that `VERSION` matches the directory of the version you are about to deploy exactly.

### 📄 Example `.env` file

```env
VERSION=v1.0.0
XMI_FILE=ggm_model.xmi
GGM_FILE=ggm_model.qea
EXCEL_FILE=ggm_model.xlsx
TRANSLATIONS_DIR=translations
i18N_FILE=translations.json
...
```

## Step 2 — build the deployment

Use the overview below to run individual tasks for parts of the deployment, or to run everything at once with `full-deploy`.

### 📋 Available tasks

| Task                    | What it does                                                                                                  |
|-------------------------|---------------------------------------------------------------------------------------------------------------|
| `check-tools`           | Verifies that required tools are installed (`crunch_uml`, `mkdocs`, etc.)                                     |
| `check-vars`            | Verifies that `.env` is correctly configured and that paths are valid                                         |
| `import-xmi`            | Imports the XMI file and creates a local database (can take several minutes)                                  |
| `generate-docs`         | Generates Markdown files from the model                                                                       |
| `generate-excel`        | Creates an Excel specification                                                                                |
| `generate-translations` | Per language, generates a translated `.qea` version (based on `translations.json`)                            |
| `deploy-docs`           | Builds the documentation locally with MkDocs and `mike` so it can be tested locally before publication        |
| `publish-docs`          | Publishes the documentation to GitHub Pages (`gh-pages` branch)                                               |
| `full-deploy`           | Runs everything above in one go. Publication via `publish-docs` to GitHub Pages is *not* included.            |

### Running tasks

List all tasks:

```bash
task --list
```

Run a single task (prerequisite tasks run automatically first):

```bash
task generate-excel
```

Run all tasks:

```bash
task full-deploy
```

## Step 3 — test locally

Before publishing, you can test the generated documentation locally. Use:

```bash
task deploy-docs
mike serve
```

Then view the documentation at <http://localhost:8000>.

## Step 4 — publish

If everything works locally, you can publish the documentation to GitHub Pages. This step only works if you have access to the GGM GitHub repository:

```bash
task publish-docs
```

Note: this publishes directly to the `gh-pages` branch of the GitHub repository. You will be asked to confirm before the site goes live.

## Utilities

The utilities do not use a previously imported XMI; they read the required information freshly each time.

### 📋 Available utilities

| Task                | What it does                                                                                                                                                                                                                                                                                                  |
|---------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `util-import-xlsx`  | Imports the Excel file specified in `.env`, reads all values into the EA repository, and updates anything changed in the Excel file. Use the same Excel layout as produced by `generate-excel`. Tabs and columns may be removed (except `id` columns) as long as the column names match.                       |

# Causal Inference, AI Systems & Data Science Portfolio

This repository contains a Quarto website for a professional GitHub Pages portfolio focused on industry-oriented causal inference, trustworthy AI systems, and data science.

The site is organized as a living knowledge hub:

- `projects/`: industry-style causal inference case studies.
- `expertise/`: professional pillars for causal inference and AI systems.
- `notes/`: lecture notes and technical explainers.
- `tutorials/`: Python package tutorials for causal inference and AI systems.
- `posts/`: blog-style essays.
- `templates/`: reusable page templates for future additions.
- `notebooks/`: Jupyter notebooks linked from project and tutorial pages.
- `data/`: public, synthetic, or shareable datasets only.

## Local Preview

Install Quarto from <https://quarto.org/docs/get-started/>. Then run:

```bash
quarto preview
```

The project is configured to preview on <http://localhost:4200>.

## Render

```bash
quarto render
```

The rendered site is written to `_site/`.

## Publish With GitHub Pages

This repository includes a GitHub Actions workflow at `.github/workflows/publish.yml`.

In your GitHub repository:

1. Go to **Settings -> Pages**.
2. Under **Build and deployment**, set **Source** to **GitHub Actions**.
3. Push to `main`.

## Before Publishing

Replace placeholders in:

- `_quarto.yml`
- `about.qmd`
- `cv.qmd`
- `index.qmd`

Search for `YOUR-`, `YOUR `, and `example.edu`.

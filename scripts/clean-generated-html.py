#!/usr/bin/env python3
"""Clean generated HTML metadata and selected site conveniences."""

from __future__ import annotations

from html import escape, unescape
import os
import re
import shutil
from pathlib import Path


SITE_DIR = Path("_site")
NOTEBOOK_HTML_DIR = SITE_DIR / "notebooks"
LECTURE_HTML_DIR = SITE_DIR / "notebooks" / "lectures"
TUTORIAL_HTML_DIR = SITE_DIR / "notebooks" / "tutorials"
PROJECT_HTML_DIR = SITE_DIR / "notebooks" / "projects"
EXTERNAL_LINK_RE = re.compile(
    r'(<a\b(?=[^>]*\bhref="https?://[^"]+")[^>]*)(>)'
)
NEW_TAB_LINK_RE = re.compile(
    r'(<a\b(?=[^>]*\bhref="(?:https://scholar\.google\.com/citations\?[^"]*|https://erau\.edu/?[^"]*|https://www\.linkedin\.com/in/prashant-shekhar-36586a28/?[^"]*)")[^>]*)(>)'
)
ANCHOR_RE = re.compile(r'<a\b[^>]*\bhref="(?P<href>[^"]+)"[^>]*>')
BODY_CLASS_RE = re.compile(r'<body class="(?P<classes>[^"]*)"')
NAVBAR_TITLE_BRAND_RE = re.compile(
    r'<a class="navbar-brand" href="[^"]*"[^>]*>\s*'
    r'(?:<img[^>]*class="navbar-logo"[^>]*>\s*)?'
    r'<span class="navbar-title">Prashant Shekhar</span>\s*</a>',
    re.DOTALL,
)
TITLE_RE = re.compile(r"<h1(?:\s+[^>]*)?>(?P<title>.*?)</h1>", re.DOTALL)
HTML_TAG_RE = re.compile(r"<[^>]+>")
NOTEBOOK_PAGER_RE = re.compile(
    r'\n<nav class="lecture-pager" aria-label="[^"]+">.*?</nav>\n',
    re.DOTALL,
)
NOTEBOOK_HOME_LINK_RE = re.compile(
    r'<a\b[^>]*\bdata-site-path="(?P<site_path>notebooks/(?:lectures|tutorials|projects)/[^"]+)"[^>]*>'
)
MAIN_CLOSE = "</main> <!-- /main -->"

PROJECT_LAB_HOME_SLUGS = {
    "project_1_ranking": "ranking-recommendation-lift-lab",
    "project_2_off_policy_evaluation": "off-policy-evaluation-bandit-lab",
    "project_3_long_term_causal_effects": "long-term-recommender-effects-lab",
    "project_4_interference_spillover_effects": "interference-spillover-effects-lab",
    "project_5_discovery_quality_mediation": "discovery-quality-mediation-lab",
}

PROJECT_LAB_SEQUENCES = (
    (
        "project_1_ranking",
        (
            "01_eda_mind.html",
            "02_propensity_ipw.html",
            "03_doubly_robust.html",
            "04_heterogeneous_effects.html",
            "05_policy_simulation.html",
            "06_sensitivity_and_limitations.html",
            "07_ml_nuisance_models.html",
            "08_econml_causal_ml.html",
        ),
    ),
    (
        "project_2_off_policy_evaluation",
        (
            "01_open_bandit_eda.html",
            "02_behavior_policy_and_propensities.html",
            "03_ips_and_snips.html",
            "04_doubly_robust_ope.html",
            "05_policy_comparison_and_sensitivity.html",
            "06_contextual_policy_learning.html",
        ),
    ),
    (
        "project_3_long_term_causal_effects",
        (
            "01_kuairec_sequence_eda.html",
            "02_long_term_outcome_definition.html",
            "03_time_varying_confounding_and_propensity.html",
            "04_marginal_structural_model.html",
            "05_g_computation.html",
            "06_doubly_robust_heterogeneous_effects.html",
        ),
    ),
    (
        "project_4_interference_spillover_effects",
        (
            "01_movielens_interference_setup_eda.html",
            "02_spillover_exposure_mapping.html",
            "03_cluster_randomized_estimators.html",
            "04_direct_indirect_total_effects.html",
            "05_advanced_spillover_models.html",
        ),
    ),
    (
        "project_5_discovery_quality_mediation",
        (
            "01_discovery_quality_problem_setup_eda.html",
            "02_metric_construction_and_validation.html",
            "03_mediation_estimands_and_assumptions.html",
            "04_direct_indirect_total_effects.html",
            "05_robustness_and_sensitivity.html",
            "06_advanced_sem_and_ml_mediation.html",
        ),
    ),
)

HTML_REPLACEMENTS = (
    (
        re.compile(
            r'(<div class="nav-footer-left">\s*)<p>Prashant Shekhar</p>',
            re.DOTALL,
        ),
        r"\1<p>Copyright@Prashant Shekhar, 2026</p>",
    ),
    (re.compile(r'\sdata-listing-date-sort="[^"]*"'), ""),
    (re.compile(r'\sdata-listing-file-modified-sort="[^"]*"'), ""),
    (re.compile(r'\sdata-quarto-private-\d+="[^"]*"'), ""),
    (re.compile(r",\s*\{\s*data:\s*\['listing-date-sort'\]\s*\}"), ""),
    (re.compile(r",\s*\{\s*data:\s*\['listing-file-modified-sort'\]\s*\}"), ""),
    (
        re.compile(
            r'\n\s*<meta[^>]+(?:datePublished|dateModified|article:published_time|citation_publication_date)[^>]*>\s*',
            re.IGNORECASE,
        ),
        "\n",
    ),
)

DATED_SLUG = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")


def scrub_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    cleaned = text
    for pattern, replacement in HTML_REPLACEMENTS:
        cleaned = pattern.sub(replacement, cleaned)
    cleaned = normalize_navbar_brand(cleaned)
    cleaned = NEW_TAB_LINK_RE.sub(add_new_tab_attrs, cleaned)
    if is_rendered_notebook_page(path) or is_resources_page(path):
        cleaned = EXTERNAL_LINK_RE.sub(add_new_tab_attrs, cleaned)
    if is_rendered_notebook_page(path):
        cleaned = add_body_class(cleaned, "notebook-page")
    cleaned = normalize_internal_link_targets(cleaned)

    if cleaned == text:
        return False

    path.write_text(cleaned, encoding="utf-8")
    return True


def add_body_class(text: str, class_name: str) -> str:
    """Add a stable body class to generated pages that need custom behavior."""

    def replace(match: re.Match[str]) -> str:
        classes = match.group("classes").split()
        if class_name not in classes:
            classes.append(class_name)
        return f'<body class="{" ".join(classes)}"'

    return BODY_CLASS_RE.sub(replace, text, count=1)


def add_new_tab_attrs(match: re.Match[str]) -> str:
    tag_start, tag_end = match.groups()
    if ' target="' not in tag_start:
        tag_start += ' target="_blank"'
    if ' rel="' not in tag_start:
        tag_start += ' rel="noopener noreferrer"'
    return f"{tag_start}{tag_end}"


def normalize_internal_link_targets(text: str) -> str:
    """Keep same-site navigation in the current tab.

    Quarto and the post-render cleanup intentionally open external scholarly
    and institutional resources in new tabs. Internal links should behave like
    normal site navigation so the browser back button remains useful.
    """

    def replace(match: re.Match[str]) -> str:
        tag = match.group(0)
        href = match.group("href")
        if not is_internal_href(href):
            return tag

        tag = re.sub(r'\s+target="_blank"', "", tag)
        tag = re.sub(r'\s+rel="noopener noreferrer"', "", tag)
        return tag

    return ANCHOR_RE.sub(replace, text)


def is_internal_href(href: str) -> bool:
    """Return True when a link points to this site or to a relative path."""

    normalized = href.lower()
    if normalized.startswith("#"):
        return True
    if normalized.startswith(("mailto:", "tel:", "javascript:")):
        return False
    if normalized.startswith(("http://", "https://")):
        return normalized.startswith("https://p-shekhar.github.io/")
    return True


def normalize_navbar_brand(text: str) -> str:
    if "navbar-brand-logo" in text:
        return NAVBAR_TITLE_BRAND_RE.sub("", text)

    return NAVBAR_TITLE_BRAND_RE.sub(linkedin_navbar_brand, text)


def linkedin_navbar_brand(_match: re.Match[str]) -> str:
    return (
        '<a class="navbar-brand" '
        'href="https://www.linkedin.com/in/prashant-shekhar-36586a28/" '
        'target="_blank" rel="noopener noreferrer">\n'
        '    <img src="/assets/linkedin-brand.svg" alt="LinkedIn profile" '
        'class="navbar-logo">\n'
        '    <span class="navbar-title">Prashant Shekhar</span>\n'
        '    </a>'
    )


def is_rendered_notebook_page(path: Path) -> bool:
    if not path.is_relative_to(NOTEBOOK_HTML_DIR):
        return False

    relative = path.relative_to(NOTEBOOK_HTML_DIR)
    return "outputs" not in relative.parts


def is_resources_page(path: Path) -> bool:
    return path == SITE_DIR / "resources.html"


def get_page_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    match = TITLE_RE.search(text)
    if not match:
        return path.stem.replace("_", " ").replace("-", " ").title()

    title = HTML_TAG_RE.sub("", match.group("title"))
    return unescape(" ".join(title.split()))


def build_notebook_pager(
    previous_page: Path | None,
    next_page: Path | None,
    titles: dict[Path, str],
    previous_label: str,
    next_label: str,
    aria_label: str,
    home_page: Path | None = None,
    home_title: str | None = None,
    home_label: str = "Home",
    current_page: Path | None = None,
) -> str:
    links: list[str] = []

    if previous_page is not None:
        links.append(
            '<a class="lecture-pager-link lecture-pager-prev" '
            f'href="{escape(previous_page.name, quote=True)}">'
            f'<span class="lecture-pager-kicker">{escape(previous_label)}</span>'
            f'<span class="lecture-pager-title">{escape(titles[previous_page])}</span>'
            "</a>"
        )

    if home_page is not None and current_page is not None:
        relative_home = os.path.relpath(home_page, start=current_page.parent)
        links.append(
            '<a class="lecture-pager-link lecture-pager-home" '
            f'href="{escape(relative_home, quote=True)}">'
            f'<span class="lecture-pager-kicker">{escape(home_label)}</span>'
            f'<span class="lecture-pager-title">{escape(home_title or "Full sequence")}</span>'
            "</a>"
        )

    if next_page is not None:
        links.append(
            '<a class="lecture-pager-link lecture-pager-next" '
            f'href="{escape(next_page.name, quote=True)}">'
            f'<span class="lecture-pager-kicker">{escape(next_label)}</span>'
            f'<span class="lecture-pager-title">{escape(titles[next_page])}</span>'
            "</a>"
        )

    return (
        f'\n<nav class="lecture-pager" aria-label="{escape(aria_label, quote=True)}">\n'
        + "\n".join(links)
        + "\n</nav>\n"
    )


def build_notebook_home_map(index_root: Path, site_path_prefix: str) -> dict[Path, Path]:
    """Map rendered notebook pages to the index page that lists them."""
    if not index_root.exists():
        return {}

    home_by_notebook: dict[Path, Path] = {}
    for index_page in sorted(index_root.rglob("index.html")):
        text = index_page.read_text(encoding="utf-8")
        for match in NOTEBOOK_HOME_LINK_RE.finditer(text):
            site_path = unescape(match.group("site_path"))
            if not site_path.startswith(site_path_prefix):
                continue
            notebook_path = SITE_DIR / site_path
            home_by_notebook[notebook_path] = index_page

    return home_by_notebook


def build_project_lab_home_map() -> dict[Path, Path]:
    """Map project lab notebooks to the current lab summary pages."""
    home_by_notebook: dict[Path, Path] = {}
    for lab_dir_name, page_names in PROJECT_LAB_SEQUENCES:
        home_slug = PROJECT_LAB_HOME_SLUGS.get(lab_dir_name)
        if home_slug is None:
            continue

        home_page = SITE_DIR / "projects" / home_slug / "index.html"
        if not home_page.exists():
            continue

        for page_name in page_names:
            notebook_page = PROJECT_HTML_DIR / lab_dir_name / page_name
            if notebook_page.exists():
                home_by_notebook[notebook_page] = home_page

    return home_by_notebook


def inject_notebook_pager(path: Path, pager: str) -> bool:
    text = path.read_text(encoding="utf-8")
    cleaned = NOTEBOOK_PAGER_RE.sub("\n", text)

    if MAIN_CLOSE not in cleaned:
        return False

    updated = cleaned.replace(MAIN_CLOSE, f"{pager}{MAIN_CLOSE}", 1)
    if updated == text:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


def add_notebook_pagers(
    root_dir: Path,
    previous_label: str,
    next_label: str,
    aria_label: str,
    home_by_notebook: dict[Path, Path] | None = None,
    home_label: str = "Home",
) -> int:
    if not root_dir.exists():
        return 0

    changed = 0
    home_by_notebook = home_by_notebook or {}
    course_dirs = sorted(
        {
            path.parent
            for path in root_dir.rglob("*.html")
            if is_rendered_notebook_page(path)
        }
    )
    for course_dir in course_dirs:
        pages = sorted(
            path for path in course_dir.glob("*.html") if is_rendered_notebook_page(path)
        )
        if len(pages) < 2:
            continue

        titles = {page: get_page_title(page) for page in pages}
        for index, page in enumerate(pages):
            previous_page = pages[index - 1] if index > 0 else None
            next_page = pages[index + 1] if index + 1 < len(pages) else None
            pager = build_notebook_pager(
                previous_page,
                next_page,
                titles,
                previous_label,
                next_label,
                aria_label,
                home_page=home_by_notebook.get(page),
                home_title=(
                    get_page_title(home_by_notebook[page])
                    if page in home_by_notebook
                    else None
                ),
                home_label=home_label,
                current_page=page,
            )
            if inject_notebook_pager(page, pager):
                changed += 1

    return changed


def add_project_lab_pagers() -> int:
    if not PROJECT_HTML_DIR.exists():
        return 0

    changed = 0
    home_by_notebook = build_project_lab_home_map()
    for lab_dir_name, page_names in PROJECT_LAB_SEQUENCES:
        pages = [PROJECT_HTML_DIR / lab_dir_name / page_name for page_name in page_names]
        pages = [page for page in pages if page.exists()]
        if len(pages) < 2:
            continue

        titles = {page: get_page_title(page) for page in pages}
        for index, page in enumerate(pages):
            previous_page = pages[index - 1] if index > 0 else None
            next_page = pages[index + 1] if index + 1 < len(pages) else None
            pager = build_notebook_pager(
                previous_page,
                next_page,
                titles,
                previous_label="Previous Notebook",
                next_label="Next Notebook",
                aria_label="Project lab notebook navigation",
                home_page=home_by_notebook.get(page),
                home_title=(
                    get_page_title(home_by_notebook[page])
                    if page in home_by_notebook
                    else None
                ),
                home_label="Lab Home",
                current_page=page,
            )
            if inject_notebook_pager(page, pager):
                changed += 1

    return changed


def remove_dated_post_dirs() -> int:
    posts_dir = SITE_DIR / "posts"
    if not posts_dir.exists():
        return 0

    removed = 0
    for path in posts_dir.iterdir():
        if path.is_dir() and DATED_SLUG.search(path.name):
            shutil.rmtree(path)
            removed += 1
    return removed


def main() -> None:
    if not SITE_DIR.exists():
        return

    changed = sum(1 for path in SITE_DIR.rglob("*.html") if scrub_html(path))
    lecture_course_homes = build_notebook_home_map(
        SITE_DIR / "notes",
        "notebooks/lectures/",
    )
    tutorial_homes = build_notebook_home_map(
        SITE_DIR / "tutorials",
        "notebooks/tutorials/",
    )
    lecture_pagers = add_notebook_pagers(
        LECTURE_HTML_DIR,
        previous_label="Previous Lecture",
        next_label="Next Lecture",
        aria_label="Lecture navigation",
        home_by_notebook=lecture_course_homes,
        home_label="Course Home",
    )
    tutorial_pagers = add_notebook_pagers(
        TUTORIAL_HTML_DIR,
        previous_label="Previous Tutorial",
        next_label="Next Tutorial",
        aria_label="Tutorial navigation",
        home_by_notebook=tutorial_homes,
        home_label="Tutorial Home",
    )
    project_lab_pagers = add_project_lab_pagers()
    removed_dirs = remove_dated_post_dirs()
    print(f"Cleaned generated HTML in {changed} files.")
    print(f"Updated lecture navigation in {lecture_pagers} files.")
    print(f"Updated tutorial navigation in {tutorial_pagers} files.")
    print(f"Updated project lab navigation in {project_lab_pagers} files.")
    if removed_dirs:
        print(f"Removed {removed_dirs} stale dated post directories.")


if __name__ == "__main__":
    main()

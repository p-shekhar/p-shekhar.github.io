"""Optional real-data loaders for lecture companion sections.

The lecture notebooks use synthetic data for controlled teaching examples.
These helpers add small, cacheable real-data companions without making the
website render depend on live public APIs.
"""

from __future__ import annotations

import io
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path
from typing import Iterable

import pandas as pd
from IPython.display import Markdown, display

DATA_DIR = Path(__file__).resolve().parents[1] / "_data"


def optional_data_note(dataset_name: str, source_url: str, enable_variable: str) -> None:
    """Display a short note when a real-data companion is intentionally skipped.

    Parameters
    ----------
    dataset_name:
        Human-readable name of the public dataset used by the companion.
    source_url:
        Official source page or API endpoint for the dataset.
    enable_variable:
        Name of the notebook flag that turns on the live data pull.

    Returns
    -------
    None
        The function displays Markdown in the notebook and does not return data.
    """

    display(
        Markdown(
            f"**Optional real-data companion skipped.** Set `{enable_variable} = True` "
            f"to pull a small sample from [{dataset_name}]({source_url}). The default "
            "keeps website rendering fast and avoids making the lecture depend on a "
            "live external API."
        )
    )


def _ensure_data_dir() -> Path:
    """Create the local data cache directory if it does not already exist."""

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def _read_cached_csv(cache_name: str) -> pd.DataFrame | None:
    """Read a cached CSV from the shared notebook data directory if present."""

    path = DATA_DIR / cache_name
    if path.exists():
        return pd.read_csv(path)
    return None


def _write_cached_csv(df: pd.DataFrame, cache_name: str) -> pd.DataFrame:
    """Persist a fetched public-data sample as CSV and return the same DataFrame."""

    _ensure_data_dir()
    df.to_csv(DATA_DIR / cache_name, index=False)
    return df


def _download_bytes(url: str, timeout: int = 60) -> bytes:
    """Download bytes from a public URL with a notebook-friendly user agent."""

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "portfolio-lecture-real-data-companion/1.0"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def _read_csv_from_zip_bytes(zip_bytes: bytes, target_filename: str, **read_csv_kwargs) -> pd.DataFrame:
    """Read a CSV by filename from a ZIP archive, including one level of nested ZIPs."""

    with zipfile.ZipFile(io.BytesIO(zip_bytes)) as archive:
        for name in archive.namelist():
            if name.endswith(target_filename):
                with archive.open(name) as file:
                    return pd.read_csv(file, **read_csv_kwargs)

        for name in archive.namelist():
            if name.endswith(".zip"):
                with archive.open(name) as nested_file:
                    return _read_csv_from_zip_bytes(
                        nested_file.read(),
                        target_filename,
                        **read_csv_kwargs,
                    )

    raise FileNotFoundError(f"Could not find {target_filename!r} inside the downloaded ZIP archive.")


def fetch_nyc_311(
    *,
    limit: int = 5_000,
    start_date: str = "2025-01-01",
    cache_name: str = "nyc_311_sample.csv",
) -> pd.DataFrame:
    """Fetch a small cacheable sample of NYC 311 service requests.

    Parameters
    ----------
    limit:
        Maximum number of recent closed service requests to request.
    start_date:
        Lower bound for created dates, in ``YYYY-MM-DD`` format.
    cache_name:
        CSV filename used to cache the downloaded sample under ``notebooks/_data``.

    Returns
    -------
    pandas.DataFrame
        Service-request records with parsed date columns when available.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return _parse_dates(cached, ["created_date", "closed_date", "due_date"])

    columns = [
        "unique_key",
        "created_date",
        "closed_date",
        "agency",
        "complaint_type",
        "descriptor",
        "borough",
        "open_data_channel_type",
        "status",
        "due_date",
        "incident_zip",
    ]
    params = {
        "$select": ",".join(columns),
        "$where": f"created_date >= '{start_date}T00:00:00' AND closed_date IS NOT NULL",
        "$limit": str(limit),
        "$order": "created_date DESC",
    }
    url = "https://data.cityofnewyork.us/resource/erm2-nwe9.json?" + urllib.parse.urlencode(params)
    df = pd.read_json(url)
    df = _parse_dates(df, ["created_date", "closed_date", "due_date"])
    return _write_cached_csv(df, cache_name)


def load_uci_bank_marketing(cache_name: str = "uci_bank_marketing_bank_full.csv") -> pd.DataFrame:
    """Load the UCI Bank Marketing dataset from a local cache or the UCI ZIP file.

    Returns
    -------
    pandas.DataFrame
        The ``bank-full.csv`` table with semicolon-delimited fields parsed.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return cached

    url = "https://archive.ics.uci.edu/static/public/222/bank+marketing.zip"
    df = _read_csv_from_zip_bytes(_download_bytes(url), "bank-full.csv", sep=";")
    return _write_cached_csv(df, cache_name)


def load_uci_bike_sharing(cache_name: str = "uci_bike_sharing_hour.csv") -> pd.DataFrame:
    """Load the UCI Bike Sharing hourly dataset from a cache or the UCI ZIP file.

    Returns
    -------
    pandas.DataFrame
        The hourly bike-rental table with the date column parsed.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return _parse_dates(cached, ["dteday"])

    url = "https://archive.ics.uci.edu/static/public/275/bike+sharing+dataset.zip"
    df = _read_csv_from_zip_bytes(_download_bytes(url), "hour.csv")
    df = _parse_dates(df, ["dteday"])
    return _write_cached_csv(df, cache_name)


def load_statsmodels_randhie(cache_name: str = "statsmodels_randhie.csv") -> pd.DataFrame:
    """Load the RAND Health Insurance Experiment data bundled with statsmodels.

    Returns
    -------
    pandas.DataFrame
        The RAND HIE table with outpatient physician visits, plan cost sharing,
        deductible-plan status, incentive payments, and health-status variables.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return cached

    import statsmodels.api as sm

    df = sm.datasets.randhie.load_pandas().data.copy()
    return _write_cached_csv(df, cache_name)


def load_statsmodels_star98(cache_name: str = "statsmodels_star98.csv") -> pd.DataFrame:
    """Load the California STAR98 grouped-binomial education data.

    Returns
    -------
    pandas.DataFrame
        County-level counts above and below the national median, plus school
        and demographic covariates.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return cached

    import statsmodels.api as sm

    df = sm.datasets.star98.load_pandas().data.copy()
    return _write_cached_csv(df, cache_name)


def load_statsmodels_grunfeld(cache_name: str = "statsmodels_grunfeld.csv") -> pd.DataFrame:
    """Load the Grunfeld firm investment panel bundled with statsmodels.

    Returns
    -------
    pandas.DataFrame
        Firm-year observations on gross investment, market value, capital stock,
        firm identity, and year.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return cached

    import statsmodels.api as sm

    df = sm.datasets.grunfeld.load_pandas().data.copy()
    return _write_cached_csv(df, cache_name)


def load_statsmodels_spector(cache_name: str = "statsmodels_spector.csv") -> pd.DataFrame:
    """Load the Spector and Mazzeo binary-outcome teaching data.

    Returns
    -------
    pandas.DataFrame
        Student-level observations with GPA, test score, program participation,
        and a binary grade-improvement outcome.
    """

    cached = _read_cached_csv(cache_name)
    if cached is not None:
        return cached

    import statsmodels.api as sm

    df = sm.datasets.spector.load_pandas().data.copy()
    return _write_cached_csv(df, cache_name)


def _parse_dates(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
    """Parse listed date columns when they are present in a DataFrame."""

    parsed = df.copy()
    for column in columns:
        if column in parsed.columns:
            parsed[column] = pd.to_datetime(parsed[column], errors="coerce")
    return parsed

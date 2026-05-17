"""
publication_trend_analysis.py

Generates bibliometric and publication trend figures for the QC-AI-BC SLR.

Expected input:
    data/bibliometric_dataset.csv
or:
    data/processed/cleaned_metadata.csv

Useful columns:
    year, document_type, source_title, publisher, country

Outputs:
    outputs/figures/Annual Distribution of Publications on AI–BC–QC Convergence.png
    outputs/figures/Year-wise Distribution of Publications by Type.png
    outputs/figures/Top Publication Venues for AI–BC–QC Convergence Studies.png
    outputs/figures/Long-Tail Distribution of Publication Venues.png
    outputs/figures/Publisher-wise Distribution of Studies on AI–BC–QC Convergence.png
    outputs/figures/Geographical Distribution of Publications on AI–BC–QC Convergence.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "outputs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_data() -> pd.DataFrame | None:
    candidates = [
        DATA_DIR / "bibliometric_dataset.csv",
        DATA_DIR / "processed" / "cleaned_metadata.csv",
        DATA_DIR / "included_studies_metadata.csv",
    ]

    for path in candidates:
        if path.exists():
            print(f"Using input file: {path}")
            return pd.read_csv(path)

    print("No metadata file found. Add bibliometric_dataset.csv or included_studies_metadata.csv in data/.")
    return None


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(" ", "_", regex=False)
    return df


def save_bar(series: pd.Series, title: str, xlabel: str, ylabel: str, filename: str) -> None:
    if series.empty:
        print(f"Skipped empty figure: {filename}")
        return

    plt.figure(figsize=(10, 6))
    series.plot(kind="bar")
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    out = FIG_DIR / filename
    plt.savefig(out, dpi=300)
    plt.close()
    print(f"Saved: {out}")


def main() -> None:
    df = load_data()
    if df is None:
        return

    df = clean_columns(df)

    if "year" in df.columns:
        year_counts = df["year"].dropna().astype(int).value_counts().sort_index()
        save_bar(
            year_counts,
            "Annual Distribution of Publications on AI–BC–QC Convergence",
            "Year",
            "Number of Publications",
            "Annual Distribution of Publications on AI–BC–QC Convergence.png",
        )

    if {"year", "document_type"}.issubset(df.columns):
        pivot = pd.crosstab(df["year"], df["document_type"])
        plt.figure(figsize=(11, 6))
        pivot.plot(kind="bar", stacked=True, figsize=(11, 6))
        plt.title("Year-wise Distribution of Publications by Type")
        plt.xlabel("Year")
        plt.ylabel("Number of Publications")
        plt.tight_layout()
        out = FIG_DIR / "Year-wise Distribution of Publications by Type.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")

    venue_col = "source_title" if "source_title" in df.columns else "venue" if "venue" in df.columns else None
    if venue_col:
        venue_counts = df[venue_col].dropna().value_counts()
        save_bar(
            venue_counts.head(15),
            "Top Publication Venues for AI–BC–QC Convergence Studies",
            "Venue",
            "Number of Publications",
            "Top Publication Venues for AI–BC–QC Convergence Studies.png",
        )

        save_bar(
            venue_counts.reset_index(drop=True),
            "Long-Tail Distribution of Publication Venues",
            "Venue Rank",
            "Number of Publications",
            "Long-Tail Distribution of Publication Venues.png",
        )

    if "publisher" in df.columns:
        publisher_counts = df["publisher"].dropna().value_counts().head(15)
        save_bar(
            publisher_counts,
            "Publisher-wise Distribution of Studies on AI–BC–QC Convergence",
            "Publisher",
            "Number of Publications",
            "Publisher-wise Distribution of Studies on AI–BC–QC Convergence.png",
        )

    country_col = "country" if "country" in df.columns else "corresponding_author_country" if "corresponding_author_country" in df.columns else None
    if country_col:
        country_counts = df[country_col].dropna().value_counts().head(20)
        save_bar(
            country_counts,
            "Geographical Distribution of Publications on AI–BC–QC Convergence",
            "Country",
            "Number of Publications",
            "Geographical Distribution of Publications on AI–BC–QC Convergence.png",
        )


if __name__ == "__main__":
    main()

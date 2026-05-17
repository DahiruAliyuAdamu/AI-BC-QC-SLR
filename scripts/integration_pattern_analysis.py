"""
integration_pattern_analysis.py

Generates integration-pattern figures for the QC-AI-BC SLR.

Expected input:
    data/coded_dataset.csv

Useful columns:
    integration_pattern, ai_role, blockchain_role, quantum_role, application_domain

Outputs:
    outputs/figures/AI–Blockchain–Quantum Integration Patterns.png
    outputs/figures/Core AI roles in AI–blockchain–quantum systems.png
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "outputs" / "figures"
FIG_DIR.mkdir(parents=True, exist_ok=True)


def load_data() -> pd.DataFrame | None:
    path = DATA_DIR / "coded_dataset.csv"
    if not path.exists():
        print(f"Input file not found: {path}")
        return None

    df = pd.read_csv(path)
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

    if "integration_pattern" in df.columns:
        counts = df["integration_pattern"].dropna().value_counts()
        save_bar(
            counts,
            "AI–Blockchain–Quantum Integration Patterns",
            "Integration Pattern",
            "Number of Studies",
            "AI–Blockchain–Quantum Integration Patterns.png",
        )

    if "ai_role" in df.columns:
        counts = df["ai_role"].dropna().value_counts().head(12)
        save_bar(
            counts,
            "Core AI roles in AI–blockchain–quantum systems",
            "AI Role",
            "Number of Studies",
            "Core AI roles in AI–blockchain–quantum systems.png",
        )

    if "application_domain" in df.columns:
        counts = df["application_domain"].dropna().value_counts().head(15)
        save_bar(
            counts,
            "Application Domains in AI–BC–QC Studies",
            "Application Domain",
            "Number of Studies",
            "Application Domains in AI–BC–QC Studies.png",
        )


if __name__ == "__main__":
    main()

"""
validation_analysis.py

Generates quality and validation-related figures for the QC-AI-BC SLR.

Expected input:
    data/coded_dataset.csv

Useful columns:
    quality_score, validation_strategy, evaluation_context

Outputs:
    outputs/figures/Quality score distribution of the publications.png
    outputs/figures/Validation Strategy Distribution.png
    outputs/figures/Evaluation Context Distribution.png
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


def main() -> None:
    df = load_data()
    if df is None:
        return

    if "quality_score" in df.columns:
        scores = pd.to_numeric(df["quality_score"], errors="coerce").dropna()

        plt.figure(figsize=(10, 6))
        plt.hist(scores, bins=10, edgecolor="black")
        plt.axvline(4.5, linestyle="--")
        plt.title("Quality score distribution of the publications")
        plt.xlabel("Quality and Eligibility Score")
        plt.ylabel("Number of Publications")
        plt.tight_layout()
        out = FIG_DIR / "Quality score distribution of the publications.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")

    if "validation_strategy" in df.columns:
        counts = df["validation_strategy"].dropna().value_counts()
        plt.figure(figsize=(10, 6))
        counts.plot(kind="bar")
        plt.title("Validation Strategy Distribution")
        plt.xlabel("Validation Strategy")
        plt.ylabel("Number of Studies")
        plt.tight_layout()
        out = FIG_DIR / "Validation Strategy Distribution.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")

    if "evaluation_context" in df.columns:
        counts = df["evaluation_context"].dropna().value_counts()
        plt.figure(figsize=(10, 6))
        counts.plot(kind="bar")
        plt.title("Evaluation Context Distribution")
        plt.xlabel("Evaluation Context")
        plt.ylabel("Number of Studies")
        plt.tight_layout()
        out = FIG_DIR / "Evaluation Context Distribution.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()

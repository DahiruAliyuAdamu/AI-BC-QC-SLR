"""
maturity_analysis.py

Generates maturity-related figures for the QC-AI-BC SLR.

Expected input:
    data/coded_dataset.csv

Useful columns:
    maturity_level, implementation_maturity, validation_rigor,
    application_domain, projected_investment

Outputs:
    outputs/figures/Maturity Distribution of AI–BC–QC Studies.png
    outputs/figures/Maturity gap between prototype validation and real-world deployment.png
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

    if "maturity_level" in df.columns:
        counts = df["maturity_level"].dropna().value_counts()
        plt.figure(figsize=(10, 6))
        counts.plot(kind="bar")
        plt.title("Maturity Distribution of AI–BC–QC Studies")
        plt.xlabel("Maturity Level")
        plt.ylabel("Number of Studies")
        plt.tight_layout()
        out = FIG_DIR / "Maturity Distribution of AI–BC–QC Studies.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")

    required = {"implementation_maturity", "validation_rigor"}
    if required.issubset(df.columns):
        plot_df = df.dropna(subset=["implementation_maturity", "validation_rigor"]).copy()

        if "projected_investment" in plot_df.columns:
            sizes = pd.to_numeric(plot_df["projected_investment"], errors="coerce").fillna(1) * 80
        else:
            sizes = 180

        plt.figure(figsize=(9, 7))
        plt.scatter(
            pd.to_numeric(plot_df["implementation_maturity"], errors="coerce"),
            pd.to_numeric(plot_df["validation_rigor"], errors="coerce"),
            s=sizes,
            alpha=0.7,
        )
        plt.title("Maturity gap between prototype validation and real-world deployment")
        plt.xlabel("Implementation Maturity")
        plt.ylabel("Validation Rigor")
        plt.tight_layout()
        out = FIG_DIR / "Maturity gap between prototype validation and real-world deployment.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()

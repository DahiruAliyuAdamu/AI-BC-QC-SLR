"""
reproducibility_analysis.py

Generates reproducibility-related figures for the QC-AI-BC SLR.

Expected input:
    data/coded_dataset.csv

Useful columns:
    code_available, data_available, reproducibility_status, artifact_available

Outputs:
    outputs/figures/Reproducibility Status Distribution.png
    outputs/figures/Reproducibility Evidence Summary.png
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

    if "reproducibility_status" in df.columns:
        counts = df["reproducibility_status"].dropna().value_counts()
        plt.figure(figsize=(10, 6))
        counts.plot(kind="bar")
        plt.title("Reproducibility Status Distribution")
        plt.xlabel("Reproducibility Status")
        plt.ylabel("Number of Studies")
        plt.tight_layout()
        out = FIG_DIR / "Reproducibility Status Distribution.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")

    evidence_cols = [c for c in ["code_available", "data_available", "artifact_available"] if c in df.columns]
    if evidence_cols:
        summary = {}
        for col in evidence_cols:
            summary[col.replace("_", " ").title()] = df[col].astype(str).str.lower().isin(["yes", "true", "1", "available"]).sum()

        plt.figure(figsize=(9, 6))
        pd.Series(summary).plot(kind="bar")
        plt.title("Reproducibility Evidence Summary")
        plt.xlabel("Evidence Type")
        plt.ylabel("Number of Studies")
        plt.tight_layout()
        out = FIG_DIR / "Reproducibility Evidence Summary.png"
        plt.savefig(out, dpi=300)
        plt.close()
        print(f"Saved: {out}")


if __name__ == "__main__":
    main()

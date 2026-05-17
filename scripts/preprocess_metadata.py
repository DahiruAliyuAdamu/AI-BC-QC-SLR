"""
preprocess_metadata.py

Preprocesses metadata files for the QC-AI-BC systematic literature review.
The script cleans column names, removes duplicates, and saves a processed metadata file.

Expected input:
    data/included_studies_metadata.csv

Output:
    data/processed/cleaned_metadata.csv
"""

from pathlib import Path
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUT_DIR = DATA_DIR / "processed"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "doi" in df.columns:
        df["doi"] = df["doi"].astype(str).str.lower().str.strip()
        df = df.drop_duplicates(subset=["doi"], keep="first")

    if "title" in df.columns:
        df["title_clean"] = df["title"].astype(str).str.lower().str.strip()
        df = df.drop_duplicates(subset=["title_clean"], keep="first")
        df = df.drop(columns=["title_clean"])

    return df


def main() -> None:
    input_file = DATA_DIR / "included_studies_metadata.csv"

    if not input_file.exists():
        print(f"Input file not found: {input_file}")
        print("Please add included_studies_metadata.csv inside the data/ folder.")
        return

    df = pd.read_csv(input_file)
    df = normalize_columns(df)
    df = remove_duplicates(df)

    output_file = OUT_DIR / "cleaned_metadata.csv"
    df.to_csv(output_file, index=False)

    print(f"Cleaned metadata saved to: {output_file}")
    print(f"Total records after preprocessing: {len(df)}")


if __name__ == "__main__":
    main()

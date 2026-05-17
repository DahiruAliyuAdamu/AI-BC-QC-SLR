"""
generate_figures.py

Master script for running all QC-AI-BC SLR analysis scripts.
Run from repository root:

    python scripts/generate_figures.py
"""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "scripts"

SCRIPTS = [
    "preprocess_metadata.py",
    "publication_trend_analysis.py",
    "integration_pattern_analysis.py",
    "maturity_analysis.py",
    "validation_analysis.py",
    "reproducibility_analysis.py",
]


def run_script(script_name: str) -> None:
    script_path = SCRIPT_DIR / script_name
    if not script_path.exists():
        print(f"Skipped missing script: {script_path}")
        return

    print(f"\nRunning {script_name}...")
    result = subprocess.run([sys.executable, str(script_path)], cwd=ROOT)

    if result.returncode != 0:
        print(f"Warning: {script_name} ended with return code {result.returncode}")


def main() -> None:
    for script in SCRIPTS:
        run_script(script)

    print("\nAll available scripts have finished running.")


if __name__ == "__main__":
    main()

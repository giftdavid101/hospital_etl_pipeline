from pathlib import Path
import pandas as pd


def clean_hospital_data(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Clean hospital data for public-facing analysis.

    Keeps only:
    - age
    - gender
    - treatment_status

    Removes rows with missing values in those fields.
    """

    # Load raw data
    df = pd.read_csv(input_path)

    print(f"Raw rows: {len(df)}")

    # Keep only the parameters needed for public analysis
    df = df[["age", "gender", "treatment_status"]].copy()

    # Clean column values
    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    df["gender"] = (
        df["gender"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    df["treatment_status"] = (
        df["treatment_status"]
        .astype("string")
        .str.strip()
    )

    # Remove rows missing any required parameter
    df = df.dropna(
        subset=["age", "gender", "treatment_status"]
    )

    # Remove duplicate records
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(drop=True)

    # Create output directory if it does not exist
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned data
    df.to_csv(output_path, index=False)

    print(f"Clean rows: {len(df)}")
    print(f"Saved cleaned data to: {output_path}")

    return df


if __name__ == "__main__":
    clean_hospital_data(
        input_path="data/hospital.csv",
        output_path="data/processed/hospital_analysis.csv"
    )
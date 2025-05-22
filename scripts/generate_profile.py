import argparse
import os
import pandas as pd
import whylogs as why
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Generate WhyLogs profile from CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Output directory to save profile")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)

    # Load dataset
    df = pd.read_csv(args.input)

    # Generate profile
    results = why.log(df)
    profile = results.profile()

    # Serialize manually and write binary with safe name
    safe_time = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    out_file = os.path.join(args.output, f"profile_{safe_time}.bin")

    with open(out_file, "wb") as f:
        f.write(profile.serialize())

    print(f"WhyLogs profile saved as: {out_file}")

if __name__ == "__main__":
    main()
import argparse
import os
import pandas as pd
import whylogs as why
from whylogs.api.writer.local import LocalWriter
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="Generate WhyLogs profile from CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output directory")
    args = parser.parse_args()

    # Load CSV
    df = pd.read_csv(args.input)

    # Create output dir
    os.makedirs(args.output, exist_ok=True)

    # Generate profile
    results = why.log(df)

    # Write profile to disk using LocalWriter with a custom filename format
    safe_time = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    writer = LocalWriter(base_dir=args.output)
    writer.write(file_name=f"profile_{safe_time}.bin", profile=results.profile())

    print(f"WhyLogs profile saved to {args.output}/profile_{safe_time}.bin")

if __name__ == "__main__":
    main()
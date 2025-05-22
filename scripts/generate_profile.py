import argparse
import os
import pandas as pd
import whylogs as why
from whylogs.api.writer.file import FileWriter

def main():
    parser = argparse.ArgumentParser(description="Generate WhyLogs profile from CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to save WhyLogs profile")
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.input)

    # Generate profile
    profile = why.log(df).profile()

    # Save profile
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    writer = FileWriter(output_dir=os.path.dirname(args.output))
    writer.write(file_name=os.path.basename(args.output), profile=profile)

    print(f"WhyLogs profile saved to {args.output}")

if __name__ == "__main__":
    main()

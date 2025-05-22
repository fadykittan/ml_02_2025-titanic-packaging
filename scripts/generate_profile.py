import argparse
import os
import pandas as pd
import whylogs as why

def main():
    parser = argparse.ArgumentParser(description="Generate WhyLogs profile from CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output directory")
    args = parser.parse_args()

    # Load CSV
    df = pd.read_csv(args.input)

    # Generate profile
    results = why.log(df)

    # Write to disk using the LocalWriter
    os.makedirs(args.output, exist_ok=True)
    results.writer("local", base_dir=args.output).write()

    print(f"WhyLogs profile written to: {args.output}")

if __name__ == "__main__":
    main()
import argparse
import os
import pandas as pd
import whylogs as why

def main():
    parser = argparse.ArgumentParser(description="Generate WhyLogs profile from CSV")
    parser.add_argument("--input", required=True, help="Path to input CSV file")
    parser.add_argument("--output", required=True, help="Path to output binary profile")
    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.input)

    # Generate profile
    results = why.log(df)
    profile = results.profile()

    # Write profile to binary file
    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "wb") as f:
        f.write(profile.serialize())

    print(f"WhyLogs profile saved to {args.output}")

if __name__ == "__main__":
    main()
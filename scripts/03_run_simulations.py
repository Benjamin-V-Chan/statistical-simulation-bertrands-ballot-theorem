import pandas as pd

def compute_empirical_probability():
    df = pd.read_csv("outputs/simulation_results.csv")
    total = len(df)
    always_ahead_count = df["always_ahead"].sum()
    return always_ahead_count / total

def main():
    empirical_prob = compute_empirical_probability()
    df = pd.read_csv("outputs/ballot_sequences.csv")
    p, q = len(df["sequence"][0].split("A")) - 1, len(df["sequence"][0].split("B")) - 1
    theoretical_prob = (p - q) / (p + q)
    
    result = pd.DataFrame({"p": [p], "q": [q], "empirical_prob": [empirical_prob], "theoretical_prob": [theoretical_prob]})
    result.to_csv("outputs/probability_comparison.csv", index=False)

if __name__ == "__main__":
    main()
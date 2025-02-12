import pandas as pd

def is_always_ahead(sequence):
    a_count = 0
    b_count = 0
    for vote in sequence:
        if vote == "A":
            a_count += 1
        else:
            b_count += 1
        if b_count >= a_count:  # B should never overtake A
            return False
    return True

def main():
    df = pd.read_csv("outputs/ballot_sequences.csv")
    df["always_ahead"] = df["sequence"].apply(lambda seq: is_always_ahead(seq))
    df.to_csv("outputs/simulation_results.csv", index=False)

if __name__ == "__main__":
    main()
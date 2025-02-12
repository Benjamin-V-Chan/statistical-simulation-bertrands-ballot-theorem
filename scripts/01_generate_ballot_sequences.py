import random
import pandas as pd

def generate_ballot_sequence(p, q):
    votes = ["A"] * p + ["B"] * q
    random.shuffle(votes)
    return votes

def main():

    candidate_a_votes = 100
    canditate_b_votes = 300
    n_sequences = 1000

    sequences = [generate_ballot_sequence(candidate_a_votes, canditate_b_votes) for _ in range(n_sequences)]
    df = pd.DataFrame({"sequence": ["".join(seq) for seq in sequences]})
    df.to_csv("outputs/ballot_sequences.csv", index=False)

if __name__ == "__main__":
    main()
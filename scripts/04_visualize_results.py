import pandas as pd
import matplotlib.pyplot as plt

def plot_probabilities():
    df = pd.read_csv("outputs/probability_comparison.csv")
    categories = ["Empirical", "Theoretical"]
    values = [df["empirical_prob"][0], df["theoretical_prob"][0]]

    plt.bar(categories, values)
    plt.ylabel("Probability")
    plt.title("Empirical vs. Theoretical Probability")
    plt.ylim(0, 1)
    plt.savefig("outputs/visualization.png")
    plt.show()

if __name__ == "__main__":
    plot_probabilities()
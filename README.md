# statistical-simulation-bertrands-ballot-theorem

# Project Overview

This project simulates and analyzes **Bertrand's Ballot Theorem**, a fundamental result in probability theory and combinatorial analysis. The theorem states:

If candidate A receives **p** votes and candidate B receives **q** votes (**p > q**), the probability that A is ahead throughout the entire counting process is given by:

$$P(A \text{ always ahead}) = \frac{p - q}{p + q}$$

### **Mathematical Proof**
To derive this formula, we employ combinatorial arguments and the concept of **lattice paths**.

#### **Step 1: Total Ways to Arrange Votes**
A total of **p + q** votes are cast, with **p** votes for A and **q** votes for B. The total number of ways to order these votes is given by the binomial coefficient:

$$\text{Total Arrangements} = \binom{p+q}{p} = \frac{(p+q)!}{p! q!}$$

Each arrangement represents a possible vote-counting sequence.

#### **Step 2: Lattice Path Representation**
Each sequence can be visualized as a lattice path in a **p × q** grid, where:
- A vote for **A** corresponds to a step **(+1, 0)** (rightward movement)
- A vote for **B** corresponds to a step **(0, +1)** (upward movement)

A valid vote sequence that satisfies Bertrand’s Ballot condition means the path **never crosses the diagonal** (i.e., A never falls behind B).

#### **Step 3: Counting Valid Paths (Reflection Principle)**
To count the number of valid paths where A is always ahead, we use a combinatorial approach called the **reflection principle**.

Define:
- **Valid paths** as those where A is never overtaken.
- **Invalid paths** as those where A is overtaken at least once.

The total number of vote arrangements is:

$$\binom{p+q}{p}$$

However, invalid paths can be mapped to valid paths by reflecting any path that first crosses the diagonal. The number of invalid paths can be computed using a shifted binomial coefficient:

$$\binom{p+q}{p-1}$$

Thus, the count of valid paths is:

$$\binom{p+q}{p} - \binom{p+q}{p-1}$$

Dividing by the total number of sequences gives:

$$P(A \text{ always ahead}) = \frac{\binom{p+q}{p} - \binom{p+q}{p-1}}{\binom{p+q}{p}} = \frac{p - q}{p + q}$$

This result holds for all **p > q** and has deep implications in electoral statistics, random walks, and stock market modeling.

---

# Folder Structure

```
project-root/
├── scripts/
│   ├── 01_generate_ballot_sequences.py   # Generates random vote sequences
│   ├── 02_check_always_ahead.py          # Checks if A is always ahead
│   ├── 03_run_simulations.py             # Runs multiple simulations
│   ├── 04_analyze_results.py             # Computes empirical probability
│   ├── 05_visualize_results.py           # Plots results
│   ├── utils.py                           # Helper functions
├── outputs/
│   ├── ballot_sequences.csv              # Stored random vote sequences
│   ├── simulation_results.csv            # Outcome of always-ahead checks
│   ├── probability_comparison.csv        # Comparison of empirical vs. theoretical probability
│   ├── visualization.png                  # Bar chart comparing probabilities
├── requirements.txt                        # Dependencies
├── README.md                               # Documentation
```

---

# Usage

### **1. Setup the Project:**
Clone the repository.
Ensure you have Python installed.
Install required dependencies using the requirements.txt file.

```sh
pip install -r requirements.txt
```

### **2. Generate Random Ballot Sequences**
This script generates `N` random sequences for given values of `p` and `q`.

```sh
python scripts/01_generate_ballot_sequences.py --p 100 --q 80 --n 10000
```

### **3. Check if A is Always Ahead**
Processes the generated sequences and determines if A remains ahead throughout.

```sh
python scripts/02_check_always_ahead.py
```

### **4. Run Simulations and Compute Empirical Probability**
Calculates the proportion of cases where A is always ahead and compares it with theory.

```sh
python scripts/03_run_simulations.py
```

### **5. Visualize Results**
Creates a bar chart comparing empirical vs. theoretical probabilities.

```sh
python scripts/04_visualize_results.py
```

---

# Requirements

- Python 3.8+
- Pandas
- Matplotlib

To install dependencies, run:

```sh
pip install -r requirements.txt
```
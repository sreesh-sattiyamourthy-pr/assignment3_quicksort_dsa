# Assignment 3: Understanding Algorithm Efficiency and Scalability

This project implements and compares two algorithms: **Randomized Quicksort** and **Deterministic Quicksort**, along with a performance analysis across various input types. The aim is to evaluate algorithm efficiency and scalability under different data conditions.

---

## Repository Structure

```
.
├── randomized_quicksort.py         # Contains both quicksort variants and timing tests
├── hash_table_chaining.py          # Hash table using chaining
├── analysis_report.md              # heoretical and empirical analysis 
└── README.md                       # This file
```

---

## How to Run the Code

### Requirements
- Python 3.x (Tested with Python 3.10+)
- No external dependencies required

### Running the Quicksort Comparison

To test the performance of **Randomized** and **Deterministic** Quicksort algorithms:

```bash
python randomized_quicksort.py
```

You will see output similar to this:

```
Size:  1000, Type: random   , Randomized: 0.00403s, Deterministic: 0.00113s
Size:  5000, Type: sorted   , Randomized: 0.01124s, Deterministic: 0.88137s
...
```

---

##  Summary of Findings

### 🔎 Theoretical Analysis

- **Deterministic Quicksort** (pivot = first element) has average-case time complexity **O(n log n)** but suffers **O(n²)** in worst-case scenarios like sorted or reversed data.
- **Randomized Quicksort** chooses pivots uniformly at random, providing an **expected time complexity of O(n log n)** even on sorted input.

### Empirical Observations

- **Randomized Quicksort** showed consistently good performance across all data types and sizes.
- **Deterministic Quicksort** performed well only on random inputs but showed exponential slowdown on sorted and reversed inputs.
- With repeated elements, **Randomized Quicksort** slowed significantly due to inefficient partitioning.

### Key Performance Data

| Size   | Input Type   | Randomized Time | Deterministic Time |
|--------|--------------|-----------------|---------------------|
| 1000   | Sorted       | 0.00192s        | 0.02539s            |
| 5000   | Reversed     | 0.02067s        | 1.17862s            |
| 10000  | Repeated     | 2.21867s        | 0.95611s            |
| 20000  | Sorted       | 0.05060s        | 11.39018s           |

### 🏁 Conclusion

**Randomized Quicksort** is the preferred sorting algorithm for scalable, real-world applications where input patterns may vary or be unpredictable. It provides reliable performance and avoids the severe pitfalls of fixed-pivot strategies like those used in Deterministic Quicksort.

---


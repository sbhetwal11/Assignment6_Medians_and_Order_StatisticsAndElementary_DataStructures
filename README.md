# Assignment 6: Medians and Order Statistics & Elementary Data Structures

**Author:** Sagar Bhetwal  
**Course:** Algorithms and Data Structures (MSCS-532)  
**University:** University of the Cumberlands   

---

##  Overview

This assignment is divided into **two major parts**:

1. **Part 1 – Selection Algorithms (Order Statistics):**
   - Implements two algorithms to find the k-th smallest element in an unsorted array:
     - **Randomized Quickselect** (expected Θ(n) time)
     - **Deterministic Median-of-Medians (BFPRT)** (guaranteed O(n) time)
   - Includes both theoretical and empirical performance analysis.

2. **Part 2 – Elementary Data Structures:**
   - Implements basic data structures from scratch:
     - **DynamicArray**
     - **Matrix**
     - **ArrayStack**
     - **CircularArrayQueue**
     - **SinglyLinkedList**
   - Demonstrates time complexity, operational efficiency, and real-world relevance.

---

##  Folder Structure

```
Assignment6/
│
├── selection_algorithms.py   # Part 1: Order statistic algorithms + benchmark
├── elementary_ds.py          # Part 2: Data structures implementation + demos
├── Assignment6 Report  # Final APA-7 formatted report
├── README.md                 # This file
```

---

## How to Run

### **1. Run Selection Algorithms (Part 1)**

**Purpose:** To demonstrate the runtime difference between randomized and deterministic selection.

**Command:**
```bash
python selection_algorithms.py
```

**Expected Output:**
- First, it prints correctness verification for both algorithms.
- Then, it runs benchmarks for multiple dataset sizes and input patterns.


This shows **empirical linear-time behavior** and verifies that Randomized Quickselect consistently outperforms Deterministic Selection in practice.

---

### **2. Run Data Structures (Part 2)**

**Purpose:** To test and verify basic data structure operations.

**Command:**
```bash
python elementary_ds.py
```

**Expected Output:**
Console output verifying operations for all structures:

This verifies that each structure behaves as expected and matches theoretical time complexity.

---

## Demonstration

1. **Selection Algorithms:**
   - Show that both Randomized Quickselect and Median-of-Medians achieve *linear-time selection*.
   - Confirm through empirical testing that:
     - Randomized Quickselect is faster in practice.
     - Deterministic Median-of-Medians guarantees O(n) even for adversarial inputs.

2. **Elementary Data Structures:**
   - Illustrate how core structures like arrays, stacks, queues, and linked lists operate internally.
   - Show their asymptotic time complexities through real Python implementations.
   - Reinforce how these structures serve as building blocks for advanced algorithms.

---

##  Findings and Conclusions

- **Performance Observations:**
  - Randomized Quickselect completed median selection in less than half the time of the deterministic version for large datasets.
  - Both algorithms maintained near-linear growth in runtime as input size increased.

- **Algorithmic Insights:**
  - Deterministic selection ensures predictable O(n) performance, critical for real-time or safety-critical systems.
  - Randomized Quickselect’s smaller constant factor makes it ideal for general-purpose use.

- **Data Structure Behavior:**
  - Arrays offer fast access (O(1)) but slow insertion/deletion (O(n)).
  - Dynamic arrays and circular queues efficiently handle growth and wrapping.
  - Stacks and queues demonstrate core LIFO/FIFO principles.
  - Linked lists excel in dynamic memory contexts but lack direct indexing.

---

##  References

- Blum, M., Floyd, R. W., Pratt, V., Rivest, R. L., & Tarjan, R. E. (1973). *Time bounds for selection*. *Journal of Computer and System Sciences, 7*(4), 448–461.  
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press.

---

## Summary

This project successfully integrates **algorithmic theory**, **implementation**, and **empirical testing**.  
By combining order statistic algorithms and elementary data structures, it provides a holistic view of how efficiency, correctness, and design principles interact in real-world computing systems.

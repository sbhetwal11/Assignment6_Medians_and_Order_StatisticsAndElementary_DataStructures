# selection_algorithms.py
from __future__ import annotations
import random
from typing import List, Sequence, Callable, Any, Tuple
import time


def partition(arr: List[int], left: int, right: int, pivot_index: int) -> int:
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
    store = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            arr[store], arr[i] = arr[i], arr[store]
            store += 1
    arr[right], arr[store] = arr[store], arr[right]
    return store


def randomized_select(arr: List[int], k: int) -> int:
    """
    Randomized Quickselect: expected Θ(n) for distinct inputs.
    Returns the k-th smallest (0-indexed).
    """
    if not (0 <= k < len(arr)):
        raise IndexError("k out of range")

    def _select(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return arr[left]
        pivot_index = random.randint(left, right)
        pivot_index = partition(arr, left, right, pivot_index)
        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return _select(left, pivot_index - 1, k_smallest)
        else:
            return _select(pivot_index + 1, right, k_smallest)

    return _select(0, len(arr) - 1, k)


def _median_of_five(a: List[int], start: int, end: int) -> int:
    """
    Sorts up to five elements a[start:end] in place and returns the index of the median.
    (Lower median for even length, matching CLRS convention.)
    """
    sub = a[start:end]
    sub.sort()
    mid_val = sub[(len(sub) - 1) // 2]
    a[start:end] = sub
    for i in range(start, end):
        if a[i] == mid_val:
            return i
    return start  


def deterministic_select(arr: List[int], k: int) -> int:
    """
    Median-of-Medians (BFPRT) SELECT with worst-case O(n).
    Returns the k-th smallest (0-indexed).
    """
    if not (0 <= k < len(arr)):
        raise IndexError("k out of range")

    def _select(left: int, right: int, k_smallest: int) -> int:
        n = right - left + 1
        if n <= 5:
            slice_sorted = sorted(arr[left:right+1])
            return slice_sorted[k_smallest - left]

        # 1) group into 5s, find medians
        med_indices = []
        i = left
        while i <= right:
            j = min(i + 5, right + 1)
            m_idx = _median_of_five(arr, i, j)
            med_indices.append(m_idx)
            i += 5

        # 2) recursively find median of medians
        med_vals = [arr[idx] for idx in med_indices]
        # We need the index of median-of-medians value within original arr slice
        mom_val = deterministic_select(med_vals[:], (len(med_vals) - 1) // 2)
        mom_index = left
        while mom_index <= right and arr[mom_index] != mom_val:
            mom_index += 1
        if mom_index > right:
            mom_index = med_indices[(len(med_indices) - 1)//2]

        pivot_index = partition(arr, left, right, mom_index)

        if k_smallest == pivot_index:
            return arr[pivot_index]
        elif k_smallest < pivot_index:
            return _select(left, pivot_index - 1, k_smallest)
        else:
            return _select(pivot_index + 1, right, k_smallest)

    return _select(0, len(arr) - 1, k)


# ------------------ Empirical benchmarking ------------------

def generate_input(n: int, pattern: str = "random") -> List[int]:
    if pattern == "random":
        return random.sample(range(10*n), n)
    elif pattern == "sorted":
        return list(range(n))
    elif pattern == "reverse":
        return list(range(n, 0, -1))
    elif pattern == "dupes":
        return [random.randint(0, n//10 or 1) for _ in range(n)]
    else:
        raise ValueError("Unknown pattern")


def time_once(fn: Callable[[], Any]) -> float:
    t0 = time.perf_counter()
    fn()
    return time.perf_counter() - t0


def benchmark_selection(sizes=(10_000, 50_000, 100_000),
                        patterns=("random", "sorted", "reverse", "dupes"),
                        trials=3, percentile=0.5) -> List[Tuple[int, str, float, float]]:
    results = []
    for n in sizes:
        k = int(percentile * (n - 1))
        for pat in patterns:
            t_rand, t_det = 0.0, 0.0
            for _ in range(trials):
                A = generate_input(n, pat)
                B = A[:]  # for the other method

                t_rand += time_once(lambda: randomized_select(A, k))
                t_det += time_once(lambda: deterministic_select(B, k))
            results.append((n, pat, t_rand / trials, t_det / trials))
    return results


if __name__ == "__main__":
    # Small sanity check
    data = [7, 1, 9, 3, 5, 2, 4, 8, 6]
    for kth in range(len(data)):
        print(kth, randomized_select(data[:], kth), deterministic_select(data[:], kth))

    print("\nRunning benchmark... please wait.\n")

    results = benchmark_selection(
        sizes=[10000, 20000, 50000],       # you can adjust for quicker tests
        patterns=["random", "sorted", "reverse", "dupes"],
        trials=3
    )

    print(f"{'n':>8} {'pattern':>10} {'rand_time(s)':>15} {'det_time(s)':>15}")
    for n, pat, t_rand, t_det in results:
        print(f"{n:8} {pat:>10} {t_rand:15.5f} {t_det:15.5f}")
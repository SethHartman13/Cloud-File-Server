from time import perf_counter as counter


def main() -> None:
    """
    Iterates through the fibonacci sequence (40 numbers) 5 times through a very inefficient recursion. 
    This is to simulate a CPU heavy task.
    This is a loop version of fib.py
    """

    # Inefficient recursion
    def f(n): return 0 if n == 0 else 1 if n == 1 else f(n-1) + f(n-2)
    print([f(n) for n in range(40)])

# Runs main program
if __name__ == "__main__":
    main()
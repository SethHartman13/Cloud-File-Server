from time import perf_counter as stopwatch


def main() -> None:
    """
    Iterates through the fibonacci sequence (40 numbers) 1 time through a very inefficient recursion. 
    This is to simulate a CPU heavy task.
    """

    begin_time = stopwatch()

    # Inefficient recursion
    def f(n): return 0 if n == 0 else 1 if n == 1 else f(n-1) + f(n-2)
    print([f(n) for n in range(40)])
    print()

    total_time = "{:.2f}".format(stopwatch() - begin_time)
    print(f'Server execution time = {total_time} sec')


# Runs main program
if __name__ == "__main__":
    main()
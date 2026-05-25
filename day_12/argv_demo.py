"""Demo: see exactly what sys.argv contains."""
import sys
def show_argv() -> None:
    """Print sys.argv with each element labeled by its index."""

    print(f"Total elements:{len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f" sys.argv[{i}] = {arg!r}")

if __name__ == "__main__":
    show_argv
    sys.argv[0] = 'argv_demo.py'
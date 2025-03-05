# Import Packages
import multiprocessing as mp
import cProfile
from pstats import Stats
from pathlib import Path


def main():
    input_file = (
        "<input filename>" + ".toml"
    )  # Want to be able to run from VS code debugger
    # input_file = sys.argv[1]
    with cProfile.Profile() as profile:
        # Your code here
        pass

    with open("profiling_stats.txt", "w") as stream:
        stats = Stats(profile, stream=stream)
        stats.strip_dirs()
        stats.sort_stats("time")
        stats.dump_stats("profiling/" + Path(input_file).stem + ".prof_stats")
        stats.print_stats()


if __name__ == "__main__":
    mp.freeze_support()
    main()

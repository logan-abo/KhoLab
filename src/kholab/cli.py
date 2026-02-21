import argparse

from .Kauffman import compute_kauffman_bracket


def main(argv=None):
    parser = argparse.ArgumentParser(prog="kholab", description="KhoLab prototype CLI")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    args = parser.parse_args(argv)
    if args.version:
        from . import __version__
        print(__version__)
        return 0
    print("KhoLab prototype. Use --version.")


    compute_kauffman_bracket()


    return 0


if __name__ == "__main__":
    import sys
    raise SystemExit(main(sys.argv[1:]))

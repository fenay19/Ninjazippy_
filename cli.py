"""Command-line interface for NinjaZipPy."""

import argparse
import logging
from ninjazippy.core import create_7z, extract_7z, NinjaZipError  # absolute import

def _build_parser():
    parser = argparse.ArgumentParser(
        prog="ninjazippy",
        description="Create and extract .7z archives"
    )
    # Global verbose argument (can be parsed separately later)
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    sub = parser.add_subparsers(dest="cmd", required=True)

    # ZIP subcommand
    z = sub.add_parser("zip", help="Create a .7z archive")
    z.add_argument("archive", help="Destination archive (e.g. my.7z)")
    z.add_argument("paths", nargs="+", help="Files/folders to include")
    z.add_argument("-v", "--verbose", action="store_true", help=argparse.SUPPRESS)  # ignore duplicate

    # UNZIP subcommand
    u = sub.add_parser("unzip", help="Extract a .7z archive")
    u.add_argument("archive", help="Archive to extract")
    u.add_argument("-d", "--dest", default=".", help="Destination folder (default: current dir)")
    u.add_argument("-v", "--verbose", action="store_true", help=argparse.SUPPRESS)  # ignore duplicate

    return parser


def main(argv=None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    # Enable logging if either global or subcommand -v was provided
    verbose = getattr(args, "verbose", False)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(levelname)s: %(message)s"
    )

    try:
        if args.cmd == "zip":
            create_7z(args.archive, args.paths)
            logging.info("Created archive: %s", args.archive)
        elif args.cmd == "unzip":
            extract_7z(args.archive, getattr(args, "dest", "."))
            logging.info("Extracted archive: %s -> %s", args.archive, getattr(args, "dest", "."))
        return 0
    except NinjaZipError as e:
        logging.error("Operation failed: %s", e)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

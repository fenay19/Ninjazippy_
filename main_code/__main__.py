"""Allow running as: python -m ninjazippy"""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())

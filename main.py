#!/usr/bin/env python3
"""One-Line Roast entry for make.fun.

Writes a single original roast line (at most 200 characters) about a
gadget used every day to /output/entry.txt, where the sealed scorer
and the judge read it.
"""

import os

ROAST = "My phone autocorrects my tired 'ok' into a chirpy 'OK!', an excitement I have never once felt."


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars, must be 1-200"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

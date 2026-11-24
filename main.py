#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather forecast (at most 140 characters) for a
city that does not exist, to /output/entry.txt.

The line: Gloomburg, an invented city, where the rain falls upwards.
A bored commuter gets the forecast register bent just enough to smile:
umbrellas optional, buses on time, dry, confused, strangely cheerful.
"""

FORECAST = (
    "In Gloomburg, rain falls upwards today \u2014 umbrellas optional, "
    "buses on time, and commuters arriving dry, confused, and "
    "strangely cheerful."
)


import os


def output_path() -> str:
    """Where the forecast goes: /output/entry.txt, or
    $MAKEFUN_OUTPUT_DIR/entry.txt when that is set (local checks)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    text = FORECAST.strip()
    assert 1 <= len(text) <= 140, f"forecast is {len(text)} characters"
    assert "\n" not in text, "forecast must be a single line"
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

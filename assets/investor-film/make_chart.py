#!/usr/bin/env python3
"""Draw the annotated pitch chart for the investor-film case study.

A copy of the graph code in the film project's tools/prosody.py, with plain-English labels
added. It reuses that tool's measure() so the numbers match it exactly.

    python3 make_chart.py /path/to/investor-film out.png
"""
import sys
from pathlib import Path

PROJECT = Path(sys.argv[1]).resolve()
OUT = sys.argv[2]
sys.path.insert(0, str(PROJECT / "tools"))
import numpy as np
import prosody
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROWS = [  # label, file, seconds to measure, plain verdict
    ("The reference ad", "audio/reference/dollar-shave-club.wav", 75, "The target: wide swings, clear pauses"),
    ("Old voice", "audio/v2/01-flood.mp3", None, "Flat and rushed"),
    ("Run-on take", "audio/v5/act1-take-a.mp3", None, "Lively, but few long pauses"),
    ("Final take", "audio/v5/act1-take-e.mp3", None, "Moves like a real ad"),
]
INK, MUTED, RULE, BLUE, BAND, PAPER, BAR = "#141317", "#6A6862", "#DFDCD4", "#1F5FD0", "#1F5FD01A", "#F5F4F0", "#B9B5AB"
LONG = 0.6  # a pause longer than this counts as a long break between ideas
SPAN = 20   # seconds shown

plt.rcParams.update({"font.family": "Arial", "font.size": 14})
ref = prosody.reference()
fig, axs = plt.subplots(len(ROWS), 1, figsize=(10, 12.4), sharex=True, facecolor=PAPER)
fig.subplots_adjust(left=.035, right=.965, top=.775, bottom=.055, hspace=.66)

for ax, (name, rel, upto, verdict) in zip(axs, ROWS):
    m, ws, (tt, st) = prosody.measure(PROJECT / rel, upto)
    d = prosody.distance(m, ref)
    t0 = ws[0][0]
    ax.set_facecolor(PAPER)
    # pitch range band: the middle 80% of the pitch, the "melody" number
    lo, hi = np.nanpercentile(st, 10), np.nanpercentile(st, 90)
    ax.axhspan(lo, hi, color=BAND, lw=0)
    # talking bars along the bottom
    for a, b, _ in ws:
        ax.axvspan(a - t0, b - t0, ymin=0, ymax=.07, color=BAR, lw=0)
    # long pauses marked under the gap
    for (a0, a1, _), (b0, b1, _) in zip(ws, ws[1:]):
        g = b0 - a1
        mid = (a1 + b0) / 2 - t0
        if g > LONG and mid < SPAN:
            ax.plot(mid, -16.2, marker="^", ms=8, color=INK, clip_on=False)
    ax.plot(tt - t0, st, ".", ms=3.2, color=BLUE)
    ax.set_ylim(-14, 14); ax.set_xlim(0, SPAN); ax.set_yticks([]); ax.set_xticks(range(0, SPAN + 1, 5))
    ax.tick_params(colors=MUTED, length=0)
    for s in ax.spines.values(): s.set_visible(False)
    ax.text(0, 1.2, name, transform=ax.transAxes, fontsize=16, color=INK, weight="bold", va="bottom")
    ax.text(0, 1.04, verdict, transform=ax.transAxes, fontsize=14, color=BLUE, va="bottom")
    tail = "the target" if upto else f"distance {d:.2f}"
    ax.text(1, 1.04, f"pitch range {m['pitch_range']:.1f}  ·  long pauses {m['long_pause_share'] * 100:.0f}%  ·  {tail}",
            transform=ax.transAxes, ha="right", va="bottom", fontsize=12, color=MUTED)
    print(f"{name:20s} range {m['pitch_range']:.2f}  long {m['long_pause_share']:.3f}  distance {d:.2f}")

axs[-1].set_xlabel("seconds", color=MUTED, fontsize=13)
axs[-1].tick_params(axis="x", pad=18)

# key across the top, drawn with real marks so it matches the chart exactly
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle
fig.text(.035, .965, "How to read it", fontsize=16, weight="bold", color=INK, va="center")
def key(x, y, mark, text):
    fig.text(x + .035, y, text, color=INK, fontsize=13.5, va="center")
    if mark == "dot": fig.add_artist(Line2D([x + .012], [y], marker="o", ms=6, color=BLUE, transform=fig.transFigure))
    if mark == "tri": fig.add_artist(Line2D([x + .012], [y], marker="^", ms=9, color=INK, transform=fig.transFigure))
    if mark == "bar": fig.add_artist(Rectangle((x, y - .005), .026, .01, color=BAR, transform=fig.transFigure))
    if mark == "band": fig.add_artist(Rectangle((x, y - .009), .026, .018, color="#DCE4F3", transform=fig.transFigure))
key(.035, .925, "dot", "Pitch going up and down. Flat means robotic.")
key(.035, .893, "bar", "Talking. The gaps are pauses.")
key(.56, .893, "tri", "A long pause between ideas.")
key(.035, .861, "band", "Where most of the pitch sits. Wider means more expressive.")

plt.savefig(OUT, dpi=110, facecolor=PAPER)
print("chart:", OUT)

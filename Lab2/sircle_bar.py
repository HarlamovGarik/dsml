import numpy as np
import seaborn as sns


def get_label_rotation(angle, offset):
    rotation = np.rad2deg(angle + offset)
    if angle <= np.pi:
        alignment = "right"
        rotation = rotation + 180
    else:
        alignment = "left"
    return rotation, alignment


def add_labels(angles, values, labels, offset, ax):
    padding = 4

    for angle, value, label, in zip(angles, values, labels):
        angle = angle

        rotation, alignment = get_label_rotation(angle, offset)

        ax.text(
            x=angle,
            y=value + padding,
            s=label,
            ha=alignment,
            va="center",
            rotation=rotation,
            rotation_mode="anchor"
        )


def preparing_date(df):
    VALUES = df["BOROUGH"].values
    LABELS = df["BUILDING CLASS CATEGORY"].values

    PAD = 3
    ANGLES_N = len(VALUES) + PAD * len(np.unique(df.values))
    ANGLES = np.linspace(0, 2 * np.pi, num=ANGLES_N, endpoint=False)
    WIDTH = (2 * np.pi) / len(ANGLES)
    OFFSET = np.pi / 2
    offset = 0
    IDXS = []

    GROUPS_SIZE = [10, 20, 12, 8]
    for size in GROUPS_SIZE:
        IDXS += list(range(offset + PAD, offset + size + PAD))
        offset += size + PAD

    # Same layout as above
    fig, ax = plt.subplots(figsize=(20, 10), subplot_kw={"projection": "polar"})

    ax.set_theta_offset(OFFSET)
    ax.set_ylim(-100, 100)
    ax.set_frame_on(False)
    ax.xaxis.grid(False)
    ax.yaxis.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])

    COLORS = [f"C{i}" for i, size in enumerate(GROUPS_SIZE) for _ in range(size)]
    ax.bar(
        ANGLES[IDXS], VALUES, width=WIDTH, color=COLORS,
        edgecolor="white", linewidth=2
    )
    add_labels(ANGLES[IDXS], VALUES, LABELS, OFFSET, ax)
#!/usr/bin/env python3

import argparse
import itertools

import matplotlib.pyplot as plt
from matplotlib.patches import Arc

from recaman import recaman


# https://stackoverflow.com/questions/5434891/iterate-a-list-as-pair-current-next-in-python
def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def plot(xs):
    max_x = max(xs)

    plt.figure(figsize=(7, 7))
    plt.axis([0, max_x, -max_x / 2, max_x / 2])
    ax = plt.gca()  # get current axes

    for i, (a, b) in enumerate(pairwise(xs)):
        center = (a + b) / 2.0
        y = 0
        diameter = abs(b - a)
        start = 0.0 if i % 2 else 180.0
        end = 180.0 if i % 2 else 360.0

        arc = Arc((center, y), diameter, diameter, theta1=start, theta2=end, edgecolor='k')
        ax.add_patch(arc)

    plt.show()


def run(args):
    visual = args.visual
    xs = list(itertools.islice(recaman(), args.iterations))
    if visual:
        plot(xs)
    else:
        for x in xs:
            print(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("iterations", type=int)
    parser.add_argument("-v", "--visual", action="store_true")
    run(parser.parse_args())

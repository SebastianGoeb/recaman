#!/usr/bin/env python3

import argparse
from recaman import recaman


def run(args):
    for x in recaman(int(args.iterations)):
        print(x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("iterations")
    run(parser.parse_args())

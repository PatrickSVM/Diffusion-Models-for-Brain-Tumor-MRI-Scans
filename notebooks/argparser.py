# Small experiment with argparser

import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--hallo", default=10, type=int)

args = parser.parse_args()
print(args.hallo)
import argparse
import os.path
import sys

def runit(args=None,globals=None,**kwargs):
    parser = argparse.ArgumentParser(prog=os.path.basename(__file__))

    required = parser.add_argument_group("Required Script Arguments")
    required.add_argument("--sa1", help="first launcher arg", required=True)
    required.add_argument("--sa2", help="first launcher arg", required=True)
    required.add_argument("--sa3", help="first launcher arg", required=True)

    optional = parser.add_argument_group("Optional Script Arguments")
    optional.add_argument("--sa4", help="first launcher arg")
    optional.add_argument("--sa5", help="first launcher arg")
    optional.add_argument("--sa6", help="first launcher arg")

    args = parser.parse_args(args)
    print("\n\n**Test is running!**\n\n")
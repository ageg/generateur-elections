#!/usr/bin/env python3
from yaml import safe_load
from argparse import ArgumentParser

import ageg
import finissante

def merge(source, destination):
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination


parser = ArgumentParser()
parser.add_argument("type", choices=["ageg", "finissante"])
parser.add_argument("-c", "--config", action="append")
parser.add_argument("-D", "--define", action="append")
args = parser.parse_args()

configuration = {}

for filename in args.config:
    with open(filename, "r") as f:
        configuration = merge(safe_load(f), configuration)

for key in args.define:
    splits = key.split("=")
    path = splits[0].split(".")
    node = configuration
    for path_segment in path[:-1]:
        if path_segment not in node:
            node[path_segment] = {}

        node = node[path_segment]

    node[path[-1]] = splits[1]

if args.type == "ageg":
    ageg.generer_questionnaire(configuration)


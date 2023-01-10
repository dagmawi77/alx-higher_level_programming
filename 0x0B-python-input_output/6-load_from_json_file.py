#!/usr/bin/python3

"""Defines function."""
import json


def load_from_json_file(filename):
    """Create JSON file."""
    with open(filename) as f:
        return json.load(f)

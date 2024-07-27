#!/usr/bin/env python

import json
import sys

DEFAULTS = """
{
}
"""

class Config:
    def __init__(self, filepath="config.json"):
        with open(filepath, 'r') as f:
            self.config = json.load(f)

    def get(self, key_path):
        keys = key_path.split('/')
        try:
            value = self.config
            for key in keys:
                value = value[key]
        except KeyError:
            try:
                value = DEFAULTS
                for key in keys:
                    value = value[key]
            except:
                value = None

        return value

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python -m config <key_path>")
        sys.exit(1)

    key_path = sys.argv[2-1]

    value = Config().get(key_path)
    if value is not None:
        print(value)
        exit(0)
    else:
        exit(1)


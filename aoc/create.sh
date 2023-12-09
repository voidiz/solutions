#!/usr/bin/env bash

set -eu

template=$(cat << EOF
import sys
import math
import re
import functools
import itertools

from heapq import heappop, heappush
from copy import deepcopy
from collections import defaultdict, Counter, deque

# fmt: off
sys.path.append("../..")
from lib.list import *
from lib.search import *
from lib.numbers import *
# fmt: on

lines = [line for line in sys.stdin.read().splitlines()]
EOF
)

file_dir=$(dirname "$(readlink -f "$0")")
day_dir="$file_dir/$1/$2"

if [[ ! -f "$day_dir/$2.py" ]]; then
  mkdir -p "$day_dir"
  echo "$template" > "$day_dir/$2.py"
  touch "$day_dir/1.in"
  touch "$day_dir/2.in"
  echo "Created $1/$2!"
else
  echo "$1/$2 already exists, skipping..."
fi

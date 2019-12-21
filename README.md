![Actions Status](https://github.com/skmatz/apog/workflows/python-package/badge.svg)

# APOG

Argparse Logger for Python

## Installation

```sh
pip install git+https://github.com/skmatz/apog.git
```

## Usage

```python
import argparse
from apog import Apog

parser = argparse.ArgumentParser()
parser.add_argument("--xxx")
parser.add_argument("--yyy")
parser.add_argument("--zzz")
args = parser.parse_args()

apog = Apog(path="apog.csv")
apog.write(args)
```

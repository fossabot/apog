[![Actions Status](https://github.com/skmatz/apog/workflows/python-package/badge.svg)](https://github.com/skmatz/apog/actions?query=workflow%3Apython-package)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fapog.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fapog?ref=badge_shield)

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


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fskmatz%2Fapog.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fskmatz%2Fapog?ref=badge_large)
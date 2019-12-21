import argparse
import os.path as osp
from datetime import datetime as dt

import pandas as pd


class Apog:
    def __init__(self, path: str):
        self._path = path
        self._df = pd.read_csv(path) if osp.exists(path) else pd.DataFrame()

    def write(self, args: argparse.Namespace, fmt=r"%Y%m%d-%H%M%S"):
        if not isinstance(args, argparse.Namespace):
            raise TypeError("Argument args must be type argparse.Namespace.")

        args = vars(args)  # type: ignore
        series = pd.Series({"date": dt.now().strftime(fmt), **args})
        self._df = self._df.append(series, ignore_index=True)

        self._df.to_csv(self._path, index=False)
        print("Args saved to {}.".format(self._path))

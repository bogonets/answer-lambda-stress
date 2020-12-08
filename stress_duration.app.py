# -*- coding: utf-8 -*-

import numpy as np
import time

duration = 1.0


def on_set(key, val):
    if key == 'duration':
        global duration
        duration = float(val)


def on_get(key):
    if key == 'duration':
        return duration


def on_run(source: np.ndarray):
    begin = time.time()
    while time.time() - begin < duration:
        pass
    return { 'result': source }


if __name__ == '__main__':
    pass

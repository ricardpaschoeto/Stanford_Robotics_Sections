#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 20:58:16 2020

@author: paschoeto
"""

import numpy as np
from scipy.optimize import fmin

print("{}".format(np.sin(np.pi/3)))

def func(x):
    p = x**2 + 2*x + 1
    return p

fmin(func,np.array([2,3]))
#!/usr/bin/env python3
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
# ---

"""
config.py

UNSW ZZEN9444 Neural Networks and Deep Learning

This file deteremines which device PyTorch will utilise.
You may change the variable device if you wish.
"""

import torch

# Use a GPU if available, as it should be faster.
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

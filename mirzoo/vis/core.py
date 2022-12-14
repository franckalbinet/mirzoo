# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_vis.core.ipynb.

# %% auto 0
__all__ = ['PRIMARY_COLOR', 'ACCENT_COLOR', 'DEFAULT_STYLE', 'centimeter', 'set_style', 'plot_spectra', 'plot_validation_curve',
           'plot_learning_curve', 'plot_capacity']

# %% ../nbs/03_vis.core.ipynb 3
#nbdev_comment from __future__ import annotations
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from matplotlib import ticker
from fastcore.test import *

from ..data.loading import get_spectra

# %% ../nbs/03_vis.core.ipynb 5
PRIMARY_COLOR = '#333'
ACCENT_COLOR = 'firebrick'
DEFAULT_STYLE = {
    'axes.linewidth': 0.5,
    'axes.facecolor': 'white',
    'axes.ymargin': 0.11,
    'font.size': 8,
    
    'axes.spines.bottom': True,
    'axes.spines.left': False,
    'axes.spines.right': False,
    'axes.spines.top': False,
    'axes.grid': True,
    
    'grid.color': 'black',
    'grid.linewidth': 0.2,
    'grid.linestyle': '-',

    'xtick.bottom': True,
    'xtick.top': False,
    'xtick.direction': 'out',
    'xtick.major.size': 5,
    'xtick.major.width': 1,
    'xtick.minor.size': 3,
    'xtick.minor.width': 0.5,
    'xtick.minor.visible': True,
        
    'ytick.left': True,
    'ytick.right': False, 
    'ytick.direction': 'in',
    'ytick.major.size': 5,
    'ytick.major.width': 1,
    'ytick.minor.size': 3,
    'ytick.minor.width': 0.5,
    'ytick.minor.visible': True
}

centimeter = 1/2.54  # centimeters in inches

# %% ../nbs/03_vis.core.ipynb 6
def set_style(style:dict # Dictionary of plt.rcParams
             ):
    for k, v in style.items():
        plt.rcParams[k] = v 

# %% ../nbs/03_vis.core.ipynb 8
def plot_spectra(X:np.ndarray, # Spectra (n_samples, n_wavenumbers)
                 X_names:np.ndarray, # Wavenumbers (n_wavenumbers)
                 ylabel:str='Absorbance', # y axis label
                 figsize=(18, 5), # Wavenumbers
                 sample=20): # Size of random subset
    """Plot Mid-infrared spectra"""
    fig, ax = plt.subplots(figsize=figsize)
    idx = np.random.randint(X.shape[0], size=sample)
    ax.set_xlim(np.max(X_names), np.min(X_names))
    ax.set(xlabel='Wavenumber', ylabel=ylabel)
    ax.set_axisbelow(True)
    ax.grid(True, which='both')
    _ = ax.plot(X_names, X[idx, :].T)

# %% ../nbs/03_vis.core.ipynb 14
def plot_validation_curve(x, losses, ax=None, plot_kwargs={}, fill_between_kwargs={}):
    Y = np.mean(np.array(losses), axis=0)
    SD = np.std(np.array(losses), axis=0) 
    ax.fill_between(x, Y + SD, Y - SD, **fill_between_kwargs)
    ax.plot(x, Y, **plot_kwargs) 
    return(ax)

# %% ../nbs/03_vis.core.ipynb 16
def plot_learning_curve(x, losses_train, losses_valid, ax=None,  train_kwargs={}, valid_kwargs={}):
    if ax is None:
        ax = plt.gca()
    ax.plot(x, losses_train, label='Training', **train_kwargs) 
    ax.plot(x, losses_valid, label='Validation', **valid_kwargs) 
    ax.set_yscale('log')
    ax.set_xscale('log')
    return(ax)

# %% ../nbs/03_vis.core.ipynb 17
def plot_capacity(x, capacity, ax=None, **kwargs):
    if ax is None:
            ax = plt.gca()
    ax.bar(x, capacity, width=0.15*np.array(x), color=PRIMARY_COLOR, zorder=99, **kwargs)
    ax.set_yscale('log')
    ax.set_xscale('log')
    # ax.spines.bottom.set_visible(True) 
    return(ax)

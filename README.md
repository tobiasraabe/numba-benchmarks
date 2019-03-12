Numba Benchmarks
================

[![Updates](https://pyup.io/repos/github/tobiasraabe/numba-benchmarks/shield.svg)](https://pyup.io/repos/github/tobiasraabe/numba-benchmarks/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tobiasraabe/numba-benchmarks/master)

This repository contains benchmarks for code examples optimized with Numba. All
results can be reproduced online in a Binder notebook.

> The objective is solely speed.
>
> ...
>
> Who said readibility? No, that is not what this is about!

Examples
--------

- [Array initilization](array-initialization.ipynb)
- [Solving linear least squares](linear-least-squares.ipynb)

Helper Functions
----------------

These functions are replacements or convenience wrappers for Numpy functions
which are currently not supported by Numba.

- [np.clip](numpy-replacements/clip.py): Will be implemented in
  https://github.com/numba/numba/pull/3468.
- [np.count_nonzero](numpy-replacements/count-nonzero.py)
- [np.triu_indices, np.tril_indices, tri_n,
  tri_n_with_diag](numpy-replacements/triangle.py)

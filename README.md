Numba Benchmarks
================

[![Updates](https://pyup.io/repos/github/tobiasraabe/numba-benchmarks/shield.svg)](https://pyup.io/repos/github/tobiasraabe/numba-benchmarks/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tobiasraabe/numba-benchmarks/master)

This repository contains benchmarks for code examples optimized with Numba. All
results can be reproduced online in a Binder notebook.

The objectives are prioritized in the following order:

1. Speed
.
.
.
n. Readibility

Examples
--------

- [Array initilization](array-initialization.ipynb)
- [Solving linear least squares](linear-least-squares.ipynb)

Helper Functions
----------------

These functions are replacements or convenience wrapper for Numpy functions
which are currently not supported by Numba.

- [np.clip](numpy-replacements/clip.py): Will be fixed in
  https://github.com/numba/numba/pull/3468.
- [np.count_nonzero](numpy-replacements/count-nonzero.py)
- [np.triu_indices, tril_indices, tri_n,
  tri_n_with_diag](numpy-replacements/triangle-indexing.py)
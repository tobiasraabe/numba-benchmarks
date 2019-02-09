import numpy as np
from numba import njit


@njit
def triu_indices(n, k=0, m=None):
    """Replacement for np.triu_indices as long it is not supported by Numba.

    Mirrors functionality from
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.triu_indices.html.

    Examples
    --------
    >>> import numpy as np
    >>> assert np.allclose(triu_indices(2), np.triu_indices(2))

    """
    if k != 0:
        raise NotImplementedError("Diagonal offset is not implemented.")

    if m is None:
        m = n

    num_elements_in_triangle = tri_n_with_diag(n)
    rows = np.zeros(num_elements_in_triangle, dtype=np.int8)
    cols = np.zeros(num_elements_in_triangle, dtype=np.int8)

    i = 0
    for row in range(n):
        for col in range(m):
            if row <= col:
                rows[i], cols[i] = row, col
                i += 1
            else:
                continue

    return rows, cols


@njit
def tril_indices(n, k=0, m=None):
    """Replacement for np.triu_indices as long it is not supported by Numba.

    Mirrors functionality from
    https://docs.scipy.org/doc/numpy/reference/generated/numpy.triu_indices.html.

    Examples
    --------
    >>> import numpy as np
    >>> assert np.allclose(tril_indices(2), np.tril_indices(2))

    """
    if k != 0:
        raise NotImplementedError("Diagonal offset is not implemented.")

    if m is None:
        m = n

    num_elements_in_triangle = tri_n_with_diag(n)
    rows = np.zeros(num_elements_in_triangle, dtype=np.int8)
    cols = np.zeros(num_elements_in_triangle, dtype=np.int8)

    i = 0
    for row in range(n):
        for col in range(m):
            if col <= row:
                rows[i], cols[i] = row, col
                i += 1
            else:
                continue

    return rows, cols


@njit
def tri_n(n):
    """Number of elements in matrix triangle."""
    return n * (n - 1) // 2


@njit
def tri_n_with_diag(n):
    """Number of elements in matrix triangle + diagonal."""
    return tri_n(n) + n

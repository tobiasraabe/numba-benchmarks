import numpy as np
from numba import njit


@njit
def diagonal(a):
    """Extracts diagonal from matrix or transforms array to square matrix.

    Parameters
    ----------
    a : np.array
        Matrix

    Returns
    -------
    np.array
        Array containing elements of the diagonal.

    Example
    -------
    >>> import numpy as np
    >>> a = np.arange(16).reshape(4, 4)
    >>> assert np.allclose(diagonal(a), np.diagonal(a))

    """
    if a.ndim > 1:

        dim = a.shape[0]

        out = np.empty(dim)

        for i in range(dim):
            out[i] = a[i, i]

    else:

        out = np.identity(a.shape[0]) * a

    return out

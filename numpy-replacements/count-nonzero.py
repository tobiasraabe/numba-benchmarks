import numpy as np
from numba import njit


@njit
def count_nonzero(a):
    """Return number of non-zero elements.

    Parameters
    ----------
    a : np.array

    Returns
    -------
    int
        Number of non-zero elements.

    Example
    -------
    >>> import numpy as np
    >>> a = np.arange(-8, 8).reshape(4, 4)
    >>> np.allclose(count_nonzero(a), np.count_nonzero(a))

    TODO: Is this class really necessary? Convenience function.

    """
    return np.sum(0 < a)

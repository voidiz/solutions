"""
list.py:
    Common functions for manipulating lists

    Supports Python 3.7+ for PyPy 7.3.4+ support
"""

# Use typing.List etc. since list as a generic type isn't supported
# until Python 3.9
from typing import Any, Union, TypeVar, List, Tuple


MatrixRow = TypeVar("MatrixRow", str, List[Any], Tuple[Any, ...])


def transpose(
    lst: Union[List[MatrixRow], Tuple[MatrixRow, ...]]
) -> List[List[Any]]:
    """
    Transpose a rectangular 2d list/tuple. Individual elements are not copied.
    Strings are also treated as rows.
    """

    if not lst:
        return []

    assert all(len(row) == len(lst[0]) for row in lst) and "Not rectangular"

    if not lst[0]:
        return [[]]

    return [
        [lst[row][col] for row in range(len(lst))]
        for col in range(len(lst[0]))
    ]


def flatten(lst: List[Any]) -> List[Any]:
    """
    Flatten an arbitrarily nested list. Individual elements are not copied.
    """

    result = []
    for item in lst:
        if isinstance(item, list):
            result += flatten(item)
        else:
            result.append(item)

    return result


def replace(lst: List[Any], old: Union[int, float, str, bool], new) -> None:
    """
    Inline replace all occurrences of old with new in an arbitrarily nested
    list. old should be a primitive.
    """

    for i, item in enumerate(lst):
        if isinstance(item, List):
            replace(item, old, new)
            continue

        if item == old:
            lst[i] = new


def rotate(lst: List[Any], deg: int) -> List[Any]:
    """
    Rotate a rectangular 2d list/tuple `deg` degrees CW. Individual elements
    are not copied. Strings are also treated as rows.

    Not optimal since it just calls `rotate90` repeatedly.
    """

    if deg == 0:
        return lst

    return rotate(rotate90(lst), deg - 90)


def rotate90(lst: List[Any]) -> List[Any]:
    """
    Rotate a rectangular 2d list/tuple 90 degrees CW. Individual elements are
    not copied. Strings are also treated as rows.
    """

    return list([list(row) for row in zip(*lst[::-1])])

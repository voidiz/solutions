from typing import TypeVar, Callable

T = TypeVar("T")


def binary_search(
    seq: Callable[[int], T],
    low: int,
    high: int,
    target_cmp: Callable[[T], int],
) -> tuple[int, int, int]:
    """
    Search through the sorted sequence `seq` defined by a function that takes
    the index of an element in the sequence. Return the first index of the
    target element based on target_cmp.

    If target_cmp(mid) is
    - negative: search below mid
    - positive: search above mid
    - 0: the goal is found, return the index, index of last <= goal and
      index of last >= goal

    If the goal wasn't found, return -1, index of last <= goal and index
    of last >= goal.
    """

    if low > high:
        return -1, high, low

    mid = (low + high) // 2

    cmp_result = target_cmp(seq(mid))

    if cmp_result > 0:
        return binary_search(seq, mid + 1, high, target_cmp)

    if cmp_result < 0:
        return binary_search(seq, low, mid - 1, target_cmp)

    return mid, low, high

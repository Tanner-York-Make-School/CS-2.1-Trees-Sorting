#!python
import random
import statistics
from sorting_iterative import insertion_sort


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def compare(item1, item2, order):
    # Determin if item1 is greater than or less that items2 based on the order
    if order == 'ascend':
        if item1 > item2:
            return False
    elif order == 'descend':
        if item1 < item2:
            return False
    return True


def merge(items1, items2, order='ascend'):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    Running time: O(n+m) because we have to iterate over every item in both
        list when merging them together.
    Memory usage: O(m+n) because we are creating a new array the size of both
        inputs combined"""
    merged_items = []
    i, j = 0, 0
    while i < len(items1) and j < len(items2):
        if compare(items1[i], items2[j], order):
            merged_items.append(items1[i])
            i += 1
        else:
            merged_items.append(items2[j])
            j += 1
    merged_items.extend(items1[i:] if i < len(items1) else items2[j:])
    return merged_items


def split_sort_merge(items, order='ascend'):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    Running time: O(n^2) because we are using another sorting algorithm to sort
        the two lists and that algorithms time complexity is O(n^2) therfore 
        making this algorithms time complexity the same as long as their are 
        not worse operations outside of the sorting algorithm.
    Memory usage: O(n) because we are creating a new list from the input using
        the merge function."""
    mid = len(items)//2
    left, right = insertion_sort(
        items[:mid]), insertion_sort(items[mid:], order)
    return merge(left, right)


def merge_sort(items, order='ascend'):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    Running time: O(nlog(n)) because as the algorithm runs we still have to
        iterate over every item but as we iterate the lists we are spliting 
        are getting smaller by a factor of two.
    Memory usage: O(n) beacuse as the algorithm runs it creates new arrays
        thats memory adds to be the length of the input array."""
    if len(items) < 2:
        return items
    mid = len(items)//2
    left, right = merge_sort(
        items[:mid], order), merge_sort(items[mid:], order)
    return merge(left, right, order)


def partition(items, low, high, order='ascend'):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot with median of 3 random elements from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    Running time: O(n) beacuse we only iterate over the range once and swap
        the elements in O(1) time complexity
    Memory usage: O(1) because the algorithms is swapping in place."""
    # Choose a pivot any way and document your method in docstring above
    # pivot_index = random.randint(0, len(items)-1)

    # Set the pivot index to the median of 3 random elements
    p_index = statistics.median(random.choices(range(low, high), k=3))
    pivot = items[p_index]

    # Move pivot to the end of list for partitioning (not needed if p_index is high)
    swap(items, high, p_index)
    last_small_index = low - 1

    # Loop through all items in range [low...high-1]
    for i in range(low, high):
        # items[i] < pivot, when order equals ascend
        if compare(items[i], pivot, order):
            # Move current item into range [low..last_small_index]
            last_small_index += 1
            swap(items, last_small_index, i)
        # items greater than pivot are in the range of [last_small_index+1...i]
    # Move pivot item into final position [p] and return index p
    swap(items, last_small_index + 1, high)
    return last_small_index + 1


def quick_sort(items, order='ascend', low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    Best case running time: O(nlog(n)) under the condition that the pivot is
        the median of the list because it creates a balanced binary tree 
        iteration of the list.
    Worst case running time: O(n^2) under the condition that the pivot is the
        largest or smallest element in the list because it creates an
        unbalanced binary tree iteration of the list
    Memory usage: O(nlog(n)) because as it recusivly runs through the items
        there can be (at best) nlog(n) callbacks open at one time."""
    # Check if high and low range bounds have default values (not given)
    if low is None and high is None:
        low, high = 0, len(items) - 1
    # Check if list or range is so small it's already sorted (base case)
    if low < high:
        # Partition items in-place around a pivot and get index of pivot
        pivot_index = partition(items, low, high, order)
        # Sort each sublist range by recursively calling quick sort
        quick_sort(items, order, low, pivot_index-1)
        quick_sort(items, order, pivot_index+1, high)
    return items

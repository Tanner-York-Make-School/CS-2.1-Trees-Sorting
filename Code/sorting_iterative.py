#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) becuase no matter what we have to go through
        every item to check if it is in the correct order.
    Memory usage: 0(1) becuase the function only creates a few ponters and
        not a new array based on the input array, which would make it O(n)
        if it did."""
    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    Running time: O(n^2) under the conditions that the list is in reverse
        order or not already sorted because of the worst case of have having to 
        swap all the items in the list for each item in the list.
    Memory usage: O(1) because the algorithm sorts the array already in memory
        preventing creating a new array from the input array."""
    swapped = True
    last_unsorted_index = len(items)
    while swapped:
        swapped = False
        for i in range(last_unsorted_index-1):
            if items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swapped = True
        last_unsorted_index -= 1
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: O(n^2) because for evey item in the list the algorithm checks
        every other item in the list.
    Memory usage: O(1) because the algorithm sorts the array already in memory
        preventing creating a new array from the input array."""
    unsorted_index = 0
    while unsorted_index < len(items):
        lowest = unsorted_index
        for i in range(unsorted_index, len(items)):
            if items[lowest] > items[i]:
                lowest = i
        items[unsorted_index], items[lowest] = items[lowest], items[unsorted_index]
        unsorted_index += 1


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because under the worst case conditions we have to
        go over every item per each item in the list.
    Memory usage: O(1) because we are swaping values in the input array rather
        than creating a new array."""
    unsoted_index = 1
    while unsoted_index < len(items):
        unsorted_index = unsoted_index
        while unsorted_index > 0 and items[unsorted_index-1] > items[unsorted_index]:
            items[unsorted_index], items[unsorted_index -
                                         1] = items[unsorted_index-1], items[unsorted_index]
            unsorted_index = unsorted_index-1
        unsoted_index += 1
    return items


def binary_insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: O(n^2) because under the worst case conditions we have to
        go over every item per each item in the list.
    Memory usage: O(1) because we are swaping values in the input array rather
        than creating a new array."""
    def binary_search(items, low, high, target):
        if low == high:
            return low
        mid = (low + high) // 2
        if target > items[mid]:
            return binary_search(items, mid + 1, high, target)
        elif target < items[mid]:
            return binary_search(items, low, mid, target)
        return mid

    for index in range(len(items)):
        insert_index = binary_search(items, 0, index, items[index])
        if insert_index < index:
            temp = items[index]
            unsorted_index = index-1
            while unsorted_index >= insert_index:
                items[unsorted_index + 1] = items[unsorted_index]
                unsorted_index -= 1
            items[insert_index] = temp
    return items

#!python

from sorting import random_ints
from sorting_iterative import is_sorted, bubble_sort, selection_sort, insertion_sort, binary_insertion_sort
from sorting_recursive import split_sort_merge, merge_sort, quick_sort, partition
from sorting_integer import counting_sort, bucket_sort
import unittest


class IsSortedTest(unittest.TestCase):

    def test_is_sorted_on_sorted_integers(self):
        # Positive test cases (examples) with lists of sorted integers
        assert is_sorted([]) is True  # Empty lists are vacuously sorted
        assert is_sorted([3]) is True  # Single item is trivially sorted
        assert is_sorted([3, 3]) is True  # Duplicate items are in order
        assert is_sorted([3, 5]) is True
        assert is_sorted([3, 5, 7]) is True
        assert is_sorted([-4, -3, -2, -1, 0, 1]) is True
        assert is_sorted([1, 0, -1, -2, -3, -4], 'descend') is True

    def test_is_sorted_on_unsorted_integers(self):
        # Negative test cases (counterexamples) with lists of unsorted integers
        assert is_sorted([5, 3]) is False
        assert is_sorted([3, 5, 3]) is False
        assert is_sorted([7, 5, 3]) is False
        assert is_sorted([-4, -3, -2, 0, -1]) is False
        assert is_sorted([-4, -3, -2, -1, 0, 1], 'descend') is False

    def test_is_sorted_on_sorted_strings(self):
        # Positive test cases (examples) with lists of sorted strings
        assert is_sorted(['A']) is True  # Single item is trivially sorted
        assert is_sorted(['A', 'A']) is True  # Duplicate items are in order
        assert is_sorted(['A', 'B']) is True
        assert is_sorted(['A', 'B', 'C']) is True
        assert is_sorted(['Bats', 'Bit', 'Boat']) is True
        assert is_sorted(['Boat', 'Bit', 'Bats'], 'descend') is True

    def test_is_sorted_on_unsorted_strings(self):
        # Negative test cases (counterexamples) with lists of unsorted strings
        assert is_sorted(['B', 'A']) is False
        assert is_sorted(['A', 'B', 'A']) is False
        assert is_sorted(['C', 'B', 'A']) is False
        assert is_sorted(['Cats', 'Apples', 'Bats']) is False
        assert is_sorted(['Bats', 'Bit', 'Boat'], 'descend') is False

    def test_is_sorted_on_sorted_tuples(self):
        # Positive test cases (examples) with lists of sorted tuples
        assert is_sorted([(3, 5)]) is True  # Single item
        assert is_sorted([(3, 'A')]) is True  # Single item
        assert is_sorted([('A', 3)]) is True  # Single item
        assert is_sorted([('A', 'B')]) is True  # Single item
        assert is_sorted([(3, 5), (3, 5)]) is True  # Duplicate items
        assert is_sorted([(3, 'A'), (3, 'A')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('A', 3)]) is True  # Duplicate items
        assert is_sorted([('A', 'B'), ('A', 'B')]) is True  # Duplicate items
        assert is_sorted([('A', 3), ('B', 5)]) is True  # Both items sorted
        assert is_sorted([('A', 3), ('B', 3)]) is True  # First item sorted
        assert is_sorted([('A', 3), ('A', 5)]) is True  # Second item sorted
        assert is_sorted([(3, 'A'), (5, 'B')]) is True  # Both items sorted
        assert is_sorted([(3, 'A'), (5, 'A')]) is True  # First item sorted
        assert is_sorted([(3, 'A'), (3, 'B')]) is True  # Second item sorted
        assert is_sorted([(2.0, 'A'), (3.1, 'B')]) is True
        assert is_sorted([('A', 'A'), ('B', 'B')]) is True
        assert is_sorted([('A', 'B'), ('C', 'D')]) is True
        assert is_sorted([('C', 'D'), ('A', 'B')], 'descend') is True

    def test_is_sorted_on_unsorted_tuples(self):
        # Negative test cases (counterexamples) with lists of unsorted tuples
        assert is_sorted([(5, 'B'), (3, 'A')]) is False  # Both items unsorted
        assert is_sorted([(5, 'A'), (3, 'B')]) is False  # First item unsorted
        assert is_sorted([(3, 'B'), (3, 'A')]) is False  # Second item unsorted
        assert is_sorted([('B', 5), ('A', 3)]) is False  # Both items unsorted
        assert is_sorted([('B', 3), ('A', 5)]) is False  # First item unsorted
        assert is_sorted([('A', 5), ('A', 3)]) is False  # Second item unsorted
        assert is_sorted([(3.1, 'B'), (2.0, 'A')]) is False
        assert is_sorted([('B', 'B'), ('A', 'A')]) is False
        assert is_sorted([('C', 'D'), ('A', 'B')]) is False
        assert is_sorted([('A', 'B'), ('C', 'D')], 'descend') is False


# class PartitionTest(unittest.TestCase):

#     def test_partiation_on_list_of_integers(self):
#         items = [100, 300, 250, 5, 6]

#         p_index = partition(items, 0, 0)
#         assert p_index == 0

#         p_index = partition(items, 0, 1)
#         assert p_index == 1

#         p_index = partition(items, 0, 4)
#         assert p_index == 1

#     def test_partition_on_list_of_strings(self):
#         items = ['A', 'C', 'D', 'B']

#         p_index = partition(items, 0, 0)
#         assert p_index == 0

#         p_index = partition(items, 0, 2)
#         assert p_index == 2


class IntegerSortTest(unittest.TestCase):

    def test_sort_on_empty_list(self):
        items = []
        items = sort(items)
        assert items == []  # List should not be changed

    def test_sort_on_small_lists_of_integers(self):
        items1 = [3]
        items1 = sort(items1)
        assert items1 == [3]  # List should not be changed
        items2 = [5, 3]
        items2 = sort(items2)
        assert items2 == [3, 5]  # List should be in sorted order
        items3 = [5, 7, 3]
        items3 = sort(items3)
        assert items3 == [3, 5, 7]
        items4 = [100, 300, 250, 5]
        items4 = sort(items4)
        assert items4 == [5, 100, 250, 300]
        items5 = [5, 7, 3]
        items5 = sort(items5, 'descend')
        assert items5 == [7, 5, 3]

    def test_sort_on_small_lists_of_integers_with_duplicates(self):
        items1 = [3, 3]
        items1 = sort(items1)
        assert items1 == [3, 3]  # List should not be changed
        items2 = [3, 5, 3]
        items2 = sort(items2)
        assert items2 == [3, 3, 5]  # List should be in sorted order
        items3 = [5, 5, 3, 5, 3]
        items3 = sort(items3)
        assert items3 == [3, 3, 5, 5, 5]
        items4 = [7, 5, 3, 7, 5, 7, 5, 3, 7]
        items4 = sort(items4)
        assert items4 == [3, 3, 5, 5, 5, 7, 7, 7, 7]
        items5 = [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
        items5 = sort(items5)
        assert items5 == [2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4]
        items3 = [5, 5, 3, 5, 3]
        items3 = sort(items3, 'descend')
        assert items3 == [5, 5, 5, 3, 3]

    def test_sort_on_lists_of_random_integers(self):
        # Generate list of 10 random integers from range [1...20]
        items1 = random_ints(10, 1, 20)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        # Call a sort function to sort list items in place
        items1 = sort(items1)
        assert items1 == sorted_items1

        # Generate list of 20 random integers from range [1...50]
        items2 = random_ints(20, 1, 50)
        sorted_items2 = sorted(items2)  # Copy
        items2 = sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 30 random integers from range [1...100]
        items3 = random_ints(30, 1, 100)
        sorted_items3 = sorted(items3)  # Copy
        items3 = sort(items3)  # Mutate
        assert items3 == sorted_items3

        # Generate list of 30 random integers from range [1...100]
        items4 = random_ints(30, 1, 100)
        sorted_items4 = sorted(items4, reverse=True)  # Copy
        items4 = sort(items4, 'descend')  # Mutate
        assert items4 == sorted_items4

    def test_sort_on_lists_of_random_integers_with_duplicates(self):
        # Generate list of 20 random integers from range [1...10]
        items1 = random_ints(20, 1, 10)
        sorted_items1 = sorted(items1)  # Create a copy of list in sorted order
        # Call a sort function to sort list items in place
        items1 = sort(items1)
        assert items1 == sorted_items1

        # Generate list of 50 random integers from range [1...20]
        items2 = random_ints(50, 1, 20)
        sorted_items2 = sorted(items2)  # Copy
        items2 = sort(items2)  # Mutate
        assert items2 == sorted_items2

        # Generate list of 100 random integers from range [1...30]
        items3 = random_ints(100, 1, 30)
        sorted_items3 = sorted(items3)  # Copy
        items3 = sort(items3)  # Mutate
        assert items3 == sorted_items3

        # Generate list of 100 random integers from range [1...30]
        items4 = random_ints(100, 1, 30)
        sorted_items4 = sorted(items4, reverse=True)  # Copy
        items3 = sort(items4, 'descend')  # Mutate
        assert items3 == sorted_items4


class StringSortTest(unittest.TestCase):

    def test_sort_on_small_lists_of_strings(self):
        items1 = ['A']
        items1 = sort(items1)
        assert items1 == ['A']  # List should not be changed
        items2 = ['B', 'A']
        items2 = sort(items2)
        assert items2 == ['A', 'B']  # List should be in sorted order
        items3 = ['B', 'C', 'A']
        items3 = sort(items3)
        assert items3 == ['A', 'B', 'C']
        items4 = ['A', 'C', 'A', 'B']
        items4 = sort(items4)
        assert items4 == ['A', 'A', 'B', 'C']
        items5 = ['A', 'C', 'A', 'B']
        items5 = sort(items5, 'descend')
        assert items5 == ['C', 'B', 'A', 'A']

    def test_sort_on_fish_book_title(self):
        items = 'one fish two fish red fish blue fish'.split()
        sorted_items = sorted(items)  # Create a copy of list in sorted order
        # Call a sort function to sort list items in place
        items = sort(items)
        assert items == sorted_items

        items2 = 'one fish two fish red fish blue fish'.split()
        # Create a copy of list in sorted order
        sorted_items2 = sorted(items2, reverse=True)
        # Call a sort function to sort list items in place
        items2 = sort(items2, 'descend')
        assert items2 == sorted_items2

    def test_sort_on_seven_dwarf_names(self):
        items = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items = sorted(items)  # Copy
        items = sort(items)  # Mutate
        assert items == sorted_items

        items2 = 'Doc Grumpy Happy Sleepy Bashful Sneezy Dopey'.split()
        sorted_items2 = sorted(items2, reverse=True)  # Copy
        items2 = sort(items2, 'descend')  # Mutate
        assert items2 == sorted_items2


def get_sort_function():
    """Read command-line argument and return sort function with that name."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort_function'.format(script))
        print('Example: {} bubble_sort'.format(script))
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
            return sort_function
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if 'sort' in name:
                    print('    {}'.format(name))
            return


# If using PyTest, change this variable to the sort function you want to test
sort = quick_sort


if __name__ == '__main__':
    # Get sort function from command-line argument
    # FIXME: This is causing unittest to throw an error
    # sort = get_sort_function()
    unittest.main()

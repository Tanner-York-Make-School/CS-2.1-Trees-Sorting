#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    Running time: O(n+range) where range is the differece between the 
        minimum and maximum values in the list because we are nut just iterating
        over all the elements in the list but also the range.
    Memory usage: O(n) where we are creating a new place in memory for each
        element in the list. (could be improved if we used an inplace movement
        instead of the output list)"""
    if len(numbers) == 0:
        return numbers
    # Find range of given numbers (minimum and maximum integer values)
    numbers_range = max(numbers) - min(numbers) + 1
    # Create an offest to save space on the length of the counts array
    offset = min(numbers)
    # Create list of counts with a slot for each number in input range
    counts = [0 for _ in range(numbers_range)]
    # Loop over given numbers and increment each number's count
    for num in numbers:
        counts[num - offset] += 1
    # Loop over counts and append that many numbers into output list
    # TODO: Improve this to mutate input instead of creating new output list
    output = []
    for index, value in enumerate(counts):
        for _ in range(value):
            output.append(index + offset)
    return output


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O(n) under the consition that the numbers in the array are
        uniformly distributed into the buckets because even though we are
        using another sorting algorithm, we are on average not performing it
        on a list of length n but some fraction of n.
    Memory usage: O(n) because as we but the elemnents in buckest we are adding
        a new space in memory for each element."""
    # Create list of buckets to store numbers in subranges of input range
    buckets = [[] for _ in range(num_buckets + 1)]
    # Loop over given numbers and place each item in appropriate bucket
    maximum = max(numbers)
    for num in numbers:
        bucket_index = num * num_buckets // maximum
        buckets[bucket_index].append(num)
    # Sort each bucket using any sorting algorithm (recursive or another)
    for index, bucket in enumerate(buckets):
        buckets[index] = counting_sort(bucket)
    # Loop over buckets and append each bucket's numbers into output list
    count = 0
    for bucket in buckets:
        for value in bucket:
            numbers[count] = value
            count += 1
    return numbers

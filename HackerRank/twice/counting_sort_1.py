"""
Comparison Sorting:
Quicksort usually has a running time of nlog(n), but is there an algorithm that can sort even faster?
In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing
the elements to one another. A comparison sort algorithm cannot beat nlog(n) (worst-case) running time, since nlog(n)
represents the minimum number of comparisons needed to know where to place each element.

Alternative Sorting:
Another sorting method, the counting sort, does not require comparison. Instead, you create an integer array whose
index range covers the entire range of values in your array to sort. Each time a value occurs in the original array,
you increment the counter at that index. At the end, run through your counting array, printing the value of each
non-zero valued index that number of times.
"""


def alternate_sorting(arr: list) -> list:
    """
    This function takes as an input an array of integers and sorts it out.

    Example:
        (1) arr = [1, 1, 3, 2, 1]
            alternate_sorting(arr) => [1, 1, 1, 2, 3]
            Method: All the values in arr are in the range [0...3], so create an array of zeros,
            freq = [0, 0, 0, 0] with length max(arr) + 1. The frequency array then becomes freq = [0, 3, 1, 1].
            These values can be used to create the sorted array as well: sorted = [1, 1, 1, 2, 3].
    """

    # initiating the frequency list
    freq = []
    for _ in range(max(arr)+1):
        freq.append(0)

    # counting each element and storing it in the frequency list
    for i in range(len(arr)):
        # first the elements that appear multiple times, avoiding double counting
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                k = arr[i]
                freq[k] = freq[k] + 1
        # last the unique elements
        for j in range(i, len(arr)):
            k = arr[j]
            if freq[k] == 0:
                freq[k] = freq[k] + 1
    # print(freq)

    # sorting out the list by using the frequency list
    sorted_arr = []
    for i in range(len(freq)):
        if freq[i] > 1:
            for j in range(freq[i]):
                sorted_arr.append(i)
        elif freq[i] > 0:
            sorted_arr.append(i)
    return sorted_arr


# ----------------- TESTS -----------------

arr1 = [1, 1, 3, 2, 1]
print(alternate_sorting(arr1))
# Expected Output: [1, 1, 1, 2, 3]

arr2 = [63, 25, 73, 1, 98, 73, 56, 84, 86, 57, 16, 83, 8, 25, 81, 56, 9, 53, 98, 67, 99, 12, 83, 89, 80, 91, 39, 86, 76, 85, 74, 39, 25, 90, 59, 10, 94, 32, 44, 3, 89, 30, 27, 79, 46, 96, 27, 32, 18, 21, 92, 69, 81, 40, 40, 34, 68, 78, 24, 87, 42, 69, 23, 41, 78, 22, 6, 90, 99, 89, 50, 30, 20, 1, 43, 3, 70, 95, 33, 46, 44, 9, 69, 48, 33, 60, 65, 16, 82, 67, 61, 32, 21, 79, 75, 75, 13, 87, 70, 33]
print(alternate_sorting(arr2))
# Expected freq Output:
# [0, 2, 0, 2, 0, 0, 1, 0, 1, 2, 1, 0, 1, 1, 0, 0, 2, 0, 1, 0, 1, 2, 1, 1, 1, 3, 0, 2, 0, 0, 2, 0, 3, 3, 1, 0, 0, 0, 0, 2, 2, 1, 1, 1, 2, 0, 2, 0, 1, 0, 1, 0, 0, 1, 0, 0, 2, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 2, 1, 3, 2, 0, 0, 2, 1, 2, 1, 0, 2, 2, 1, 2, 1, 2, 1, 1, 2, 2, 0, 3, 2, 1, 1, 0, 1, 1, 1, 0, 2, 2, ],
# Expected Output:
# [1, 1, 3, 3, 6, 8, 9, 9, 10, 12, 13, 16, 16, 18, 20, 21, 21, 22, 23, 24, 25, 25, 25, 25, 27, 27, 30, 30, 32, 32, 32, 32, 33, 33, 33, 33, 34, 39, 39, 40, 40, 41, 42, 43, 44, 44, 46, 46, 48, 50, 53, 56, 56, 57, 59, 60, 61, 63, 65, 67, 67, 68, 69, 69, 69, 69, 70, 70, 73, 73, 74, 75, 75, 76, 78, 78, 79, 79, 80, 81, 81, 82, 83, 83, 84, 85, 86, 86, 87, 87, 89, 89, 89, 89, 90, 90, 91, 92, 94, 95, 96, 98, 98, 99, 99]

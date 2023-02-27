"""
There is a collection of rocks where each rock has various minerals embedded in it. Each type of mineral is designated
by a lowercase letter in the range ascii[a-z]. There may be multiple occurrences of a mineral in a rock. A mineral is
called a gemstone if it occurs at least once in each of the rocks in the collection.

Given a list of minerals embedded in each of the rocks, display the number of types of gemstones in the collection.
"""


def gemstones(arr: list) -> int:
    """
    This function takes as an input an array of strings and returns an integer representing the number of characters
    occurring in all the strings inside the provided array.

    Example:
        (1) arr = ['abc', 'abc', 'bc']
            gemstones(arr) => 2
    """

    gems = 0
    gems_dic = {}
    gems_arr = []
    minerals = []
    for stone in arr:
        temp = []
        for i in range(len(stone)):
            temp.append(stone[i])
            minerals.append(stone[i])
        temp_set = set(temp)
        temp_arr = []
        for item in temp_set:
            temp_arr.append(item)
        gems_arr.append(temp_arr)
    gems_set = set(minerals)
    for item in gems_set:
        gems_dic[item] = 0
    for i in range(len(gems_arr)):
        for mineral in gems_arr[i]:
            gems_dic[mineral] = gems_dic[mineral] + 1
    for g in gems_dic.keys():
        if gems_dic[g] == len(arr):
            gems = gems + 1
    return gems


# ----------------- TESTS -----------------

arr_1 = ['abc', 'abc', 'bc']
print(gemstones(arr_1))
# Expected Output: 2

arr_2 = ['abcdde', 'baccd', 'eeabg']
print(gemstones(arr_2))
# Expected Output: 2

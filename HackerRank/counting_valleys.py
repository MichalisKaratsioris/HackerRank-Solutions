"""
An avid hiker keeps meticulous records of their hikes. During the last hike that took exactly "steps" steps, for
every step it was noted if it was an uphill, U, or a downhill, D step. Hikes always start and end at sea level,
and each step up or down represents a "1" unit change in altitude. We define the following terms:
    - A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and
        ending with a step-down to sea level.
    - A valley is a sequence of consecutive steps below sea level, starting with a step-down from sea level and
        ending with a step-up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""


def counting_valleys(path: list) -> int:
    """
    This function takes as an input a list of characters denoting the path,
    and returns an integer representing the number of valleys.

    Example:
        (1) path = [DDUUUUDD]
            return 1
        (2) path = [UDDDUDUU]
            return 1
    """

    valleys = 0
    level = 0
    for direction in path:
        if direction == 'D' and level == 0:
            valleys = valleys + 1
            level = level - 1
        elif direction == 'U':
            level = level + 1
        else:
            level = level - 1
    return valleys


# ----------------- TESTS -----------------

path_1 = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']
print(counting_valleys(path_1))
# Expected Output: 1

path_2 = ['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
print(counting_valleys(path_2))
# Expected Output: 1

path_3 = ['D', 'D', 'U', 'U', 'U', 'U', 'D', 'D', 'D', 'D', 'U', 'U', 'U', 'U', 'D', 'D']
print(counting_valleys(path_3))
# Expected Output: 2

path_4 = ['U', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'U', 'U', 'D', 'U', 'D', 'D', 'U', 'D', 'U', 'U', 'U', 'D', 'D', 'D', 'U']
print(counting_valleys(path_4))
# Expected Output: 6

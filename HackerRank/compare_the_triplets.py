"""
Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale
from 1 to 100 for three categories: problem clarity, originality, and difficulty. The rating for Alice's challenge is
the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]). The task
is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].

    - If a[i] > b[i], then Alice is awarded 1 point.
    - If a[i] < b[i], then Bob is awarded 1 point.
    - If a[i] = b[i], then neither person receives a point.

Comparison points is the total points a person earned. Given a and b, determine their respective comparison points.
"""


def compare_the_triplets(a: list, b: list) -> list:
    """
    This function takes as an input two lists of integers, a and b, and returns a list of length 2 with integers which
    represent the total points Alice and Bob finally got.

    Example:
        (1) a = [1, 2, 3]
            b = [3, 2, 1]
            compare_the_triplets(a, b) => [1, 1]
    """

    score = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            score[0] = score[0] + 1
        elif a[i] < b[i]:
            score[1] = score[1] + 1
    return score


# ----------------- TESTS -----------------

a_1 = [1, 2, 3]
b_1 = [3, 2, 1]
print(compare_the_triplets(a_1, b_1))
# Expected Output: [1, 1]

a_2 = [5, 6, 7]
b_2 = [3, 6, 10]
print(compare_the_triplets(a_2, b_2))
# Expected Output: [1, 1]

a_3 = [17, 28, 30]
b_3 = [99, 16, 8]
print(compare_the_triplets(a_3, b_3))
# Expected Output: [2, 1]

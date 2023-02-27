"""
Louise joined a social networking site to stay in touch with her friends. The signup page required her to input a
name and a password. However, the password must be strong. The website considers a password to be strong if it
satisfies the following criteria:

    - Its length is at least .
    - It contains at least one digit.
    - It contains at least one lowercase English character.
    - It contains at least one uppercase English character.
    - It contains at least one special character. The special characters are: !@#$%^&*()-+

She typed a random string of length n in the password field but wasn't sure if it was strong. Given the string she
typed, can you find the minimum number of characters she must add to make her password strong?

Note: Here's the set of types of characters in a form you can paste in your solution:
    - numbers = "0123456789"
    - lower_case = "abcdefghijklmnopqrstuvwxyz"
    - upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    - special_characters = "!@#$%^&*()-+"
"""


def strong_password(password: str) -> int:
    """
    This function takes as an input
    and returns

    Example:
        (1) password = "2bbbb" (missing upper case and special character)
            strong_password(password) => 2
    """

    checks = [0, 0, 0, 0, 0]
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    if len(password) < 6:
        checks[0] = checks[0] + abs(len(password) - 6)
    for i in range(len(password)):
        if not password[i] in numbers:
            checks[1] = checks[1] + 1
        if not password[i] in lower_case:
            checks[2] = checks[2] + 1
        if not password[i] in upper_case:
            checks[3] = checks[3] + 1
        if not password[i] in special_characters:
            checks[4] = checks[4] + 1
    for i in range(1, 5):
        if checks[i] == len(password):
            checks[i] = 1
        else:
            checks[i] = 0
    if checks[0] <= sum(checks[1:]):
        return sum(checks[1:])
    return checks[0]


# ----------------- TESTS -----------------

password_1 = "2bbbb"
print(strong_password(password_1))
# Expected Output: 2

password_2 = "2bb#A"
print(strong_password(password_2))
# Expected Output: 1

password_3 = "Ab1"
print(strong_password(password_3))
# Expected Output: 3

password_4 = "#HackerRank"
print(strong_password(password_4))
# Expected Output: 1

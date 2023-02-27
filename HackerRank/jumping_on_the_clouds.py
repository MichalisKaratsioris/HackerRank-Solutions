"""
There is a new mobile game that starts with consecutively numbered clouds. Some clouds are thunderheads and
others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the
current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will
take to jump from the starting position to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.
"""


def jumping_on_the_clouds(clouds: list) -> int:
    """
    This function takes as an input a list of 0s and 1s, and returns an integer representing the minimum jumps needed,
    starting from the first index of the list to arrive in the last, by avoiding the 1s.

    Example:
        (1) clouds = [0, 1, 0, 0, 0, 1, 0]
            jumping_on_the_clouds(clouds) => 3 because 0(index 0) -> 0(index 2) -> 0(index 4) -> 0(index 6)
    """

    cloud = 0
    jumps = 0
    while cloud != (len(clouds) - 1):
        if clouds[cloud + 2] == 1:
            cloud = cloud + 1
            jumps = jumps + 1
        else:
            cloud = cloud + 2
            jumps = jumps + 1
    return jumps


# ----------------- TESTS -----------------

clouds_1 = [0, 1, 0, 0, 0, 1, 0]
print(jumping_on_the_clouds(clouds_1))
# Expected Output: 3

clouds_2 = [0, 0, 1, 0, 0, 1, 0]
print(jumping_on_the_clouds(clouds_2))
# Expected Output: 4

clouds_3 = [0, 0, 0, 0, 1, 0]
print(jumping_on_the_clouds(clouds_3))
# Expected Output: 3

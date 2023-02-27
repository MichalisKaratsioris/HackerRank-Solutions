"""
    Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
    Note:
        - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
        - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
    """


def time_conversion(s: str) -> str:
    """
    This function takes as an input a string s which denotes the time in 12-hour format and
    converts it into 24-hour format.

    Examples:
        (1) s_1 = '12:01:00PM'
            time_conversion(s_1) => '12:01:00'
        (2) s_2 = '12:01:00AM'
            time_conversion(s_2) => '00:01:00'
        (3) s_3 = '07:05:45PM'
            time_conversion(s_3) => '19:05:45'
    """

    time_in = s.split(":")
    if time_in[-1][-2] == 'A':
        time_in[-1] = time_in[-1][0:2]
        if int(time_in[0]) == 12:
            time_in[0] = '00'
    if time_in[-1][-2] == 'P':
        time_in[-1] = time_in[-1][0:2]
        if int(time_in[0]) < 12:
            time_in[0] = int(time_in[0]) + 12
    return f"{time_in[0]}:{time_in[1]}:{time_in[-1]}"


# ----------------- TESTS -----------------

print(time_conversion('12:01:00PM'))
# Expected Output: '12:01:00'

print(time_conversion('12:01:00AM'))
# Expected Output: '00:01:00'

print(time_conversion('05:38:45PM'))
# Expected Output: '17:38:45'

print(time_conversion('05:29:39AM'))
# Expected Output: '05:29:39'

print(time_conversion('07:05:45PM'))
# Expected Output: '19:05:45'

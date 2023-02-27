"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note:   - 12:00:00AM on a 12-hour clock, is 00:00:00 on a 24-hour clock.
        - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example:    s = '12:01:00PM'
            Return '12:01:00'

            s = '12:01:00AM'
            Return '00:01:00'

Function Description: Complete the timeConversion function in the editor below. 
It should return a new string representing the input time in 24 hour format.
        timeConversion has the following parameter(s):
            string s: a time in 12 hour format
        Returns:
            string: the time in 24 hour format

Input Format: A single string s that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

Constraints: All input times are valid

Sample Input: s = '07:05:45PM'

Sample Output: 19:05:45
"""

def timeConversion(s: str) -> str:
    s_temp = s[:-2]
    if s[-2:] == 'PM':
        if s[:2] == '12':
            return s_temp
        return f"{int(s_temp[:2]) + 12}{s_temp[2:]}"
    elif s[:2] == '12':
        return f"00{s_temp[2:]}"
    return s_temp


time = '07:05:45PM'
print(timeConversion(time))
# Output: 19:05:45

time = '12:01:00PM'
print(timeConversion(time))
# Output: 12:01:00

time = '12:01:00AM'
print(timeConversion(time))
# Output: 00:01:00

time = '01:01:00AM'
print(timeConversion(time))
# Output: 01:01:00

time = '05:01:00PM'
print(timeConversion(time))
# Output: 17:01:00

time = '07:01:00AM'
print(timeConversion(time))
# Output: 07:01:00

time = '07:05:45PM'
print(timeConversion(time))
# Output: 19:05:45

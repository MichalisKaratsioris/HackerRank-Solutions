"""
Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his
handwriting. He found a magazine and wants to know if he can cut out whole words from it and use them to create an
untraceable replica of his ransom note. The words in his note are case-sensitive, and he must use only whole words
available in the magazine. He cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note
exactly using whole words from the magazine; otherwise, print No.
"""


def ransom_note(magazine: str, note: str) -> str:
    """
    This function takes as an input two strings, magazine and note, and returns a string: "Yes" or "No",
    depending on if it is possible to reconstruct the note-string from words inside the magazine-string.

    Example:
        (1) magazine = "attack at dawn"
            note = "Attack at dawn"
            ransom_note(magazine, note) => No
    """

    mag_arr = magazine.split(" ")
    note_arr = note.split(" ")
    mag_set = set(mag_arr)
    note_set = set(note_arr)
    mag_dic = {}
    note_dic = {}
    for item in mag_set:
        mag_dic[item] = 0
    for item in note_set:
        note_dic[item] = 0
    for item in note_arr:
        note_dic[item] = note_dic[item] + 1
    for item in mag_arr:
        mag_dic[item] = mag_dic[item] + 1
    # print(mag_dic)
    # print(note_dic)
    for item in note_dic.keys():
        for word in mag_dic.keys():
            if item == word and note_dic[item] != 0:
                note_dic[item] = note_dic[item] - 1
    sum_f = 0
    for item in note_dic.keys():
        sum_f = sum_f + note_dic[item]
    if sum_f == 0:
        return "Yes"
    return "No"


# ----------------- TESTS -----------------

magazine_1 = "attack at dawn"
note_1 = "Attack at dawn"
print(ransom_note(magazine_1, note_1))
# Expected Output: No

magazine_2 = "give me one grand today night"
note_2 = "give one grand today"
print(ransom_note(magazine_2, note_2))
# Expected Output: Yes

magazine_3 = "two times three is not four"
note_3 = "two times two is four"
print(ransom_note(magazine_3, note_3))
# Expected Output: No

magazine_4 = "ive got a lovely bunch of coconuts"
note_4 = "ive got some coconuts"
print(ransom_note(magazine_4, note_4))
# Expected Output: No

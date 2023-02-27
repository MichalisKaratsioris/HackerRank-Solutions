"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each
letter by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of
the alphabet. In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
"""


def caesar_cipher(s: str, k: int) -> str:
    """
    This function takes as an input a string s and an integer k, and returns a string which is encrypted using Caesar's
    cipher.

    Example:
        (1) s = 'There's-a-starman-waiting-in-the-sky'
            k = 3
            caesar_cipher(s, k) => Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb
    """

    # add a check to k so that to create if needed the appropriate alphabet

    alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz-'"
    cipher = ''
    for letter in s:
        # print(letter)
        if letter == alphabet[-1]:
            cipher = cipher + alphabet[-1]
        elif letter == alphabet[-2]:
            cipher = cipher + alphabet[-2]
        else:
            if letter.islower():
                index = alphabet.index(letter) + k
                cipher = cipher + alphabet[index]
            else:
                index = alphabet.index(letter.lower()) + k
                cipher = cipher + alphabet[index].upper()
    return cipher


# ----------------- TESTS -----------------

s_1 = "There's-a-starman-waiting-in-the-sky"
k_1 = 3
print(caesar_cipher(s_1, k_1))
# Expected Output: Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb

s_2 = "middle-Outz"
k_2 = 2
print(caesar_cipher(s_2, k_2))
# Expected Output: okffng-Qwvb

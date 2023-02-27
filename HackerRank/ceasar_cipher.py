"""
Julius Caesar protected his confidential information by encrypting it using a cipher. Caesar's cipher shifts each letter 
by a number of letters. If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example: s = 'There's-a-starman-waiting-in-the-sky', k = 3. The alphabet is rotated by 3, matching the mapping above. 
The encrypted string is 'Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb'.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Function Description Complete the caesarCipher function in the editor below, which has the following parameter(s):

        string s: cleartext
        int k: the alphabet rotation factor
    Returns:
        string: the encrypted string

Constraints:
    1 <= n <= 100
    0 <= k <= 100
    s is a valid ASCII string without any spaces.

Sample Input: s = 'middle-Outz', k = 2

Sample Output: 'okffng-Qwvb'

Explanation:
    Original alphabet:      abcdefghijklmnopqrstuvwxyz
    Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

    m -> o
    i -> k
    d -> f
    d -> f
    l -> n
    e -> g
    - -> -
    O -> Q
    u -> w
    t -> v
    z -> b
"""

def caesarCipher(s: str, k: int) -> str:
    ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if k == len(ab):
        return s
    cipher = []
    for ch in s:
        cipher.append(ch)
    for i, ch in enumerate(cipher):
        if ch.lower() not in ab:
            continue
        if ch.isupper():
            position = ab.index(ch.lower())
            cipher_position = position + k
            if cipher_position >= len(ab):
                cipher_position %= len(ab)
            cipher[i] = ab[cipher_position].upper()
        else:
            position = ab.index(ch)
            cipher_position = position + k
            if cipher_position >= len(ab):
                cipher_position %= len(ab)
            cipher[i] = ab[cipher_position]
    return "".join(cipher)

    
message = "middle-Outz"
k = 2
print(caesarCipher(message, k))
# Output: okffng-Qwvb

message = "There's-a-starman-waiting-in-the-sky"
k = 3
print(caesarCipher(message, k))
# Output: Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb

message = "Always-Look-on-the-Bright-Side-of-Life"
k = 5
print(caesarCipher(message, k))
# Output: Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj

message = "Hello_World!"
k = 4
print(caesarCipher(message, k))
# Output: Lipps_Asvph!



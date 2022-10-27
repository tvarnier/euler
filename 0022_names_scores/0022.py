"""
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

def alphabetic_value(str):
    value = 0
    for c in str.upper():
        value += ord(c) - ord('A') + 1
    return value

if __name__ == '__main__':
    text_file = open("names.txt", "r")
    s = text_file.read()
    text_file.close()

    name_array = s.translate({ord(c): None for c in '"'}).upper().split(",")
    name_array.sort()

    res = 0
    for position, name in enumerate(name_array):
        res += alphabetic_value(name) * (position + 1)

    print(res)
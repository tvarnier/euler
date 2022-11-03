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
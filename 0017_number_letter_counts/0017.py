if __name__ == '__main__':
    num2word = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
                6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}

    count_letters = 0
    for nbr in range(1, 1000):
        str = ""
        if nbr // 100 > 0:
            str += num2word[nbr // 100] + "hundred"
            if nbr % 100 > 0:
                str += "and"
        if nbr % 100 > 0:
            if nbr % 100 >= 20:
                str += num2word[nbr % 100 // 10 * 10]
            if nbr % 100 >= 10 and nbr % 100 < 20:
                str += num2word[nbr % 100]
            elif nbr % 10 > 0:
                str += num2word[nbr % 10]
        print(nbr, " = ", str)
        count_letters += len(str)
    count_letters += len("OneThousand")
    print(count_letters)
    
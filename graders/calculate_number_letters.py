
def cal_number_letters(data):
    digit_count = 0
    letter_count = 0
    for char in data:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            letter_count += 1
    return "LETTERS {}\nDIGITS {}".format(letter_count, digit_count)
data = input()
result = cal_number_letters(data)
print(result)
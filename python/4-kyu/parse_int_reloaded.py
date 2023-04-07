def translate_number(number_string):
    if number_string == "one":
        return 1
    elif number_string == "two":
        return 2
    elif number_string == "three":
        return 3
    elif number_string == "four":
        return 4
    elif number_string == "five":
        return 5
    elif number_string == "six":
        return 6
    elif number_string == "seven":
        return 7
    elif number_string == "eight":
        return 8
    elif number_string == "nine":
        return 9
    elif number_string == "ten":
        return 10
    elif number_string == "eleven":
        return 11
    elif number_string == "twelve":
        return 12
    elif number_string == "thirteen":
        return 13
    elif number_string == "fourteen":
        return 14
    elif number_string == "fifteen":
        return 15
    elif number_string == "sixteen":
        return 16
    elif number_string == "seventeen":
        return 17
    elif number_string == "eighteen":
        return 18
    elif number_string == "nineteen":
        return 19
    elif number_string == "twenty":
        return 20
    elif number_string == "thirty":
        return 30
    elif number_string == "forty":
        return 40
    elif number_string == "fifty":
        return 50
    elif number_string == "sixty":
        return 60
    elif number_string == "seventy":
        return 70
    elif number_string == "eighty":
        return 80
    elif number_string == "ninety":
        return 90
    elif number_string == "hundred":
        return 100
    elif number_string == "thousand":
        return 1000
    elif number_string == "million":
        return 1000000

    return 0


def parse_int(string):
    numbers = string.split()

    final_result = 0
    i = 0
    while i < len(numbers):
        if i == "and":
            continue
        if i < len(numbers) - 1:
            if (
                numbers[i + 1] == "hundred"
                or numbers[i + 1] == "thousand"
                or numbers[i + 1] == "million"
            ):

                num = translate_number(numbers[i]) * translate_number(numbers[i + 1])
                print(num)
                final_result += num
                i += 2
                continue
        if "-" in numbers[i]:
            aux_numbers = numbers[i].split("-")
            num = 0
            for j in aux_numbers:
                num += translate_number(j)
            final_result += num
        else:
            final_result += translate_number(numbers[i])
        print(final_result)
        i += 1

    return final_result

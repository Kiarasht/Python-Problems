def fizz_buzz(number):
    result = ""

    for i in range(0, number):
        if i % 15 == 0:
            result += "Fizz Buzz! "
        elif i % 5 == 0:
            result += "Buzz! "
        elif i % 3 == 0:
            result += "Fizz! "
        else:
            result += str(i) + " "

    return result

print(fizz_buzz(100))

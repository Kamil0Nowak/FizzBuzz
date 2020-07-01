def fizzbuzz(entered_number):
    if entered_number % 5 == 0 and entered_number % 3 == 0:
        return "FizzBuzz"
    elif entered_number % 3 == 0:
        return "Fizz"
    elif entered_number % 5 == 0:
        return "Buzz"
    return "No fizz, no buzz and no fizzbuzz :)"


print(fizzbuzz(45))

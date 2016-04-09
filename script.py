"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""

def multiples(range): #this creates a 
    all_numbers = list(xrange(range))
    sum_list = []
    for number in all_numbers:
        if (number % 3 == 0) or (number % 5 == 0):
            sum_list.append(number)
    return sum(sum_list)

multiples(1000)
    
def multiples_faster(range): 
    """
    this second function prompts the user for a range and two numbers and then calculates the sum with regards to Euler problem.
    """
    range = range - 1
    number1 = int(raw_input("What is the first number: "))
    number2 = int(raw_input("What is the second number: "))
    number3 = number1 * number2
    calc = (number1 * 0.5 * (range // number1) * ((range // number1) + 1)) + (number2 * 0.5 * (range // number2) * ((range // number2) + 1)) - (number3 * 0.5 * (range // number3) * ((range // number3) + 1)) 
    return int(calc)

multiples_faster(int(raw_input("Please input the range: ")))


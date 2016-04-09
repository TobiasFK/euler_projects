grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
print "Grades:", grades

def multiples(range):
    all_numbers = list(xrange(range))
    sum_list = []
    for number in all_numbers:
        if (number % 3 == 0) or (number % 5 == 0):
            sum_list.append(number)
    print sum(sum_list)

multiples(1000)
    
def multiplescool(range):
    range = range - 1
    number1 = int(raw_input("What is the first number: "))
    number2 = int(raw_input("What is the second number: "))
    number3 = number1 * number2
    calc = (number1 * 0.5 * (range // number1) * ((range // number1) + 1)) + (number2 * 0.5 * (range // number2) * ((range // number2) + 1)) - (number3 * 0.5 * (range // number3) * ((range // number3) + 1)) 
    print int(calc)

multiplescool(int(raw_input("Please input the range: ")))


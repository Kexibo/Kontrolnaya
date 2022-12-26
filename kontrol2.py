# Задача номер 10

def simple_number(number):
    numbers = [1]* number
    x = number
    for i in range(len(numbers)):
        numbers[i] = x
        x -=1
    number_of_delitels = 0
    #print(numbers)
    for j in range(len(numbers)):
        if number % numbers[j] == 0:
            number_of_delitels += 1
    #print(number_of_delitels)
    if number_of_delitels == 2:
        return True
    else:
        return False

    
    


x = int(input('Введите число: '))
print(f'Это число простое - {simple_number(x)}')

#print(simple_number(13))
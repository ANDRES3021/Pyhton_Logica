#!/usr/bin/python3

def number_fibonacci(num_1, num_2):
    
    while num_2 <= 1597:
        
        serie = print(num_1, num_2, end=" ")
        num_1 = num_1 + num_2
        num_2 = num_1 + num_2
        
    return serie

res = number_fibonacci(int(input()), int(input()))
print(res)

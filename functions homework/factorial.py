def factorial(number):
    j=1
    for i in range(1,number):
        j = i*j
    return j

print(factorial(6))
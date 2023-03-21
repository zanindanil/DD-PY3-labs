def factorial(n):
    fact=1
    if  type(n) is not int :
        return Exception('Введите натуральное n')
    else:
        for i in range(1, n + 1):
            fact = fact * i

        return fact



n=3
fact = factorial(n)
print(fact)

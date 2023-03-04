def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
number = int(input("Entrez un nombre entier :"))
result = factorial(number)
print(f"La fatorielle de {number} est {result}")
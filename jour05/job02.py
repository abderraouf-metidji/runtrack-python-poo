def power(x, n):
    if n == 0:
        return 1
    else: 
        return x*power(x, n-1)
    
x = int(input("Entrez un nombre : "))
n = int(input("Entrez un exposant entier positif : "))

result = power(x, n)

print("{}^{} = {}" .format(x, n, result))
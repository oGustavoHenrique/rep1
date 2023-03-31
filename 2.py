def fibonacci(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False

n = int(input("numero: "))
if fibonacci(n) == True:
    print("está")
else:
    print("não está")



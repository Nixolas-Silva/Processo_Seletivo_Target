def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

# Example usage
n = int(input("Insira um número: "))
if is_fibonacci(n):
    print(n, "faz parte da Sequência Fibonacci")
else:
    print(n, "não faz parte da Sequência Fibonacci")
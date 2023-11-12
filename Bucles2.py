numeros = [1,2,3,4,5,6,7,8,9,10]
for num in range(0, len(numeros),2):
    print(num)
print("===================================")
for i in range(0,10,2):
    print(i)

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
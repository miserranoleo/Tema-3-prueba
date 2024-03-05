#generame una funcion iterativa del factorial de 5
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

#generame una funcion recursiva del factorial de 5
def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursive(n-1)

#generame un main para llamar a las dos funciones
if __name__ == "__main__":
    print(factorial_iterative(5))
    print(factorial_recursive(5))
def fibonacchi(n):
    array = [0,1] #initial fibonacchi numbers set as 0,1
    for i in range(2,n,1):
        array.append(array[i-1]+array[i-2])
    return array

n = int(input("Enter number of terms to be printed: "))
print(fibonacchi(n))

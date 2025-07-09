def factorial():
     n = 7
     fact = 1
     while n > 0:
          fact = fact * n
          n = n - 1
     return fact


# def fibonacci(n):
# 	fibo = []
# 	if n <= 0:
# 	   return []
# 	elif n == 1:
# 	   return [0]
# 	elif n == 2:
# 	   return [0,1]
#     else n > 2:
# 	   series = [0,1]
# 	   next_element = series[n-1] + series[n-2]
#        series = series.append(next_element)
#     return series

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        series = [0, 1]
        for i in range(2, n):
            next_element = series[i - 1] + series[i - 2]
            series.append(next_element)
        return series


print(fibonacci(10))  # Example usage, prints the first 10 Fibonacci numbers
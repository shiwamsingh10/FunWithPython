'''
Created on Jun 6, 2018

@author: shiwamsingh
'''
# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result


#To run from command line and get arguments
#python3 fibo.py 50
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
'''
Created on Jun 6, 2018

@author: shiwamsingh
'''
import fibonacci.fibo as fibo

print(fibo.fib(1000))
print(fibo.fib2(100))

print(fibo.__name__)

fib = fibo.fib
print(fib(500))
#!/usr/bin/env python3

def greet_programmer ():
    print("Hello, programmer!")    
    

def greet(Naureen):
    print (f"Hello, {Naureen}!")
    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1 + num2
    

def halve(number):
    if type (number) == int:
        return number / 2
    elif type(number) == float:
        return number / 2.0 
    else:
        return None
    pass
        
        
    

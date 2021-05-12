def add(value_1, value_2):
    """this function adds two numbers together"""
    sum = value_1 + value_2
    return sum

def subtraction(value_1, value_2):
    difference = value_1 - value_2
    return difference


def multiplication(value_1, value_2):
    product = value_1 * value_2
    return product

def division(value_1, value_2):
    quotient = value_1 / value_2
    return quotient

from tkinter import *

window = Tk()

window.title("Chase's Calculator")

window.mainloop()
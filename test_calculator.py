import pytest    #importing pytest
from calculator import add, subtract, multiply, divide

def test_add():                #for addition
    assert add(5, 3) == 8
    assert add(-1, 1) == 0

def test_subtract():            #for subtraction
    assert subtract(10, 2) == 8
    assert subtract(5, 5) == 0

def test_multiply():            #for multiplication
    assert multiply(4, 5) == 20
    assert multiply(5, 0) == 0

def test_divide():              #for division
    assert divide(10, 2) == 5
    assert divide(5, 2) == 2.5

def test_divide_by_zero():      #divison by zero
    with pytest.raises(ValueError):
        divide(10, 0)


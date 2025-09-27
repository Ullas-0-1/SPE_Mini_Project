import pytest
from app.calculator import sqrt, factorial, ln, power


# ---------- TESTING SQUARE ROOT ----------

def test_sqrt_normal():
    assert sqrt(4) == 2
    assert sqrt(9) == 3
    assert round(sqrt(2), 5) == 1.41421  #Approximation check

def test_sqrt_edge_cases():
    assert sqrt(0) == 0  #sqrt(0) is valid

def test_sqrt_negative_input():
    with pytest.raises(ValueError, match="Cannot take square root of a negative number"):
        sqrt(-4)


#---------- TESTING FACTORIAL ----------

def test_factorial_normal():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_large_number():
    # Factorial of 10 should be 3628800
    assert factorial(10) == 3628800

def test_factorial_negative_input():
    with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
        factorial(-3)




# ---------- TESTING NATURAL LOG ----------

def test_ln_normal():
    assert round(ln(1), 5) == 0.00000
    assert round(ln(2.71828), 5) == 1.00000  # ln(e) ≈ 1

def test_ln_edge_case():
    with pytest.raises(ValueError, match="Logarithm only defined for positive numbers"):
        ln(0)

def test_ln_negative_input():
    with pytest.raises(ValueError, match="Logarithm only defined for positive numbers"):
        ln(-5)



# ---------- TESTING POWER ----------

def test_power_normal():
    assert power(2, 3) == 8
    assert power(5, 0) == 1  
    assert power(0, 5) == 0

def test_power_negative_exponent():
    assert round(power(2, -2), 5) == 0.25

def test_power_fractional_base():
    assert round(power(0.5, 2), 5) == 0.25


# ---------- EDGE CASES & STRESS TESTING ----------

def test_large_numbers():
    assert sqrt(1e10) == 100000
    assert power(10, 6) == 1e6
    assert factorial(10) == 3628800

def test_extremely_large_factorial():
    # Just check it doesn't crash, we don't need exact value
    result = factorial(20)
    assert isinstance(result, int)

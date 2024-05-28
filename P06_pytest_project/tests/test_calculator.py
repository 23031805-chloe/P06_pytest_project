import pytest
from calculator.calculator import Calculator

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 3087
        assert result == expected
    
    def test_multiply(self):
        # arrange
        a = 400
        b = 10
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 4000
        assert result == expected

    
    def test_divide(self):
        # arrange
        a = 400
        b = 0
        cal = Calculator()

        #act 
        with pytest.raises(ZeroDivisionError): 
            cal.divide(a,b)




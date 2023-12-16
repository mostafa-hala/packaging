from calculator.calculator_logic import CalculatorLogic

def test_calculator_logic():
    calculator_logic = CalculatorLogic()

    # Test addition
    assert calculator_logic.evaluate_expression("2 + 3") == 5

    # Test multiplication
    assert calculator_logic.evaluate_expression("4 * 5") == 20

    # Test division
    assert calculator_logic.evaluate_expression("10 / 2") == 5

    # Test subtraction
    assert calculator_logic.evaluate_expression("8 - 3") == 5

    # Test invalid expression
    try:
        calculator_logic.evaluate_expression("10 / 0")
        assert False, "Expected ZeroDivisionError"
    except ZeroDivisionError:
        pass

z=test_calculator_logic()
if z==True:
    print("All tests passed successfully.")

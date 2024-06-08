def calculate(a,b,op):
    if op == "1":
        return a + b
    elif op == "2":
        return a - b
    elif op == "3":
        return a * b
    elif op == "4":
        if b == 0:
            return "ZeroDivide"
        return a / b
    else:
        return "Invalid operator"


def test_op1_is_working():
    assert calculate(1,1,"1") == 2.0


def test_op2_is_working():
    assert calculate(1,1,"2") == 0.0


def test_op3_is_working():
    assert calculate(1,1,"3") == 1.0


def test_op4_is_working():
    assert calculate(1,1,"4") == 1.0


def test_zero_divide():
    assert calculate(1,0,"4") == "ZeroDivide"


def test_all():
    test_op1_is_working()
    test_op2_is_working()
    test_op3_is_working()
    test_op4_is_working()
    test_zero_divide()


test_all()
while True:
    a,b = float(input("a = ")),float(input("b = "))
    op = input("1 - add, 2 - sub, 3 - mul, 4 - div\n")
    print("Result: ",calculate(a,b,op))
    print("-"*15)

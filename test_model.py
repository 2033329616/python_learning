def my_abs(x):
    """
    function:get the absolute value of the input number
    parameter: x input number
    """
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')   # 自己定义抛出异常
    if x >= 0:
        return x
    else:
        return -x
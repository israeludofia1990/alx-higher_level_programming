#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    add_res = add(a, b)
    sub_res = sub(a, b)
    mul_res = mul(a, b)
    div_res = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add_res))
    print("{:d} - {:d} = {:d}".format(a, b, sub_res))
    print("{:d} * {:d} = {:d}".format(a, b, mul_res))
    print("{:d} / {:d} = {:d}".format(a, b, div_res))


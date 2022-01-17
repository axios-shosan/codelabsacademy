try:
    a = 12
    s = "hello"
    print(a+s)
except TypeError as error:
    print(f"error about type of variables : {error}")
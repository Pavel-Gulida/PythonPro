
def new_format(string):
    cikle = len(string) // 3
    if cikle * 3 == len(string):
        cikle-=1
    i=1
    while True:
        if i > cikle:
            break
        string = string[:1-i-i * 3] + "." + string[1-i-i * 3:]
        i+=1
    return string

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

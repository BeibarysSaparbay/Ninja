def func(adress):
    c = ""
    for i in adress:
        if i == ".":
            c +="[.]"
        else:
            c += i
    return c
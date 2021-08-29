def getList(width):

    from string import ascii_lowercase
    import itertools

    ss = list()

    #ваще не понимаю как это работает
    def iter_all_strings():
        for size in itertools.count(1):
            for s in itertools.product(ascii_lowercase, repeat=size):
                #
                yield "".join(s)


    for s in iter_all_strings():
        ss.append(s)
        if len(ss) == width:
            break
    return ss

print(getList(10000))

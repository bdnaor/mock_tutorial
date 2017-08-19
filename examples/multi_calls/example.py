
def bar(i):
    print i


def foo(number):
    for i in range(0, number, 2):
        bar(i)

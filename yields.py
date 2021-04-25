# NOTE: Kind of a bad example cus range is a generator itself.

def original_generator(n):
    for i in range(n):
        yield i

def yieldf(gen):
    yield from gen

for i in original_generator(10):  # normal generator yield
    print(i)

for i in yieldf(original_generator(10)):  # yield from
    print(i)
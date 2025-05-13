def test(func):
    def wrapper(wrd):
        func(wrd)
        print("finished")
    return wrapper


@test
def say_hello(word):
    print(word)


say_hello('Hi')


# Closure


def fun1(x):
    print "fun1 calling..."

    def fun2(y):
        print "fun2 calling..."
        return x(y)

    return fun2


@fun1
def fun3(y):
    print "fun3 calling... " + y


def func(name):

    def p_name(string):
        print "I am "
        return name(string)
    return p_name

@func
def set_string(string):
    print "string"


def logging(level):
    if level == 'girl':
        print "Oh, you are beautiful"
    else:
        print "You are cool"

    def print_func(name):
        print "who are you?"

        def p_name(*args, **kwargs):
            print args, kwargs
            return name(*args, **kwargs)
        return p_name
    return print_func


@logging(level='girl')
def set_string_a(string):
    print "string"

if __name__ == "__main__":
    #set_string("test")
    #fun3('a')
    set_string_a('Tory')
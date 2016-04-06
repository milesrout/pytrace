import functools

def trace(show_counter=False, show_types=False):
    def outer_wrapper(f):
        counter = 0
        @functools.wraps(f)
        def inner_wrapper(*args):
            nonlocal counter
            counter += 1
            local_counter = counter

            args_string = None
            if show_types:
                args_string = ', '.join(
                    '{}: {}'.format(arg, type(arg).__name__
                ) for arg in args)
            else:
                args_string = ', '.join(map(str, args))

            ret = f(*args)

            if show_counter:
                print('{} {}({}) -> {}'.format(local_counter, f.__name__, args_string, ret))
            else:
                print('{}({}) -> {}'.format(f.__name__, args_string, ret))
            return ret
        return inner_wrapper
    return outer_wrapper

if __name__ == '__main__':
    for sc in [True, False]:
        for st in [True, False]:
            @trace(show_counter=sc, show_types=st)
            def fib(n):
                if n == 0:
                    return 1
                return n * fib(n-1)
            fib(5)


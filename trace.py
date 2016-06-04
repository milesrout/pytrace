# Licensed CC0, see file LICENSE.

import functools

def trace(show_counter=False, show_types=False):
    def outer_wrapper(f):
        counter = 0
        @functools.wraps(f)
        def inner_wrapper(*args):
            nonlocal counter
            counter += 1
            local_counter = counter

            if show_types:
                args_string = ', '.join(
                    '{}: {}'.format(arg, type(arg).__name__
                ) for arg in args)
            else:
                args_string = ', '.join(map(str, args))

            ret = f(*args)

            if show_counter:
                print(local_counter, end=' ')
            print('{}({}) -> {}'.format(f.__name__, args_string, ret))
            
            return ret
        return inner_wrapper
    return outer_wrapper

if __name__ == '__main__':
    for sc in [True, False]:
        for st in [True, False]:
            @trace(show_counter=sc, show_types=st)
            def fib(n):
                if n == 0 or n == 1:
                    return 1
                return fib(n-2) + fib(n-1)
            fib(6)

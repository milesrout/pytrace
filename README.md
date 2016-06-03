# pytrace

A **simple** tracing decorator for Python. So simple that it couldn't be anything but **CC0 licensed**.

```python
@trace()
def foo(a, b, c):
    return "hello, world!"
foo(1, 'a', True)
```

```
$ python3 pytrace.py
foo(1, 'a', True) -> "hello, world!"
```

**pytrace** supports showing argument types.

```python
@trace(show_types=True)
def foo(a, b, c):
    return "hello, world!"
foo(1, 'a', True)
```

```
$ python3 pytrace.py
foo(1: int, 'a': str, True: bool) -> "hello, world!"
```

**pytrace** also supports a per-definition call counter.

```python
@trace(show_counter=True)
def test_counter(n):
    return n
fac(1)
fac(10)
fac(20)
```

```
$ python3 pytrace.py
1 fac(1) -> 1
2 fac(10) -> 10
3 fac(20) -> 20
```

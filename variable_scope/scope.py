'''
LEGB
Local, Enclosing, Global, Built-in
'''

x='global x'

def test():
    y = 'local y'
    print(y)

test()
'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
local y

Process finished with exit code 0
'''

x='global x'

def test():
    y = 'local y'
    # print(y)
    print(x)

test()
'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
global x

Process finished with exit code 0
'''
x='global x'

def test():
    y = 'local y'
    # print(y)
    print(x)

test()
print(x)

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
global x
global x

Process finished with exit code 0
'''
x = 'global x'

def test():
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)
'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
local x
global x

Process finished with exit code 0
'''
x = 'global x'

def test():
    global x
    x = 'local x'
    # print(y)
    print(x)

test()
print(x)

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
local x
local x

Process finished with exit code 0
'''
def test(z):
    x = 'local x'
    # print(y)
    print(z)


test('local z')
# print(x)

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
local z

Process finished with exit code 0
'''
import builtins

print(dir(builtins))

m = min([5, 1, 4, 2, 3])
print(m)

# x = 'global x'


def test(z):
    x = 'local x'
    # print(y)
    print(z)


test('local z')
# print(z)

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
1
local z

Process finished with exit code 0
'''

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
inner x
outer x

Process finished with exit code 0
'''
def outer():
    x = 'outer x'

    def inner():
        # x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
outer x
outer x

Process finished with exit code 0
'''
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
inner x
inner x

Process finished with exit code 0
'''
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()
print(x)

'''
D:\python\.venv\Scripts\python.exe D:\python\scope.py 
inner x
outer x
global x

Process finished with exit code 0
'''



try:
    f = open('testfile.txt')
except Exception:
    print('Sorry. This file does not exist')
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
Sorry. This file does not exist

Process finished with exit code 0
'''

try:
    f = open('test_file.txt')
    var = bad_var
except Exception:
    print('Sorry. This file does not exist')
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
Sorry. This file does not exist

Process finished with exit code 0
'''

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
Sorry. Something went wrong

Process finished with exit code 0
'''

try:
    f = open('test_file.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
name 'bad_var' is not defined

Process finished with exit code 0
'''

try:
    f = open('testfile.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
[Errno 2] No such file or directory: 'testfile.txt'

Process finished with exit code 0
'''

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
Test File Contents!

Process finished with exit code 0
'''

try:
    f = open('test_file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
Test File Contents!
Executing Finally...

Process finished with exit code 0
'''

try:
    f = open('testfile.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
'''
D:\python\.venv\Scripts\python.exe D:\python\exceptions.py 
[Errno 2] No such file or directory: 'testfile.txt'
Executing Finally...

Process finished with exit code 0
'''






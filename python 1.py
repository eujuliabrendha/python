Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello, World!')
Hello, World!
print (7+4)
11
print ('7'+'4')
74
print ('Olá" + 5)
       
SyntaxError: unterminated string literal (detected at line 1)
print('Olá'+5)
       
Traceback (most recent call last):
  File "/usr/lib/python3.10/idlelib/run.py", line 578, in runcode
    exec(code, self.locals)
  File "<pyshell#4>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
print ('Olá', 5)
       
Olá 5

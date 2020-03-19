import platform
import os
import site
import multiprocessing
import cProfile
import getpass
print(getpass.getuser())
#Write a Python program to get OS name, platform and release information.
print(os.name)
print(platform.system())
print(platform.release())
print(site.getsitepackages())
print("cpu= " ,multiprocessing.cpu_count())
n="234.567"
n1="234"
print(int(n1))
print(float(n))
print(int(float(n)))

for i in range(1,10):
    print('*',end="")
print("\n")


def sum():
    print(1+2)
cProfile.run('sum()')


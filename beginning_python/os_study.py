import os
abspath = os.path.abspath(__file__)
print(abspath)
dirname = os.path.dirname(abspath)
print(dirname)
print(os.path.dirname(dirname))
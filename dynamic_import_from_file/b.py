import os
import glob
import importlib.util


def find_modules_from_folder(folder):
    absolute_f = os.path.abspath(folder)
    print(absolute_f)
    md = glob.glob(os.path.join(absolute_f, "*.py"))
    print(md)
    return [(os.path.basename(f)[:-3], f) for f in md if os.path.isfile(f) and not f.endswith('__init__.py')]


def import_modules_dynamically(mod, file_path):
    spec = importlib.util.spec_from_file_location(mod, file_path)
    md = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(md)
    return md


if __name__ == "__main__":
    module = find_modules_from_folder('tests')
    for m in module:
        print(m)
        mod = import_modules_dynamically(m[0], m[1])
        mod.hello()
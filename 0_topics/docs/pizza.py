
import os
ppath = "/Users/johncaperton/Projects/sandbox/0_topics/pizza.py"
ret = ppath[:ppath.rfind('/', 0)]
os.chdir(ret)


def make_sammy(*fixings):
    print("Making your sandwich with:")
    for fixing in fixings:
        print("\n{}".format(fixing))

#------------------------------
#   Xan's Helper Funcs
#------------------------------

import webbrowser
import os

def open_in_browser(url):
    """Open a designated file in chrome"""
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

def repl_set_cwd():
    ppath = "/Users/johncaperton/Projects/sandbox/helper.py"
    ret = ppath[:ppath.rfind('/',0)]
    os.chdir(ret)


print(os.path.dirname(os.path.abspath(__file__)))
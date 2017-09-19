#------------------------------
#   Xan's Helper Funcs
#------------------------------

import webbrowser
import os


def open_in_browser(url):
    """Open a designated file in chrome"""
    chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
    webbrowser.get(chrome_path).open(url)

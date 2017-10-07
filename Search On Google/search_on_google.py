#!/usr/bin/python

import os
import urllib

string_to_search = os.popen('zenity --entry --text="Enter Text to Search: " --title="Google here" 2> /dev/null',"r").read()
if(len(string_to_search.replace("\n",""))>0):
    os.system('firefox http://www.google.com/search?q=%s' % (urllib.quote(string_to_search)))

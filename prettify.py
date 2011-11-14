#!/usr/bin/python
#
# File:         prettify.py
#
# Purpose:      Simple dirty script to use the prettify in javadoc generated files
#
# Author:       BRAGA, Bruno <bruno.braga@gmail.com>
#
# Copyright:
#
#               Licensed under the Apache License, Version 2.0 (the "License");
#               you may not use this file except in compliance with the License.
#               You may obtain a copy of the License at
#
#               http://www.apache.org/licenses/LICENSE-2.0
#
#               Unless required by applicable law or agreed to in writing, software
#               distributed under the License is distributed on an "AS IS" BASIS,
#               WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#               implied. See the License for the specific language governing
#               permissions and limitations under the License.
#
# Notes:        This file is part of the project CustomTaglets. More info at:
#               https://github.com/brunobraga/CustomTaglets
#  
#               Bugs, issues and requests are welcome at:
#               https://github.com/brunobraga/CustomTaglets/issues
#

import os
import sys
import getopt

"""
Defines the version of this script.
"""
__VERSION__ = 0.1

"""
Defines the author of this script.
"""
__AUTHOR__ = "Bruno Braga <bruno.braga@gmail.com>"

# ############################
# CONFIGURABLE SETTINGS: BEGIN
# ############################

#
# The location of the documentation files (set by argument in command-line)
#
DOC_ROOT = "docs/"

# 
# location of prettify files 
# 
PRETTIFY_CSS_PATH = "css/"
PRETTIFY_JS_PATH = "js/"
PRETTIFY_CSS = "prettify.css"
PRETTIFY_JS = "prettify.js"

# google-code-prettify
# Latest downloads are available here
# http://code.google.com/p/google-code-prettify/downloads/list
#
PRETTIFY_URL = "http://google-code-prettify.googlecode.com/files/prettify-small-1-Jun-2011.tar.bz2"

# ############################
# CONFIGURABLE SETTINGS: END
# ############################

def usage():
    print """
%s version %s.

Usage: %s [options]

Simple dirty script to alter standard javadoc created files to use the prettify
code, an open-source solution that enable <pre> HTML tags to be better formatted
with syntax highlighting for Java.

Use this file by placing it at the root path of your project. All paths handled
by this script are relative to the location where this script is executed.

Options:

    -d  --docroot   Defines the location of the documentation generated
                    by javadoc. If not informed, "docs/" is used.

    -v  --verbose   Prints detailed information on what this script
                    is executing.
    
    -h  --help      Prints this help information 

Details of the Prettify project are available here:
    http://code.google.com/p/google-code-prettify/
    
This script is part of the open-source initiative:
    https://github.com/brunobraga/CustomTaglets/
    
    Report a problem or bug at:
        https://github.com/brunobraga/CustomTaglets/issues
    
Author: %s 

    """  % (sys.argv[0], __VERSION__, sys.argv[0], __AUTHOR__)

def print_start():
    """
    Just prints a initial information on script startup.
    """    
    print """
%s version %s. Author: %s 
Starting process. Configurable variables:
  
  DOC_ROOT: %s
  PRETTIFY_CSS_PATH: %s
  PRETTIFY_JS_PATH: %s
  PRETTIFY_URL: %s
    """ % (sys.argv[0], __VERSION__, __AUTHOR__, DOC_ROOT, PRETTIFY_CSS_PATH, PRETTIFY_JS_PATH, PRETTIFY_URL)

__verbose = False

def get_prettify():
    """
    If applicable (not installed yet), this will download a version of pretty print
    project, as defined in PRETTIFY_URL, unpack it and place the proper files 
    in their respective locations:
    
        {docroot}PRETTIFY_CSS_PATH
        {docroot}PRETTIFY_JS_PATH
    """
    
    # check if files are in place already
    if not (os.path.exists(DOC_ROOT + PRETTIFY_CSS_PATH + PRETTIFY_CSS) and os.path.exists(DOC_ROOT + PRETTIFY_JS_PATH + PRETTIFY_JS)):
        # download code
        temp_path = "/tmp/"
        source_path = "google-code-prettify/"
        temp_file = "%sprettify.tar.bz2" % temp_path
        if __verbose: print "Prettify files not found. Downloading source..."
        res = os.system("wget %s -O %s %s" % ("-v" if __verbose else "", temp_file, PRETTIFY_URL))
        if res > 0: sys.exit(2)
        if __verbose: print "Unpacking..."
        res = os.system("tar -jx%sf %s -C /tmp/" % ("v" if __verbose else "", temp_file))
        if res > 0: sys.exit(2)
        
        if not os.path.exists(DOC_ROOT + PRETTIFY_CSS_PATH):
            if __verbose: print "Creating directory for CSS/JS files..."
            res = os.system("mkdir %s %s%s" % ("-v" if __verbose else "", DOC_ROOT, PRETTIFY_CSS_PATH))
            if res > 0: sys.exit(2)
            res = os.system("mkdir %s %s%s" % ("-v" if __verbose else "", DOC_ROOT, PRETTIFY_JS_PATH))
            if res > 0: sys.exit(2)
            
        if __verbose: print "Moving files..."
        res = os.system("mv -f%s %s%sprettify.css %s%s%s" % ("v" if __verbose else "", temp_path, source_path, DOC_ROOT, PRETTIFY_CSS_PATH, PRETTIFY_CSS))
        if res > 0: sys.exit(2)
        res = os.system("mv -f%s %s%sprettify.js %s%s%s" % ("v" if __verbose else "", temp_path, source_path, DOC_ROOT, PRETTIFY_JS_PATH, PRETTIFY_JS))
        if res > 0: sys.exit(2)
        if __verbose: print "Removing garbage..."
        res = os.system("rm -rf%s %s%s" % ("v" if __verbose else "", temp_path, source_path))
        if res > 0: sys.exit(2)
        if __verbose: print "Done!"
    else:
        if __verbose: print "Prettify files are ok!"


def recurse_dirs(func, d, m, e, depth=0):
    if __verbose: print "checking dir [%s]" % d
    for item in os.listdir(d):
        item_path = os.path.join(d, item)
        if os.path.isdir(item_path):
            if __verbose: print "looping directory [%s] (depth=%s)" % (item_path, depth)
            recurse_dirs(func, item_path, m, e, depth + 1)
        else:   
            if item_path.endswith(e):    
                if __verbose: print "checking file [%s]" % item_path
                f = open(item_path, 'r')
                data = f.readlines()
                f.close()
                if str(m).lower() in str(data).lower():
                    if __verbose: print "File [%s] has <pre> tags. Updating..." % item_path
                    func(item_path, depth)

def append(fi, depth):
    """
    Dirty workaround (but works nicely) to:
    
        - append javascript and css headers to HTML file
        - add onload attribute to the body tag
    
    """
    if __verbose: print "Appending to file [%s] header..." % fi

    header = """
    <link href="%s%s%s" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="%s%s%s"></script>
    """ % ("../"*depth, PRETTIFY_CSS_PATH, PRETTIFY_CSS, "../"*depth, PRETTIFY_JS_PATH, PRETTIFY_JS)
    
    # get file content
    data = ""
    f = open(fi, 'r')
    for line in f:
        # Append to head
        if "<head>" in str(line).lower():
            data += line + header + "\n" 
        # Append to body-start
        elif "<body" in str(line).lower():
            # append onload attribute
            line = line.replace("onload=\"windowTitle();\"", "onload=\"prettyPrint(); windowTitle();\"")
            data += line  
        else:
            data += line  
    f.close()

    # rename old file
    if __verbose: print "Renaming file to .old..."
    res = os.system("mv -f%s %s %s" % ("v" if __verbose else "", fi, fi + ".old"))
    if res > 0: sys.exit(2)

    # save new file
    if __verbose: print "Saving new appended file on its place..."
    f = open(fi, 'w')
    f.write(data)
    f.close()
    if __verbose: print "Done!"

    # display a diff for the sake of the update done here
    if __verbose: 
        print "Showing diff..."
        os.system("diff -u %s %s" % (fi + ".old", fi))
    
    
def main():

    global DOC_ROOT, __verbose
    
    # read command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvd:", ["help", "verbose", "docroot"])
    except getopt.GetoptError, err:
        print str(err) # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-v", "--verbose"):
            __verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--docroot"):
            DOC_ROOT = a
            if  not os.path.exists(DOC_ROOT):
                print "docroot must be a valid path!"
                usage()
                sys.exit(2)
        else:
            print "option not available option"    
            usage()
            sys.exit(2)

    if __verbose: print_start()
    
    # make sure prettify is in place
    get_prettify()
    
    # recurse files with <pre class
    recurse_dirs(append, DOC_ROOT, "<pre", "html")

if __name__ == '__main__':
    main()

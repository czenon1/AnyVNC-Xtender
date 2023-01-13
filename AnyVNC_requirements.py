import pip

# List of libraries to check and install
libraries = ['Xlib','pyvnc2swf']

# Iterate over the list and check if each library is installed
for library in libraries:
    try:
        __import__(library)
    except ImportError:
        pip.main(['install', library])

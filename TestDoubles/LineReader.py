import os

def read_from_file(file_name):
    if not os.path.exists(file_name):
        raise Exception("Bad File")
    io = open(file_name, 'r')
    line = io.readline()
    return line
#!/usr/bin/python3.6

import sys
import re
import matplotlib.pyplot as plt

def is_initialization(line):
    if(re.search("(Created)|(Setup)", line) == None):
        return False
    return True

def is_correct_node(line, name):
    if(re.search("\[" + name, line) == None):
        return False
    return True

def is_node(line):
    if(re.search("\[node", line) == None):
        return False
    return True

def parse_line(line):
    a = re.search("\[node.*", line)
    if(a != None):
        aux = line[a.start():-1]
        #print(aux[aux.index(" ")+1:])
        return re.split(",|;", aux[aux.index(" ")+1:])
    return []

if len(sys.argv) != 3:
    print("./parse.py <logfile> <node_name>")
else:
    l = []
    f = open(sys.argv[1], "r")
    for i in f.readlines():
        if(not is_initialization(i)):
            if(is_correct_node(i, sys.argv[2])):
                l.append(parse_line(i))
    l = l[:-1]
    print("escolher gráfico:")
    for i in range(len(l[0])):
        print(str(i) + " - " + l[0][i])
    option = int(input("> "))
    plt.ylabel(l[0][option])
    plt.plot([float(x[option]) for x in l[1:] if x != []])
    plt.show()
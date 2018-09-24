import os
import re

filePath = "./ssh.log.txt"
fd = open(filePath, 'r')

with fd as reader :
    for line in reader :
        print( line )
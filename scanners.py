# requirements
import os
import re

# hard-coded parth to log file
filePath = "./ssh.log.txt"

# opening up filePath file in read mode
fd = open(filePath, 'r')
total_scans = 0;

all_split_stored = []

# prints out all lines in file
with fd as reader :
  for line in reader :
    all_split_stored.append(line.split())
    total_scans += 1

print('[scan attempts] ', total_scans)
print('[test] ', all_split_stored)


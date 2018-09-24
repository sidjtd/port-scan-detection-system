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

# now that each line is a list within a super list, organize all Addresses
all_origins = []
all_destinations = []

# This may be more effecient?
# new_list = list(set(my_list))

for unique_arrs in all_split_stored :
  all_origins.append(unique_arrs[2])
  all_destinations.append(unique_arrs[4])

print(all_origins)
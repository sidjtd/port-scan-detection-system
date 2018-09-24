# requirements
import os
import re

# hard-coded parth to log file
filePath = "./ssh.log.txt"

# opening up filePath file in read mode
fd = open(filePath, 'r')
total_scans = 0;

all_split_stored = []

empty = []

# prints out all lines in file
with fd as reader :
  for line in reader :
    split_up = line.split()
    if(len(split_up) > 0):
      all_split_stored.append(split_up)
      total_scans += 1

# now that each line is a list within a super list, organize all Addresses
all_origins = []
all_destination = []

# This may be more effecient?
# new_list = list(set(my_list))

for unique_arrs in all_split_stored :
  all_origins.append(unique_arrs[2])
  all_destination.append(unique_arrs[4])

all_origins = list(set(all_origins))
all_destination = list(set(all_destination))


# print('[scan attempts] ', total_scans)

# print('\n[scan origin hosts] ',)
# for each in all_origins:
#   print(each)

# print('\n[scan destination hosts] ')
# for each in all_destination:
#   print(each)

# requirements
import os
import re
import copy
# hard-coded parth to log file
filePath = "./ssh.log.txt"

# opening up filePath file in read mode
fd = open(filePath, 'r')
total_scans = 0;

all_split_stored = []
master_obj = {}

# prints out all lines in file
with fd as reader :
  for line in reader :
    split_up = line.split()

    # if scan line has more than 4 elements, do the following
    if(len(split_up) > 4):
      key_origin = '{}'.format(split_up[2])

      # if key doesnt exist, make it a list. If already list, just add value to lists
      if key_origin in master_obj:
        master_obj[key_origin].append(split_up[4])
      else:
        master_obj[key_origin] = []
        master_obj[key_origin].append(split_up[4])

      # prepare to create duplicate free list
      all_split_stored.append(split_up)
      total_scans += 1


total_access_attempts = copy.deepcopy(master_obj)

# print(master_obj)

for each in total_access_attempts:
  total_access_attempts[each] = len(total_access_attempts[each])

print(total_access_attempts)

# now that each line is a list within a super list, organize all Addresses
all_origins = []
all_destination = []

for unique_arrs in all_split_stored :
  all_origins.append(unique_arrs[2])
  all_destination.append(unique_arrs[4])

# dedupe
all_origins = list(set(all_origins))
all_destination = list(set(all_destination))

# prepare write_file (ensure it initializes blank)
reset_file = open('scanners_found.txt', 'w')
reset_file.write('FOUND SCANNERS\n')
reset_file.close()

# prepare file to be appended by results
append_file = open('scanners_found.txt', 'a')
append_file.write('\n[scan attempts] ' + str(total_scans) + '\n')
# print('[scan attempts] ', total_scans)

append_file.write('\n[scan origin hosts]\n')
for each in all_origins:
  append_file.write(each + '\n')
# print('\n[scan origin hosts] ',)
#   print(each)

append_file.write('\n[scan destination hosts]\n')
for each in all_destination:
  append_file.write(each + '\n')
# print('\n[scan destination hosts] ')
# for each in all_destination:
#   print(each)


append_file.close()



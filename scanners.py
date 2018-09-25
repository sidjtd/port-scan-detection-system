# requirements
import os
import re
import copy

all_split_stored = []
all_destination = []
all_origins = []
master_obj = {}

def biggest_value(dic):
  hold = 0;
  for each in dic:
    if(each > hold):
      hold = each


# prints out all lines in text file
fd = open("./ssh.log.txt", 'r')
with fd as reader :
  for line in reader :
    line = line.split()

    # if scan line has more than 4 elements, continue
    if(len(line) > 4):
      orig_as_key = '{}'.format(line[2])

      # if key doesnt exist, make it a list. If already list, add value to lists
      if orig_as_key in master_obj:
        master_obj[orig_as_key].append(line[4])
      else:
        master_obj[orig_as_key] = [line[4]]

      # prepare to create duplicate free list using following
      all_split_stored.append(line)
      all_origins.append(line[2])
      all_destination.append(line[4])

total_access_attempts = copy.deepcopy(master_obj)
unique_dest = copy.deepcopy(master_obj)
unique_totals = copy.deepcopy(unique_dest)

# create dictionary tracking total hits, each unique destination, total of unique hits
for each in total_access_attempts:
  total_access_attempts[each] = len(total_access_attempts[each])
for each in unique_dest:
  unique_dest[each] = list(set(unique_dest[each]))
for each in unique_totals:
  unique_totals[each] = len(unique_totals[each])

# dedupe values in both
all_origins = list(set(all_origins))
all_destination = list(set(all_destination))

# prepare write_file (ensure it initializes blank)
new_file = open('scanners_found.txt', 'w')
new_file.write('FOUND SCANNERS\n')
new_file.close()

# prepare file to be appended by results
file = open('scanners_found.txt', 'a')
file.write('\n[scan attempts] ' + str(len(all_split_stored )) + '\n\n[scan origin hosts]\n')

for each in all_origins:
  file.write(each + '\n')

file.write('\n[scan destination hosts]\n')
for each in all_destination:
  file.write(each + '\n')

file.write('\nCONCLUSION\n')
file.write('\nIt appears that \n')

file.close()



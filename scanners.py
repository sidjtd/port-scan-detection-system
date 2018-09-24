# requirements
import os
import re
import copy

# hard-coded parth to log file, then opening up filePath file in read mode
fd = open("./ssh.log.txt", 'r')

all_split_stored = []
master_obj = {}

# prints out all lines in text file
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

total_access_attempts = copy.deepcopy(master_obj)
unique_dest = copy.deepcopy(master_obj)
unique_totals = copy.deepcopy(unique_dest)

# create dictionary that tracks total hits per origin IP Address
for each in total_access_attempts:
  total_access_attempts[each] = len(total_access_attempts[each])

# create dictionary that tracks unique hits per origin IP Address
for each in unique_dest:
  unique_dest[each] = list(set(unique_dest[each]))

# create dictionary that tracks total unique addresses that origin hits
for each in unique_totals:
  unique_totals[each] = len(unique_totals[each])


# now that each line is a list within a super list, organize all Addresses
all_origins = []
all_destination = []
for unique_arrs in all_split_stored :
  all_origins.append(unique_arrs[2])
  all_destination.append(unique_arrs[4])

# dedupe values in both
all_origins = list(set(all_origins))
all_destination = list(set(all_destination))

# prepare write_file (ensure it initializes blank)
new_file = open('scanners_found.txt', 'w')
new_file.write('FOUND SCANNERS\n')
new_file.close()

# prepare file to be appended by results
appendee = open('scanners_found.txt', 'a')
appendee.write('\n[scan attempts] ' + str(len(all_split_stored )) + '\n')
appendee.write('\n[scan origin hosts]\n')
for each in all_origins:
  appendee.write(each + '\n')
appendee.write('\n[scan destination hosts]\n')
for each in all_destination:
  appendee.write(each + '\n')

appendee.write('\nCONCLUSION\n')
appendee.write('\nIt appears that \n')

appendee.close()



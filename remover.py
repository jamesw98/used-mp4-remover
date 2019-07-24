import os
import sys

sanity_check = "I wish to delete the above listed files"

sfk_only = False # only deletes the sfk files, keeps mp4/mp3/wav etc.
quick = False # disables the sanity check

to_remove = [] 

all_files = os.listdir('./') 

# command line arguments 
if len(sys.argv) > 1:
    if sys.argv[1] == "-s": # sfk_only
        sfk_only = True
    if sys.argv[1] == "-q": # quick
        quick = True
    if sys.argv[1] == "-sq": # sfk_only and quick 
        sfk_only = True
        quick = True

# runs though all the files in the current directory
for file in all_files:
    split_file = file.split('.') 
    
    # checks if sfk is in the current file name
    if "sfk" in split_file: 
        mp4_file_name = split_file[0] + '.' + split_file[1] 

        if not sfk_only: to_remove.append(mp4_file_name)
        to_remove.append(file)                      

print("\nAre you sure you want to delete the following files?")
for file in to_remove:
    print("   " + file)
response = raw_input("\n(y/n) ")

if response == 'y' :

    if not quick:
        sanity = ""
        while(sanity != sanity_check):
            print("\nPlease type the sanity check to continue:")
            print("'I wish to delete the above listed files'")
            sanity = raw_input(":: ")
    
    # removes files
    for file in all_files:
        if file in to_remove:
            os.remove(file)

else:
    print("Exiting...") 
        
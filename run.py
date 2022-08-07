import os
import shutil
from helper import utility

# Ask user to provide valid directory path
directory = input("Enter the path of the directory: ")
while not os.path.isdir(directory):
    print("\n!!!Invalid directory path.")
    directory = input("Please enter valid path or Enter 0 to exit: ")
    if directory == '0': exit()

# Get all the files/folder_names
old_names_list = os.listdir(directory)

# Show the welcome page
utility.welcome(old_names_list)





























































# ========================================================================
# Open all the folders and then files from list of directories
# ========================================================================
# for directory in directories:
#     # Rename the current subfolder - Remove Spaces
#     os.chdir(root)
#     if not os.path.isdir(directory): continue
#     directory_old_name = directory
#     directory_new_name = directory_old_name.replace(' ', '_')
#     os.rename(directory_old_name, directory_new_name)

#     # Change directory to sub-folder
#     os.chdir(directory_new_name)
#     current_directory = os.getcwd()
#     curr_list = os.listdir(current_directory)
#     curr_list = [dir_name for dir_name in curr_list if '.ico' not in dir_name]
#     curr_list = [dir_name for dir_name in curr_list if '.ini' not in dir_name]
#     # Remove the spaces from file_name
#     old_file_name = curr_list[0]
#     new_file_name = old_file_name.replace(' ', '_')
#     os.rename(old_file_name, new_file_name)
#     # print(new_file_name)

#     # Open the renamed file
#     file_path = os.path.join(current_directory, new_file_name)
#     os.system("start " + file_path)
# ========================================================================

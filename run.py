import os

# file1 = open("MyFile1.txt","a")
path_to_file = "E:\\Movies\\Attack On Titan\\Episodes.txt"
with open(path_to_file) as f:
    new_names = f.readlines()

episodes_dir = "E:\\Movies\\Attack On Titan\\a"
old_names = os.listdir(episodes_dir)
# print(old_names)
for video in old_names:
	pass
	# print(video)
# print(len(old_names))

for i in range(len(old_names)):
	old_name = episodes_dir + "\\" + old_names[i]
	new_name = episodes_dir + "\\" + new_names[i][:-1] + ".mkv"
	print(old_name)
	print(new_name)
	os.rename(old_name, new_name)

# episodeNamesFile = open(, "r")

# for ele in new_names:
# 	ele = ele[:len(ele)-1]
# 	print(ele)
# print(new_names)

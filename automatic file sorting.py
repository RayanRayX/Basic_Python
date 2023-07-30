import os, shutil

path =r'/storage/emulated/0/pythonDemo/'
file_name = os.listdir(path)

folder_name = ['csv files', 'music files','image files']

for loop in range(0,3):
	if not os.path.exists(path + folder_name[loop]):
		print(path + folder_name[loop])
		os.makedirs(path + folder_name[loop])

for file in file_name:
	if ".csv" in file and not os.path.exists(path + "csv files/" + file):
		shutil.move(path + file, path + "csv files" + file)
	elif ".jpeg" in file and not os.path.exists(path+ "image files/" + file):
		shutil.move(path + file, path + "image files/" + file)
	elif ".mp3" in file and not os.path.exists(path + "music files/" + file):
		shutil.move(path + file,path + "music files/" + file)
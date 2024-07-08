import os

path_src='/home/nrc/test_data/oxts/data'
filename=os.listdir(path_src)
filename.sort(key=lambda x:int(x[5:-4]))
i=0
for file in filename:
	if i>=0 and i<=9:
		new_name = "000000000"+str(i)+'.txt'
	if i>=10 and i<=99:
		new_name = "00000000"+str(i)+'.txt'
	if i>=100 and i<=999:
		new_name =  "0000000"+str(i)+'.txt'
	if i>=1000 and i<=9999:
		new_name =  "000000"+str(i)+'.txt'
	os.rename(os.path.join(path_src,file), os.path.join(path_src,new_name))
	i+=1


path_src='/home/nrc/test_data/image_00/data'
filename=os.listdir(path_src)
filename.sort(key=lambda x:int(x[5:-4]))
i=0
for file in filename:
	if i>=0 and i<=9:
		new_name = "000000000"+str(i)+'.png'
	if i>=10 and i<=99:
		new_name = "00000000"+str(i)+'.png'
	if i>=100 and i<=999:
		new_name =  "0000000"+str(i)+'.png'
	if i>=1000 and i<=9999:
		new_name =  "000000"+str(i)+'.png'
	os.rename(os.path.join(path_src,file), os.path.join(path_src,new_name))
	i+=1

path_src='/home/nrc/test_data/image_01/data'
filename=os.listdir(path_src)
filename.sort(key=lambda x:int(x[5:-4]))
i=0
for file in filename:
	if i>=0 and i<=9:
		new_name = "000000000"+str(i)+'.png'
	if i>=10 and i<=99:
		new_name = "00000000"+str(i)+'.png'
	if i>=100 and i<=999:
		new_name =  "0000000"+str(i)+'.png'
	if i>=1000 and i<=9999:
		new_name =  "000000"+str(i)+'.png'
	os.rename(os.path.join(path_src,file), os.path.join(path_src,new_name))
	i+=1

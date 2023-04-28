import os
import shutil

from_dir = "C:/Users/Xervice665/Downloads"
to_dir = "C:/Users/Xervice665/Desktop/Document_Files"

list_of_docs = os.listdir(from_dir)
print(list_of_docs)

for file_name in list_of_docs:
    name,extensions = os.path.splitext(file_name)
    print(name)
    print(extensions)

    if extensions == '':
        continue
    if extensions == ['.pdf','.txt','.doc','.docx']:
        path1 = from_dir + '/' + file_name 
        path2 = to_dir + '/' + 'Document_Files'
        path3 = to_dir + '/' + 'Document_Files' + '/' + file_name

        if os.path.exists(path2):
            print("Moving" + file_name + ".....")
            shutil.move(path1,path3)
        else :
            os.makedirs(path2)
            print("Moving" + file_name + ".....")
            shutil.move(path1,path3)

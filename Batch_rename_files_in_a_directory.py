import os 

files= os.listdir(".")
counter=1

for file in files: 
    if file.endswith(".txt"):
        new_name=f"newfile_{counter}.txt"

        os.rename(file,new_name)
        counter+=1
        




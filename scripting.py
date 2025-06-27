import os 

#functing to extract current working directory
def current_directory():  
    cwd=os.getcwd
    print(cwd)

#how to retrive a part of a particular file/file sample
def file_path(filename):
    path=os.path.abspath(filename)  #absolute path give the paths name right from your c drive 
    #relative path name is the path respective to our current working directly
    print(path)


current_directory()
filename="sample.txt"
file_path(filename)

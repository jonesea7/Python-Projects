#	Author:		Edmund Alyn Jones
#
#	Purpose:	This scripts job is to check a specific folder on the hard drive
#				and verify whether a file ends with '.txt' file extension. If it does
#				the script should print the qualifying file names and time-stamps to the console for the user.
#	
#   Note:       I will create a directory with at least two 'txt' files to see if this script actually works.
#
#	File:		PyIODrill.py
#
#	Project:	GetThemTxtsYo!

#import os module
import os


#create a directory

os.makedirs('C:\\Wasteland\\Tips\\')

#make that directory the new current directory

os.chdir('C:\\Wasteland\\Tips\\')

#add files to said directory


newFileList = ['eddy.txt', 'jones.txt', 'samson.py', 'miracle.html', 'gary.txt', 'fallout3.html', 'pizza.txt', 'erick.py', 'malcolm.html', 'lather.py']


def birthFile():
    for filename in newFileList:
        createdFiles = open(filename, 'w+').write('This is content.')
        return createdFiles


pathName = 'C:\\Wasteland\\Tips\\'

def createDir():
    for filename in createdFiles:
        newDir = os.path.join(pathName,filename)
        return newDir

newDir = createDir()

userListDir = os.listdir(newDir)


#use the listdir() method from the os module to list directory in a folder.

#first we need to set variables for the path itself





def getDir():


    for file in userListDir:

        if '.txt' in file:
        
            #path.join to concat the file name to its file path. This allows us to print an absolute path to the console
            
            fullPath = os.path.join(pathName,file)
            
            #getmtime() is the method that will help us retrieve the timestamp for each file.
            
            timeStp = os.path.getmtime(fullPath)

            #Remember you need the script to print to the console the name of the 'txt' files AND their respective timestamps.

            print("The path is: " + fullPath + "\nThe last modification time is: " + str(timeStp))

        else:
            print('There are no files with the txt designation in this folder.')











if __name__ == "__main__":
    getDir()
  


#	Author:		Edmund Alyn Jones
#
#	Purpose:	This scripts job is to check a specific folder on the hard drive
#				and verify whether a file ends with '.txt' file extension. If it does
#				the script should print the qualifying file names and time-stamps to the console for the user.
#	
#   Note:       I will create a directory with at least two 'txt' files to see if this script actually works.
#               I have included the link to the directory on GitHub.
#
#	File:		drillPage100.py
#
#	Project:	GetThemTxtsYo!

#import os module
import os

#use the listdir() method to iterate through files

#first we need to establish variables/containers for the path and the files

pathName = 'C:\\PyProjects\\'

userListDir = os.listdir(pathName)



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
            print('This file does not have the \'.txt\' designation.')











if __name__ == "__main__":
    getDir()
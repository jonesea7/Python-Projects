#   Author:     Edmund Alyn Jones
#
#   Project:    dB Drill for Python Course
#
#   Summary:    Create a dB and use it to extract the names of the files with '.txt' designation
#               and print to the console for the user.
#               


#import sqlite3

import sqlite3

#establish a connection/cursor setup function

connection = sqlite3.connect('TextExtract.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_txt_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,col_file TEXT)") ## add field with INTEGER PRIMARY KEY AUTO-INCREMENT, add field that uses a string
    
    connection.commit()

connection.close()


fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

print(fileList)

#create a function that extracts the '.txt' files and places them into a separate variable

newFileList = []

def extractFile():
    for filename in fileList:
        if '.txt' in filename:
           newFileList.append(filename)
           

extractFile()

print(newFileList)

#add the list of '.txt' files to the dB
connection = sqlite3.connect('TextExtract.db')

with connection:
    cursor = connection.cursor()
    for file in fileList:
        if '.txt' in file:
            cursor.execute("INSERT INTO tbl_txt_file(col_file) VALUES (?)", (file,))
    
    connection.commit()

connection.close()

#print the qualifying texts to the console

connection = sqlite3.connect('TextExtract.db')

with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tbl_txt_file")
    varFile = cursor.fetchall()
    for item in varFile:
        message = f"File name: {item}"
    print(message)

#if __name__ == '__main__':
 #   extractFile()
import zipfile
import os
import shutil
import subprocess
def extract(imgs_folder):
    def remove_files(directory):
        paths=[]
        for root, directories, files in os.walk(directory):
             for filename in files:
                    filepath=os.path.join(root,filename)
                    os.remove(filepath)

     #To remove files if there are any
    remove_files('extracted_files')

    with zipfile.ZipFile(fileName,'r') as zip:
        zip.extractall("extracted_files") 
    shutil.copytree("extracted_files/word/media",imgs_folder)
    remove_files('extracted_files')
def main():
     input_file=input("Enter your .docx file name : ")
     if(input_file[-4:]=='docx'):
          global fileName
          fileName=input_file
          global extractedFolder
          extractedFolder = 'extracted_files/word/media/'   #path to generated media media folder obtained by extracting files from zip
          imgs_folder=input("Enter folder name to place images:")
          extract(imgs_folder)
          
     else:
          print("please enter .docx file")

if __name__=="__main__":
    main()     
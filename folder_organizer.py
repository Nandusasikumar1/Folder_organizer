from pathlib import Path
import string
import shutil

alphabets=list(string.ascii_uppercase)

class FolderDoesNotExistError(Exception):
    def __init__(self, message) :
        super().__init__(message)

class Folder_check:
  
    def __init__(self,folder:str) :
        self.folder=folder
        self.folder_path=Path(self.folder)
        self.check_path()

    def __repr__(self) -> str:
        return f'Selected folder is {self.folder}'
    
    def check_path(self):
        if self.folder_path.is_dir():
           return True
        else:
            raise FolderDoesNotExistError(message='Folder does not exist')
    
    def get_path(self):
        return self.folder_path

class Arrange_files(Folder_check):
    
    def get_file_list(self) -> list:#returns a list of files in the folder
        file_path=super().get_path()
        files=[i.parts[-1] for i in file_path.iterdir() if i.is_file()]
        return files
    
    def file_dictionary(self) ->dict:
        """Returns a dictionary containing alphabets as keys and corresponding 
        file names as list of values """

        file_list=self.get_file_list()
        file_dict= dict.fromkeys(alphabets)
        for i in file_dict:
            file_dict[i]=[j for j in file_list if j.startswith(i) or j.upper().startswith(i)]
        return {key:val for key,val in file_dict.items() if len(val)!=0}


class Move_files ( Arrange_files):
    
    def make_folders(self):#Creates folders with names as alphabet 

        folders=list(super().file_dictionary().keys())
        parent_folder=self.folder_path
        for folder in folders:
            new_path=parent_folder/folder
            new_path.mkdir(exist_ok=True)
        
    def move_files(self):#Moves files to their respective folder based on the first letter of the file
        self.make_folders()
        src_folder=self.folder_path
        for i in super().file_dictionary():
            destination_folder=src_folder/i
            for j in super().file_dictionary()[i]:
                shutil.move(rf'{src_folder/j}',rf'{destination_folder}')
            
       
c=Move_files(folder=r'C:\Users\user\Pictures\Screenshots')
c.move_files()



    
    


    

import pathlib
import fnmatch
import os

class local_file(self):
    '''
    @Descirbe:
    @param pwd:
    @return
    '''
    def getfiles(self, pwd, pattern=None):
        if os.path.isdir(pwd):
            for file in pathlib.Path(pwd).iterdir():
                if fnmatch.fnmatch(file, pattern) :
                    print(file)
                    #todo 插入数据库
        else :
            return

    '''
    @Descirbe:
    @param pwd:
    @return
    '''
    def findfile(self, filepwd):
        if os.path.isfile(filepwd):
            filename=os.path.


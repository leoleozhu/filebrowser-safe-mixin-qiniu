#coding: utf-8
from django.core.files.base import ContentFile
from filebrowser_safe.storage import StorageMixin


class QiniuStorageMixin(StorageMixin):

    def isfile(self, name):
        return self.exists(name)

    def isdir(self, name):
        if not name:
            return True

        if self.isfile(name):
            return False

        dirs, files = self.listdir(name)
        return True if dirs or files else False

    def move(self, old_file_name, new_file_name, allow_overwrite=False):
        if(self.isfile(old_file_name)): # move if isfile
            if self.exists(new_file_name):
                if allow_overwrite:
                    self.delete(new_file_name)
                else:
                    raise Exception("The destination file '%s' exists and allow_overwrite is False" % new_file_name)

            ret, info = self.bucket_manager.rename(self.bucket_name, old_file_name, new_file_name)
            if ret is None or info.status_code != 200:
                raise Exception("Failed to move %s to %s, reason: %s" % (old_file_name, new_file_name, info) )

        else:
            dirs, files = self.listdir(old_file_name)
            if files:
                for f in files:
                    self.move(old_file_name+'/'+f, new_file_name+'/'+f, allow_overwrite)
            if dirs:
                for d in dirs:
                    self.move(old_file_name+'/'+d, new_file_name+'/'+d, allow_overwrite)

    def makedirs(self, name):
        self.save(name + "/.folder", ContentFile(""))

    def rmtree(self, name):
        if(self.isfile(name)): # delete if isfile
            self.delete(name)
        else:
            dirs, files = self.listdir(name)
            if files:
                keys = [ name+'/'+f for f in files ]
                for k in keys:
                    self.delete(k)
            if dirs:
                for d in dirs:
                    self.rmtree(name+'/'+d)

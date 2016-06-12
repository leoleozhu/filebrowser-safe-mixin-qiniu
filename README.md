Overview
========

Some methods are necessary for `filebrowser_safe` to browse the file storage
(e.g. `isfile`, `isdir`). Which can be achived by defining a `Mixin` class.

filebrowser_safe contains `Mixin` classes for famous storage providers like Amazon or Google.

Qiniu is a file service provider in China and of course not in the list.

This project defines an extension for filebrowser_safe to make it work with QiniuStorage (django-qiniu-storage).

# Usage


`pip install filebrowser-safe-mixin-qiniu`

Then, add the following lines at your django application's entry point.


```python
from qiniustorage.backends import QiniuStorage
from filebrowser_safe_mixin_qiniu.storage import QiniuStorageMixin

if QiniuStorageMixin not in QiniuStorage.__bases__:
    QiniuStorage.__bases__ += (QiniuStorageMixin,)
```

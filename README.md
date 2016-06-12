Overview
========

Some methods are necessary for `filebrowser_safe` to browse the file storage
(e.g. `isfile`, `isdir`). Which can be achived by defining a `Mixin` class.

filebrowser_safe contains `Mixin` classes for famous storage providers like Amazon or Google.

Qiniu is a file service provider in China and of course not in the list.

This project defines an extension for filebrowser_safe to make it work with QiniuStorage (django-qiniu-storage).

from setuptools import setup, find_packages

setup(
    name="filebrowser_safe_mixin_qiniu",
    version="0.1.1",
    description="Contain QiniuStorageMixin, which makes filebrowser_safe compatible with Qiniu",
    long_description=open("README.md").read(),
    author="Leo Zhu",
    author_email="leiping.zhu@gmail.com",
    url="http://github.com/leoleozhu/filebrowser-safe-mixin-qiniu",
    install_requires=["filebrowser-safe", "django-qiniu-storage>=2.0.0"],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)

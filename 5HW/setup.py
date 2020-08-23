"""from distutils.core import setup, Extension

def main():
    setup(name="sample",
          version="1.0.0",
          description="Example of C extensions",
          author="Anton Kukhtichev",
          author_email="a.kukhtichev@corp.mail.ru",
          ext_modules=[Extension("sample", ["3.c"])])

if __name__ == "__main__":
    main()"""
from distutils.core import setup, Extension

setup(name="custom", version="1.0",
      ext_modules=[Extension("custom", ["custom.c"])])


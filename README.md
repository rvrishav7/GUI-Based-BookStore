# GUI-Based-BookStore
I have created an executable GUI based application of an BookStore through Python. There are 2 files, one is 'frontend.py' and the second 'backend.py'. 
The frontend.py file is the driver program also, which designs the GUI of the application, and links it to the backend.py file. Now, the backend file is bascially a code in 'sqlite3'  with some basic operations like create table, insert queries, update and delete.

Once You have created both the files, to make the front-end executable. 
You need following command to run in the same directory as the above mentoned files: 

pyinstaller frontend.py --onefile --windowed

This will create an executable file, you can run it simply by clicking on it.

Enjoy!!

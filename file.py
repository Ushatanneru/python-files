import pyodbc
conn=pyodbc.connect('Driver={SQL Server};'
                    'Server=HCL-02-NEW-19\SQLEXPRESS;'
                    'Database= FileSearchResults;'
                    'Trusted_Connection=yes;')
cursor=conn.cursor()
cursor.execute('''
                 INSERT INTO  FileSearchResults_table2 (File_Location, SearchCount, NameOfFile)
                 VALUES
                 ('C:\file\file1\file2\file3\file4\file5\file6\file7\file8\file9\file10\ProgramDemo.txt')
                                                ''')
conn.commit();
cursor.execute('Select *From FileSearchResults_table')
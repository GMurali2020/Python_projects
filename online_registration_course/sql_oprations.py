# this is manually created sqlite3 table ,here not using any orm models

import sqlite3 as sql
conn=sql.connect("onlineclasses.sqlite3")
curs=conn.cursor()
def createcoursetable():
    curs.execute("create table course(cno number primary key,course_name text,"
                 "course_faculty text,couse_date date,course_time text,"
                 "fee real,duration number)")
    curs.close()
    print("table is created")
createcoursetable()

from flask import Flask
from flask import render_template
from flask import request
#import sql_oprations
import sqlite3 as sql
app = Flask(__name__)


@app.route('/admin')
def admin_login():
    return render_template("admin_login.html")
@app.route('/validate', methods=['POST'])
def validate_admin_login():
    username=request.form.get('t1')
    password=request.form.get('t2')
    if username=="hari" and password=='Hari123':
        return render_template("admin_wellcome.html")
    else:
        mess={"error":"invalid login"}
        return render_template('admin_login.html',message=mess)


@app.route('/admin_home')
def admin_home():
    return render_template("admin_wellcome.html")

@app.route('/new_class')
def new_class():
    return render_template('new_class.html')
@app.route('/save_course',methods=['post'])
def save_course():
    name=request.form.get('c1')
    faculty = request.form.get('c2')
    data = request.form.get('c3')
    time = request.form.get('c4')
    fee = request.form.get('c5')
    duration = request.form.get('c6')
    print(name,faculty,data,time,fee,duration)
    conn=sql.connect('onlineclasses.sqlite3')
    curs=conn.cursor()
    curs.execute('select max(cno) from course')
    res=curs.fetchone()
    print(res)
    if res[0]:
        cno=res[0]+1
    else:
        cno=1001
    curs.execute("insert into course values (?,?,?,?,?,?,?)",(cno,name,faculty,data,time,fee,duration))
    conn.commit() # is save purpuse
    conn.close()
    return render_template('new_class.html',message='new class saved')

@app.route('/view_all_sheduled')
def view_all_sheduled():
    conn=sql.connect('onlineclasses.sqlite3')
    curs=conn.cursor()
    result=curs.execute('select * from course')
    res=result.fetchall()
    #print(res)
    return render_template('view_all_sheduled.html',data=res)
@app.route('/update_course')
def update_course():
    cno=request.args.get('idno')
    conn = sql.connect('onlineclasses.sqlite3')
    curs = conn.cursor()
    result = curs.execute('select * from course where cno=?',(cno,))
    res=result.fetchone()
    return render_template('update_course.html',data=res)

@app.route('/save_course_update',methods=['POST'])
def save_course_update():
    cno=request.form.get('c0')
    name = request.form.get('c1')
    faculty = request.form.get('c2')
    date = request.form.get('c3')
    time = request.form.get('c4')
    fee = request.form.get('c5')
    duration = request.form.get('c6')
   # print(cno,name,faculty,date,time,fee,duration)
    conn=sql.connect('onlineclasses.sqlite3')
    curs=conn.cursor()
    curs.execute('update course set course_name=?,course_faculty=?,couse_date=?,course_time=?,fee=?,duration=? where cno=?',
                 (name,faculty,date,time,fee,duration,cno))
    conn.commit()
    conn.close()
    return view_all_sheduled()

@app.route('/delete_couse_scheduled')
def delete_couse_scheduled():
    cno=request.args.get('idno')
    conn=sql.connect('onlineclasses.sqlite3')
    curs=conn.cursor()
    curs.execute('delete from course where cno=?',(cno,))
    conn.commit()
    conn.close()

    return view_all_sheduled()
if __name__ == '__main__':
    app.run()

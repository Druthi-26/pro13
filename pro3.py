from flask import Flask,request,jsonify
import sqlite3

app=Flask(__name__)
def init_db():
    conn=sqlite3.connect('student.db')
    cursor=conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS student(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       name TEXT NOT NULL,
                       email TEXT NOT NULL,
                       age INTEGER)
                   ''')
    conn.commit()
    conn.close()

@app.route('/student',methods=['POST'])
def Insert_student():
    data=request.get_json()
    conn=sqlite3.connect('student.db')
    cursor=conn.cursor()
    cursor.execute(
        'INSERT INTO student(name,email,age) VALUES(?,?,?)',
        (data['name'],data['email'],data.get('age',0))
        )
    conn.commit()
    student_id=cursor.lastrowid
    conn.close()
    return jsonify({"message":"student created","id":student_id}),201

@app.route('/student',methods=['GET'])
def get_student():
    conn=sqlite3.connect('student.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM student')
    rows=cursor.fetchall()
    conn.close()
    student=[{"id":r[0],"name":r[1],"email":r[2],"age":r[3]} for r in rows]
    return jsonify(student)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)


     
    

 
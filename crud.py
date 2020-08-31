import mysql.connector as mysql

def crud_get(id):
    con = mysql.connect(host="localhost", user="root", passwd="", database="student")
    custor = con.cursor()
    custor.execute("""SELECT * FROM student where id = "%s" """ % (id))
    rows = custor.fetchall()

    con.commit()
    con.close()
    return rows[0][1], rows[0][2]


def crud_insert(id,name,surname):
    con = mysql.connect(host = "localhost", user = "root", passwd= "", database="student" )
    custor = con.cursor()
    custor.execute("""INSERT INTO student
                      VALUES ('%s', '%s', '%s')""" % (id, name,surname))
    con.commit()
    con.close()



def crud_delete(id):
    con = mysql.connect(host = "localhost", user = "root", passwd= "", database="student" )
    custor = con.cursor()
    custor.execute("""DELETE FROM student
                      WHERE id = '%s' """ % (id))
    con.commit()
    con.close()



def crud_update(id,name,surname):
    con = mysql.connect(host = "localhost", user = "root", passwd= "", database="student" )
    custor = con.cursor()
    custor.execute("""UPDATE student
                      SET name ="%s",surname ="%s"
                       WHERE id = '%s' """ % (name,surname,id))
    con.commit()
    con.close()



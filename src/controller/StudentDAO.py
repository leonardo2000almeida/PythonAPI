import psycopg2
from psycopg2.extras import RealDictCursor
from src.model_.Student import Student

class StudentDAO:

    def __init__(self): pass

    @staticmethod
    def insert_student(self, student: Student):
        conn = psycopg2.connect("host=localhost dbname= Students user=postgres password=918171")
        cur = conn.cursor()
        cur.execute("INSERT INTO person(name, cpf) VALUES (%s, %s)", (student.getName(), student.getCpf()))
        cur.execute("INSERT INTO student(registration_number, cpf_person) VALUES (%s, %s)",
                    (student.getRegistrationNumber(), student.getCpf()))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def delete_student(self, student: Student):
        conn = psycopg2.connect("host=localhost dbname= Students user=postgres password=918171")
        cur = conn.cursor()
        cur.execute("DELETE FROM student WHERE cpf_person = %s",(student.getCpf()))
        cur.execute("DELETE FROM person where cpf = %s", (student.getCpf()))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def update_student(self, student: Student):
        conn = psycopg2.connect("host=localhost dbname= Students user=postgres password=918171")
        cur = conn.cursor()
        cur.execute("UPDATE person SET name=%s, cpf=%s WHERE cpf=%s", (student.getName(), student.getCpf()))
        cur.execute("UPDATE student SET registration_number=%s", (student.getRegistrationNumber()))
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def list_students(self):
        conn = psycopg2.connect("host=localhost dbname= Students user=postgres password=918171")
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute("SELECT * FROM person INNER JOIN student on person.cpf = student.cpf_person")
        students = cur.fetchall()
        cur.close()
        conn.close()
        return students

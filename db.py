import mysql.connector
import pandas as pd

data = pd.read_csv('random_data.csv')
data = pd.DataFrame(data)

db = mysql.connector.connect(
    # host='localhost',
    user='root',
    password='lol',
    database='ip_practical'
)
cursor = db.cursor()

for i,row in data.iterrows():

      cursor.execute(
        "INSERT INTO students (student_name) VALUES (%s) ON DUPLICATE KEY UPDATE student_id=LAST_INSERT_ID(student_id)",
        ([(row.student_name)])
    )
      cursor.execute(
        "INSERT INTO classes (class_name) VALUES (%s) ON DUPLICATE KEY UPDATE class_id=LAST_INSERT_ID(class_id)",
        ([(row.class_name)])
    )

      cursor.execute(
        "INSERT INTO subjects (subject_name) VALUES (%s) ON DUPLICATE KEY UPDATE subject_id=LAST_INSERT_ID(subject_id)",
        ([(row.subject_name)])
    )
      cursor.execute(
          "INSERT INTO marks (student_id, subject_id, marks) "
          "VALUES ((SELECT student_id FROM students WHERE student_name=%s LIMIT 1), "
          "(SELECT subject_id FROM subjects WHERE subject_name=%s LIMIT 1), %s)",
          (row.student_name, row.subject_name, row.marks)
      )


db.commit()
db.close()

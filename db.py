import mysql.connector
import pandas as pd

# Read CSV
data = pd.read_csv('random_data.csv')
data = pd.DataFrame(data)

# Connect to MySQL
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

    # Next, insert the class into the 'classes' table if not already present
      cursor.execute(
        "INSERT INTO classes (class_name) VALUES (%s) ON DUPLICATE KEY UPDATE class_id=LAST_INSERT_ID(class_id)",
        ([(row.class_name)])
    )

    # Next, insert the subject into the 'subjects' table if not already present
      cursor.execute(
        "INSERT INTO subjects (subject_name) VALUES (%s) ON DUPLICATE KEY UPDATE subject_id=LAST_INSERT_ID(subject_id)",
        ([(row.subject_name)])
    )

    # # Finally, insert the marks into the 'marks' table using the generated IDs
    #   cursor.execute(
    #     "INSERT INTO marks (student_id, subject_id, marks) VALUES ((SELECT student_id FROM students WHERE student_name=%s), (SELECT subject_id FROM subjects WHERE subject_name=%s), %s)",
    #     (row.student_name, row.subject_name, row.marks)
    # )
    # Finally, insert the marks into the 'marks' table using the generated IDs
      cursor.execute(
          "INSERT INTO marks (student_id, subject_id, marks) "
          "VALUES ((SELECT student_id FROM students WHERE student_name=%s LIMIT 1), "
          "(SELECT subject_id FROM subjects WHERE subject_name=%s LIMIT 1), %s)",
          (row.student_name, row.subject_name, row.marks)
      )


db.commit()
db.close()

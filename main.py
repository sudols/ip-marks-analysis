import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

db = mysql.connector.connect(
    user='root',
    password='lol',
    database='ip_practical'
)

def fetch_data(query):
    """Fetch data from the database and return a DataFrame."""
    cursor = db.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    cursor.close()
    return df

def plot_average_marks_per_student():
    """Plot average marks per student."""
    query = """
        SELECT student_name, AVG(marks) as avg_marks
        FROM students s
        JOIN marks m ON s.student_id = m.student_id
        GROUP BY student_name
    """
    df = fetch_data(query)
    
    #bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(df['student_name'], df['avg_marks'], color='skyblue')
    plt.xlabel('Student')
    plt.ylabel('Average Marks')
    plt.title('Average Marks per Student')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

plot_average_marks_per_student()

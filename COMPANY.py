import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Tanmay@12345",
    database="school"
)

if connection.is_connected():
    print("Connected to MySQL successfully!")
import mysql.connector

# Database connection class
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tanmay@12345",
            database="school"
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()


db = Database()



# Create table if not exists
def create_table():
    query = """
            CREATE TABLE IF NOT EXISTS employee(
                                                   emp_id INT AUTO_INCREMENT PRIMARY KEY,
                                                   name VARCHAR(50),
                age INT,
                position VARCHAR(50),
                salary INT,
                dept VARCHAR(50)
                ); \
            """
    db.cursor.execute(query)
    db.commit()
    print("✔ Table 'employee' ready!")


# CREATE
def create_employee():
    name = input("Enter Employee Name: ")
    age = int(input("Enter Age: "))
    position = input("Enter Position: ")
    salary = int(input("Enter Salary: "))
    dept = input("Enter Department: ")

    query = "INSERT INTO employee (name, age, position, salary, dept) VALUES (%s, %s, %s, %s, %s)"
    values = (name, age, position, salary, dept)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Employee added successfully!")


# READ
def read_employees():
    query = "SELECT * FROM employee"
    db.cursor.execute(query)
    rows = db.cursor.fetchall()

    print("\n--- Employee Records ---")
    for row in rows:
        print(row)
    print("------------------------\n")


# UPDATE
def update_employee():
    emp_id = int(input("Enter Employee ID to update: "))
    new_name = input("New Name: ")
    new_age = int(input("New Age: "))
    new_position = input("New Position: ")
    new_salary = int(input("New Salary: "))
    new_dept = input("New Department: ")

    query = """
            UPDATE employee
            SET name=%s, age=%s, position=%s, salary=%s, dept=%s
            WHERE emp_id=%s \
            """
    values = (new_name, new_age, new_position, new_salary, new_dept, emp_id)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Employee updated successfully!")


# DELETE
def delete_employee():
    emp_id = int(input("Enter Employee ID to delete: "))

    query = "DELETE FROM employee WHERE emp_id=%s"
    values = (emp_id,)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Employee deleted successfully!")


# MENU
def menu():
    create_table()

    while True:
        print("""
===== EMPLOYEE MANAGEMENT SYSTEM =====
1. Add Employee
2. View All Employees
3. Update Employee
4. Delete Employee
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_employee()
        elif choice == "2":
            read_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting...")
            db.close()
            break
        else:
            print("Invalid choice, try again!")

menu()


























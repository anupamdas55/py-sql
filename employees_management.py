import psycopg2 as pg2

conn=pg2.connect(
dbname="employee_db",
user="postgres",
password="@ANUPAM123a",
host="localhost",
port="5432"
)
# print("Connect succesfull !")
cur=conn.cursor() # this cursor function use execute SQL queries

# for add employees >>>>>>>>>>>>>>
def add_employe(name,depertment,salary):
    cur.execute("INSERT INTO employees(name,depertment,salary)VALUES(%s,%s,%s)",(name,depertment,salary))
    conn.commit()
    print("employes add succesfull !")

# for View all employees >>>>>>>>>>>>>>
def view_employees():
    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()
    for emp in employees:
        print(emp)

# for updated employees >>>>>>>>>>>>>>>>>>>>>>
def update_employee(emp_id, name, department, salary):
    cur.execute("UPDATE employees SET name=%s, department=%s, salary=%s WHERE id=%s", (name, department, salary, emp_id))
    conn.commit()
    print("Employee updated successfully!")   

# Function to delete an employee
def delete_employee(emp_id):
    cur.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")  

#  task item
while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")
   # for user input 
    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: "))
        add_employe(name, department, salary)
    
    elif choice == '2':
        view_employees()
    
    elif choice == '3':
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter New Name: ")
        department = input("Enter New Department: ")
        salary = float(input("Enter New Salary: "))
        update_employee(emp_id, name, department, salary)

    elif choice == '4':
        emp_id = int(input("Enter Employee ID to delete: "))
        delete_employee(emp_id)

    elif choice == '5':
        break
    
    else:
        print("Invalid choice! Try again.")

# Close connection
cur.close()
conn.close()  
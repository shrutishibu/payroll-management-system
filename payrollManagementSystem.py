import mysql.connector as sqct mydb = sqct.connect (host="localhost", user="root", 
password="12345", database="payroll") cur = mydb.cursor() 
cur.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age 
INT, address VARCHAR(255), sal int)") 
 
cur.execute("CREATE TABLE IF NOT EXISTS salary (id INT, amount INT, date DATE, FOREIGN KEY(id) 
references employee(id))") # add a new employee 
def add_employee(): 
print() 
name = input("Enter name: ") age 
= input("Enter age: ") address = 
input("Enter address: ") 
sal=int(input("Enter starting salary: ")) 
sql = "INSERT INTO employee (name, age, address, sal) VALUES (%s, %s, %s, 
%s)" val = (name, age, address, sal) cur.execute(sql, val) mydb.commit 
amount = sal 
cur.execute("SELECT LAST_INSERT_ID()") 
result = cur.fetchone() 
emp_id = result[0] 
sql="INSERT INTO salary (id,amount,date) VALUES (%s, %s, 
CURDATE())" val = (emp_id,amount) cur.execute(sql, val) 
mydb.commit() 
print("Employee added successfully!") 
print() 
 
# remove an employee 
def remove_employee(): 
print() 
id = input("Enter employee ID: ") 
cur.execute("DELETE FROM salary WHERE id = %s", (id,)) 
sql = "DELETE FROM employee WHERE id = 
%s" val = (id,) cur.execute(sql, val) 
mydb.commit() 
print("Employee removed successfully!") 
print() 
 
# increase an employee's 
salary def increase_salary(): 
print() 
id = input("Enter employee ID: ") amount = 
input("Enter amount to increase: ") 
sql = "INSERT INTO salary (id, amount, date) VALUES (%s, %s, 
CURDATE())" val = (id, amount) cur.execute(sql, val) mydb.commit() 
print("Salary increased successfully!") 
# decrease an employee's salary 
def decrease_salary(): 
print() 
id = input("Enter employee ID: ") amount = input("Enter amount to 
decrease: ") sql = "INSERT INTO salary (id, amount, date) VALUES (%s, 
%s, CURDATE())" val = (id, -int(amount)) cur.execute(sql, val) 
mydb.commit() 
print("Salary decreased successfully!") 
print() 
# total salary received by an employee 
def total_salary(): 
print() 
id = input("Enter employee ID: ") 
sql = "SELECT SUM(amount) FROM salary WHERE id = 
%s" val = (id,) cur.execute(sql, val) result = 
cur.fetchone()[0]  if result: 
print("Total salary received: " + 
str(result)) print() else: print("No 
salary received yet!") 
 
# print an employee's details 
def print_employee(): 
id = input("Enter employee ID: ") sql = 
"SELECT * FROM employee WHERE id = %s" 
val = (id,) 
cur.execute(sql, val) 
result = cur.fetchone() 
if result: print() 
print("ID: " + str(result[0])) 
print("Name: " + result[1]) 
print("Age: " + str(result[2])) 
print("Address: " + result[3]) 
print("Salary: " + str(result[4])) 
print() else: 
print("Employee not found!") 
 
# print all employee details 
def print_all(): 
cur.execute("SELECT * FROM 
employee") result = cur.fetchall() for 
row in result: 
print() print("ID: " + 
str(row[0])) print("Name: 
" + row[1]) print("Age: " + 
str(row[2])) 
print("Address: " + row[3]) 
print("Salary: " + str(row[4])) 
print() 
 
# pay all the 
employes def 
pay_all(): print() 
cur.execute("SELECT 
id, sal FROM 
employee") 
result = cur.fetchall() 
for row in result: 
emp_id = row[0] 
sal = row[1] 
sql = "INSERT INTO salary (id, amount, date) VALUES (%s, %s, CURDATE())" 
val = (emp_id, sal) 
cur.execute(sql, val) 
mydb.commit() print("All employees 
paid successfully!") 
 
# truncate all values in the 
DB def trun(): print() 
x=input("Are You Sure to TRUNCATE All VALUES (Y/N) :") 
if (x=="Y" or x=="y"): 
cur.execute("DROP table salary") 
cur.execute("DROP table employee") 
cur.execute("CREATE TABLE IF NOT EXISTS employee (id INT AUTO_INCREMENT PRIMARY KEY, name 
VARCHAR(255), age INT, address VARCHAR(255), sal int)") cur.execute("CREATE TABLE IF NOT EXISTS salary (id 
INT, amount INT, date DATE, FOREIGN KEY(id) references employee(id))") mydb.commit() print("Tables 
Truncated") else: print("Revoked by User") 
 
 
while True: 
print() 
print("1. Add Employee") 
print("2. Remove Employee") 
print("3. Increase Salary") 
print("4. Decrease Salary") 
print("5. Total Salary received till 
date") print("6. Print Employee 
Details")  print("7. Print All Details") 
print("8. Pay All The Employees") 
print("9. Truncate Data") 
print("0. Exit") 
print() 
ch = input("Enter choice: 
") if ch == "1": 
add_employee() elif ch == 
"2": 
remove_employee() elif 
ch == "3": 
increase_salary() 
elif ch == "4": 
 
decrease_salary() 
elif ch == "5": 
total_salary() elif 
ch == "6": 
 
print_employee() 
elif ch == "7": 
print_all() elif ch == 
"8": pay_all() 
elif ch == 
"9": trun() 
elif ch == "0": 
print("Program Terminated By 
User") break else: 
print("\nInvalid choice.\nPlease try again.")
from flask import Flask
import os
app = Flask(__name__)

emp = {}

# Greeting 
@app.route("/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

# Create Employee
@app.route('/employee', methods=['POST'])
def create_employee():
    print ("Employee details: ")
    name = input("Name: ")
    row = int(input("Id: "))
    dept = input("Department: ")
    title = input("job Title: ")
    emp[row] = Employee(name, dept, title)

# Get all Employee details
@app.route('/employees/all', methods=['GET'])
def get_all_employees():
    return []

# Get Employee details
@app.route('/employee/<id>', methods=['GET'])
def get_employee(id):
	emp[row].display(id)
    

# Update Employee
@app.route('/employee/<id>', methods=['PUT'])
def update_employee(id):
    name = input("New name: ")
    dept = input("New Department: ")
    title = input("New job Title: ")
    emp[id].editName(name)
    emp[id].editDept(dept)
    emp[id].editTitle(title)

# Delete Employee
@app.route('/employee/<id>', methods=['DELETE'])
def delete_employee(id):
    emp[id].delete()
	del emp[id]

class Employee:
	def __init__(self, name, dept, jobTitle):
		self.name = name
		self.dept = dept
		self.jobTitle = jobTitle
		print ("Employee added successfully.")

	def editName (self, name):
		self.name = name

	def editDept (self, dept):
		self.dept = dept

	def editTitle (self, title):
		self.jobTitle = title

	def delete (self):
		del self

	def display(self, id):
		print ("Employee details:\n" + self.name + " " + str(id) + " " + self.dept + " " + self.jobTitle)

	def data (self, id):
		return self.name + "," + str(id) + "," + self.dept + "," + self.jobTitle

try:
	f = open('myfile.txt', 'r')
	lines = f.read()
	lines = lines.split("\n")
	for line in lines:
		empdet = line.split(",")
		emp[int(empdet[1])] = Employee (empdet[0], empdet[2], empdet[3])
except IOError:
	f = open('myfile.text', 'w')
finally:
	f.close()
print ("Enter\n 0: Exit\n 1: create Employee\n 2: get all employee \n 3: get particular employee\n 4:update employee\n 5: delete employee 6: Continue")
allTask = [0, 1, 2, 3, 4, 5]
task = int(input(" "))
while task in allTask:
	if task == 0:
		break
	elif task == 1:
       create_employee()
	elif task == 2:
       get_all_employees()
    elif task == 3:
        row = int(input("Id: "))
        get_employee(row)
    elif task == 4:
        row = int(input("Existing id: "))
        update_employee(row)
    elif task == 5:
        row = int(input("Existing id: "))
        delete_employee(row)
        
    


if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

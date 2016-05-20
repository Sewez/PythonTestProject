__author__ = 'Amasha'

passwords = ["password1", "password2", "password3"]

employees = {"Amasha": 1000, "Ahmed": 2000, "Abass": 3000, "Yehia": 4000, "Gom3a": 5000}

class employee(object):
	def __init__(self, emp_name, emp_salary):
		self.name = emp_name
		self.salary = emp_salary

	def salary(self):
		return self.salary


class company():
	def __init__(self, employees):
		self.staff = employees
		# Counter for iteratble 
		self.count = -1

	def add_employee(self, name, salary, employeeObj=None):
		if employeeObj is None:
			self.staff.append(employee(name, salary))
		else:
			self.staff.append(employeeObj)

	def remove_employee(self, name):
		for i, emp in enumerate(self.staff):
			if emp.name.lower() == name.lower():
				del self.staff[i]
				return 1

		return 0
		
	def get_employee_salary(self, emp_name):
		for emp in self.staff:
			if emp.name == emp_name:
				return emp.salary()

		return -1
		
	def __iter__(self):
		return self
	
	def next(self):
		self.count += 1
		if self.count < len(self.staff):
			return self.staff[self.count]
		else:
			self.count = -1
			raise StopIteration
	
	def __str__(self):
		return "\n".join(sorted(["Name: %s | Salary: %s " % (x.name, x.salary) for x in self.staff]))



a_company = company([])

# Create employees objects
a_company.add_employee("", "", employee("Amasha", 1000))
#a_company.add_employee("", "", employee("Ahmed", 2000))
#a_company.add_employee("", "", employee("Osama", 3000))
#a_company.add_employee("", "", employee("Gamal", 4000))
a_company.add_employee("", "", employee("Medhat", 5000))
#a_company.add_employee("Test", 50)

#a_company.remove_employee("amasha")

#print a_company

#for e in a_company:
#	print e.salary

while 1:
	print "1. Add employee"
	print "2. List employees"
	print "3. Remove employee"
	try:
		input = int(raw_input("Please select your option: "))

		if input == 1:
			#pass
			inputName = raw_input("Please enter employee name: ")
			inputSalary = int(raw_input("Please entery employee salary: "))
			a_company.add_employee(inputName, inputSalary)
		elif input == 2:
			print "\n", a_company, "\n"
		elif input != 1 and input != 2:
			empName = raw_input("Please enter employee name to remove: ")
			result = a_company.remove_employee(empName)
			if result != 1:
				print "Please enter valid employee name (case insensitive)"
			else:
				print "Employee {0} remove successfully from our system\n".format(empName)
	except ValueError:
		print "\n\nPlease enter valid number\n\n"

# def searchlist(listtosearch, keyword):
	# for index, item in enumerate(listtosearch):
		# if keyword == item:
			# return index

	# return -1


# def searchdic(dictosearch, key):
	# """
	# This function will return the employee salary if found.
	# :param dictosearch:
	# :param key:
	# :return: Employee salary
	# """
	# if key in dictosearch:
		# return dictosearch[key]

	# return -1
# # Ask user to input his account password
# ' Test this comment '

# inputPassword = raw_input("Please enter your password: ")

# result = searchlist(passwords, inputPassword)

# 'Check if the password is correct'
# if result != -1:
	# print "Password correct."

	# while 1:
		# 'Get employee name to search for the salary.'
		# employeename = raw_input("Plese enter employee name: ")
		# result = searchdic(employees, employeename)

		# print result

# else:
	# print "Password incorrect."

#mylist = [x*x for x in range(3)]

#for i in mylist:
#    print (i)

#mygenerator = (x*x for x in range(3))

#for i in mygenerator:
#    print (i)

#for i in mygenerator:
#    print (i)

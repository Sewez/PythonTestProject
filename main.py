__author__ = 'Amasha'

passwords = ["password1", "password2", "password3"]

employees = {"Amasha": 1000, "Ahmed": 2000, "Abass": 3000, "Yehia": 4000, "Gom3a": 5000}

def searchlist(listtosearch, keyword):
    for index, item in enumerate(listtosearch):
        if keyword == item:
            return index

    return -1


def searchdic(dictosearch, key):
    """
    This function will return the employee salary if found.
    :param dictosearch:
    :param key:
    :return: Employee salary
    """
    if key in dictosearch:
        return dictosearch[key]

    return -1
# Ask user to input his account password
' Test this comment '

inputPassword = raw_input("Please enter your password: ")

result = searchlist(passwords, inputPassword)

'Check if the password is correct'
if result != -1:
    print "Password correct."

    while 1:
        'Get employee name to search for the salary.'
        employeename = raw_input("Plese enter employee name: ")
        result = searchdic(employees, employeename)

        print result

else:
    print "Password incorrect."

#mylist = [x*x for x in range(3)]

#for i in mylist:
#    print (i)

#mygenerator = (x*x for x in range(3))

#for i in mygenerator:
#    print (i)

#for i in mygenerator:
#    print (i)

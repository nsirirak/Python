"""
Nicholas Sirirak
Final project: Pay roll report

Given name, pay rate, and worked hour
print a report
name, pay rate, and worked hour, regular hours, overtime hours, gross income,
federal tax, state tax, FICA, net income

overtime rate 1.5x
10% federal tax
6% state tax
FICA 3%
"""
import sys
from tabulate import tabulate

"""
Validate input. The function loops until the user enter valid number
"""
def isValidNumber(prompt)->float:
    value = None
    while value is None:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid input. Please try again")
        if value < 0:
            print("Value must greater than zero")
            value = None
    return value

"""
Calculate payroll require pay rate and total worked hours
over time rate is 1.5 
federal tax 10%, state tax 6% and FICA 3%
return: (regular hours, overtime hours, gross income, federal tax, state tax, FICA, net income)
"""
def payRollCalculate(payRate, workHour)->tuple:
    OT = 0
    if workHour > 40:
        OT = workHour - 40
        workHour = 40
    grossIncome = round((workHour * payRate) + (OT * payRate * 1.5), 2)
    federalTax = round(grossIncome * 0.1, 2)
    stateTax = round(grossIncome * 0.06, 2)
    FICA = round(grossIncome * 0.03, 2)
    netIncome = round(grossIncome - federalTax - stateTax - FICA,2)
    return workHour, OT, grossIncome, federalTax, stateTax, FICA, netIncome

"""
Calculate pay roll for each employee in the list and print the result.
"""
def printPayRoll():
    for e in employee_list:
        e['regular hours'], e['over time'], e['gross income'],\
        e['federal tax'], e['state tax'],e['FICA'], \
        e['net income'] = payRollCalculate(e['pay rate'], e['total hours'])
    print(tabulate(employee_list, headers='keys'))

"""
Read employee information from a file. Extract data and store in employee list
"""
def fileMode(file):
    print(f"file name = {file}" )
    d = {}
    try:
        with open (file,'r') as f:
            for line in f:
                temp = [l.strip() for l in line.split(',')]
                d.setdefault(temp[0],[temp[1], temp[2]])
                info['name'] = temp[0]
                info['pay rate'] = float(temp[1])
                info['total hours'] = float(temp[2])
                employee_list.append(info.copy())
    except Exception as e:
        print(e)

"""
Manual create employee list, asking a number of employees, name, pay rate, and worked hours.
"""
def manualMode():
    print("Welcome to employee pay stub calculator")
    employees = int(isValidNumber("How many employees : "))
    for _ in range(employees):
        name = input("Please enter employee name : ")
        pay_rate = isValidNumber(f"Please enter {name}'s pay rate per hour : $")
        hours = isValidNumber("Please enter hours worked : ")
        info['name'] = name
        info['pay rate'] = pay_rate
        info['total hours'] = hours
        employee_list.append(info.copy())

#args =  str(sys.argv)
#print(args)
info = {"name": None, "pay rate":None, "total hours":None, "regular hours":None,
            "over time":None, "gross income":None, "federal tax":None, "state tax":None,
            "FICA":None, "net income":None}
employee_list = []
if len(sys.argv) == 2:
    fileMode(sys.argv[1])
else:
    manualMode()
printPayRoll()



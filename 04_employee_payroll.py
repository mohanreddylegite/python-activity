# Case Study 4: Employee Payroll and Deduction Analysis

print("EMPLOYEE PAYROLL")
basic = 30000
allowances = 8000
overtime_hours = 10
overtime_rate = 200
incentive = 3000

overtime_pay = overtime_hours * overtime_rate
gross = basic + allowances + overtime_pay + incentive

if gross <= 20000:
    tax = gross * 0.05
elif gross <= 40000:
    tax = 1000 + (gross - 20000) * 0.10
else:
    tax = 3000 + (gross - 40000) * 0.15

professional_tax = 200
net_salary = gross - tax - professional_tax

print("Basic Pay: Rs.", basic)
print("Allowances: Rs.", allowances)
print("Overtime Pay: Rs.", overtime_pay)
print("Incentive: Rs.", incentive)
print("Gross Salary: Rs.", gross)
print("Income Tax: Rs.", tax)
print("Professional Tax: Rs.", professional_tax)
print("Net Salary: Rs.", net_salary)

def display_wage_slip(name, net_pay):
	print()
	print('WAGE_SLIP')
	print()
	print('name:',name)
	print('net_pay :', format(net_pay,".1f"))
	print()




Emp_Name = input('Emp_Name :')
Emp_Net_pay = float(input('net_pay :'))
display_wage_slip(Emp_Name, Emp_Net_pay)
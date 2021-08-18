driving = input('Have u ever driven a car?')
age = input('please enter your age:')
age = int(age)
if driving != 'ys'and driving != 'no':
	print('please enter ys/no')
	raise SystemExit

	if age >= 18:
		print('u are passed!')
	else:
		print('There is no way that you have driven a car!')
elif driving == 'no':
	if age >= 18:
		print('you can apply for a driving license now!')
	else :
		print('great,you can get your own license after few more years!')


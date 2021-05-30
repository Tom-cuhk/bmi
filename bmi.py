weight = input('Please input your weight in Kg: ')
weight = float(weight)
height = input('Please input your height in meter: ')
height = float(height)
BMI = weight / (height * height)
if BMI < 18.5:
	print('Your BMI is', BMI, 'You are Less Weight')
elif BMI >=18.5 and BMI < 24:
	print('Your BMI is', BMI, 'You are Normal')
elif BMI >= 24 and BMI <27:
	print('Your BMI is', BMI, 'You are Over Weitht')
elif BMI >= 27 and BMI <30:
	print('Your BMI is', BMI, 'You are Slightly Obesity')
elif BMI >=30 and BMI <35:
	print('Your BMI is', BMI, 'You are Modest Obestiy')
else:
	print('Your BMI is', BMI, 'You are Serious Obesity')

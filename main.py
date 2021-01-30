while True:
	try:
		year = int(input("Enter Year between 0-9999: "))
		if 0 <= year <= 9999:
			break
		raise ValueError()

	except ValueError:
		print("Enter number between 0 and 9999")

if year % 4 == 0 and year % 100 != 0:
	print(year, "is a leap year")

elif year % 400 == 0:
	print(year, "is a leap year")

elif year % 100 == 0:
		print(year, "is not a leap year")

else:
	print(year, "is not a leap year");

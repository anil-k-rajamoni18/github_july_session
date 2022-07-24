
print("======================================================")
print()

print("Program to print the course with highest fee")

print()

print("======================================================")

print()

languages = [("Python",10000),("Java",8000),("C",2000),("Scala",12000),("ReactJs",3000)]

print(languages)

highFeeCourse =""
highFee=0

for course,fee in languages:
	if(highFee<fee):
		highFee = fee
		highFeeCourse = course

print()
print("--------------------------------------------------------------")

print(f'{highFeeCourse} course  has highest fee with {highFee}')

language = input("язык программирование:")

age = int(input("сколько вам лет:"))

skill = int(input("опыт работы:"))

salary = int(input("зарплата:"))

if language == "python" and age >= 18 and age <= 65 and skill >= 3 and salary <= 60000:
	print("вы приняты на работу!")
elif language == "java" and age >= 18 and age <= 65 and skill >= 3 and salary <= 60000:
        print("вы приняты на работу!")
elif language =="javascript" and age >= 18 and age <= 65 and skill >= 3 and salary <= 60000:
        print("вы приняты на работу!")
else:
	print("к сожелению вы не приняты на работу:(")




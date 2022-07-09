#1 method string formating
name="Maxim"
day="25.06.2022"
print("Good day"+" "+name +"!"+" "+day+" "+"is a perfect day to learn some python.")
#2 method string formating
name=" Maxim"
day=" 25.06.2022 "
print("Good day"+name +"!"+day+"is a perfect day to learn some python.")
#3 method string formating
name="Maxim"
day="25.06.2022"
print("Good day %s! %s is a perfect day to learn some python." % (name,day))
#4 method string formating
name="Maxim"
day="25.06.2022"
print(f"Good day {name}! {day} is a perfect day to learn some python.")
#5 method string formating
name="Maxim"
day="25.06.2022"
print("Good day {name}! {day} is a perfect day to learn some python.".format(name=name, day=day))



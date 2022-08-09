
class Mathematician():
    def square_nums(self,list_int):
        list2=[]
        for n in list_int:
            q=n**2
            list2.append(q)
        return print("List of the squares",list2)

    def remove_positives(self,list_int2):
        list3=[]
        for n in list_int2:
            if n<0:
                list3.append(n)
        return print("List with out positive numbers",list3)
    
    def filter_leaps (self,list_year):
        list_leap_year=[]
        for n in list_year:
            if n %4==0 and n%100!=0:
                list_leap_year.append(n)
            elif n%400==0:
                list_leap_year.append(n)
            
        return print("List with leap years",list_leap_year)
m=Mathematician()
m.square_nums([7,11,5,4])
m.remove_positives([26,-11,-8,13,-90])
m.filter_leaps([2001,1884, 1995,2003,2020])

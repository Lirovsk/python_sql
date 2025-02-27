from datetime import datetime
from models import Membro, area_hist, charge_hist

class add_membro:
    def __init__(self, name=str, start_date=str, course=str, actual_area=str, more_than1_area=bool, actual_charge=str, more_than1_charge=bool, menager=bool):
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        self.course = course
        self.actual_area = actual_area
        self.more_than1_area = more_than1_area
        self.actual_charge = actual_charge
        self.more_than1_charge = more_than1_charge
        self.menager = menager
    
    @classmethod
    def getting_data(cls):
        list = []
        print("Type the name of the member:")
        name = input()
        list.append(name)
        print("Type the start date of the member:")
        start_date = input()
        list.append(start_date)
        print("Type the course of the member:")
        course = input()
        list.append(course)
        print("Type the actual area of the member:")
        actual_area = input()
        list.append(actual_area)
        print("Is there more than one area? (True or False)")
        if input() == 'True':
            more_than1_area = True
        else:
            more_than1_area = False
        list.append(more_than1_area)
        print("Type the actual charge of the member:")
        actual_charge = input()
        list.append(actual_charge)
        print("Is there more than one charge? (True or False)")
        if input() == 'True':
            more_than1_charge = True
        else:
            more_than1_charge = False
        list.append(more_than1_charge)
        print("Is the member a menager? (True or False)")
        if input() == 'True':
            menager = True
        else:
            menager = False
        list.append(menager)
        return list
    
    def __str__(self):
        return f"""Name: {self.name}
Start date: {self.start_date}
Course: {self.course}
Actual area: {self.actual_area}
More than one area: {self.more_than1_area}
Actual charge: {self.actual_charge}
More than one charge: {self.more_than1_charge}
Menager: {self.menager}"""

    def call_for_correction(self):
        print("Is there any data that needs to be corrected?")
        print(self)
        print("\nAnswer [y/n]:")
        answer = input()
        if answer == "y":
            print("Type the name of the data that needs to be corrected:")
            data = input()
            if data == "name":
                self.which_correction(1)   
            elif data == "start date":
                self.which_correction(2)
            elif data == "course":
                self.which_correction(3)
            elif data == "actual area":
                self.which_correction(4)
            elif data == "more than one area":
                self.which_correction(5)
            elif data == "actual charge":
                self.which_correction(6)
            elif data == "more than one charge":
                self.which_correction(7)
            elif data == "menager":
                self.which_correction(8)
            del answer
        
    
    def which_correction(self, field=int):
        if field == 1:
            print("Type the new name:")
            self.name = input()
        elif field == 2:    
            print("Type the new start date:")
            self.start_date = input()
        elif field == 3:
            print("Type the new course:")
            self.course = input()
        elif field == 4:
            print("Type the new actual area:")
            self.actual_area = input()
        elif field == 5:    
            print("Is there more than one area? (True or False)")
            if input() == 'True':
                self.more_than1_area = True
            else:
                self.more_than1_area = False
        elif field == 6:
            print("Type the new actual charge:")
            self.actual_charge = input()
        elif field == 7:    
            print("Is there more than one charge? (True or False)")
            if input() == 'True':
                self.more_than1_charge = True
            else:
                self.more_than1_charge = False
        elif field == 8:    
            print("Is the member a menager? (True or False)")
            if input() == 'True':
                self.menager = True
            else:
                self.menager = False
    
    def create_isntance(self):
        Membro(name=self.name,
               start_date=self.start_date,
               course=self.course,
               actual_area=self.actual_area,
               more_than1_area=self.more_than1_area,
               actual_charge=self.actual_charge,
               more_than1_charge=self.more_than1_charge,
               menager=self.menager)
        return Membro
    
    @classmethod
    def creating_process(cls):
        list = cls.getting_data()
        return cls(name=list[0],
                   start_date=list[1],
                   course=list[2],
                   actual_area=list[3],
                   more_than1_area=list[4],
                   actual_charge=list[5],
                   more_than1_charge=list[6],
                   menager=list[7])

        
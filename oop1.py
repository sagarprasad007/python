class students:
    roll_no=15;
    name ="Sagar Prasad"
    stream= "Information Technology"
    def show(self):
        print("Name: %s \nRoll No.: %d\nStream: %s"%(self.name,self.roll_no,self.stream))
emp=students()
emp.show()
print("-----------------------------------------------------------------")

print("Name :",emp.name, "\nRoll No. :",emp.roll_no, "\nStream :",emp.stream)
        

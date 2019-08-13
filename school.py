class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
    def add_student(self, student_name, grade):
        if grade in self.roster:
            self.roster[grade].append(student_name)
        else:
            self.roster[grade] = [student_name]
    def grade(self, grade):
        return self.roster[grade]
    def sort_roster(self):
        #return sorted(self.roster.items(), key = lambda x: x[0], reverse = True)
        return sorted(self.roster.items(), reverse = False)
        
     

        
        
  



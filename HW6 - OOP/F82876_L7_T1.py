class SchoolMember:
    def __init__(self,name,age):
        self.name = name
        self.age = age
 
class Teacher(SchoolMember):
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        self.dict = {}
    def getSalary(self):
        return self.salary
    def addCourse(self,signature_of_course,name_of_course):
        self.dict[signature_of_course] = name_of_course
    def getCourses(self):
        for i in self.dict:
            print i,self.dict[i]
 
class Student(SchoolMember):
	def __init__(self,name,age):
        	SchoolMember.__init__(self,name,age)
        	self.student_dict = {}
	def attendCourse(self,signature_of_course,year):
		self.student_dict[signature_of_course] = {"grade": [], "year": year} 
 	def getCourses(self):
		for i in self.student_dict:
			print i,self.student_dict[i]
	def addGrade(self,signature_of_course,grade):
		if(self.student_dict.has_key(signature_of_course) == True):
 			self.student_dict[signature_of_course]["grade"].append(grade)
	def getAvgGrade(self,signature_of_course):
		avg = 0.0
		cnt = 0.0
		for i in self.student_dict[signature_of_course]["grade"]:
			avg += i
			cnt += 1
		if(avg == 0.0 or cnt == 0.0):
			return 0.0
		return avg/cnt

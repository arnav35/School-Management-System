from django.db import models

# Create your models here.

class Teacher(models.Model):
	teacher_id = models.AutoField(primary_key=True) 
	first_name = models.CharField(max_length=100)
	middle_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200, unique=True)
	password = models.CharField(max_length=100)
	mobile = models.CharField(max_length=100)
	
	def __str__(self):
		return self.first_name

	def getPassword(self):
		return self.password

	def getEmail(self):
		return self.email

	def getfName(self):
		return self.first_name

	def getlName(self):
		return self.last_name

	def getMobile(self):
		return self.mobile

	def getId(self):
		return self.teacher_id

class ClassTeacher(models.Model):
	#foreign key teacher_id
	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	class_name = models.CharField(max_length=100, primary_key=True)
	
	def __str__(self):
 		return self.class_name
	
	def getClass(self):
		return self.class_name

class Subject(models.Model):
	#primary key subject_id
	subject_id = models.AutoField(primary_key=True)	
	subject_name = models.CharField(max_length=100, unique=True)

	def __str__(self):
 		return self.subject_name

	def getSubject(self):
		return self.subject_id

	def getSubjectName(self):
		return self.subject_name
	

class SubjectTeacher(models.Model):
	#foreign key teacher_id subject_id class

	teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)

	def getClass(self):
		return self.class_name

	def getSubject(self):
		return self.subject_id

	def getClass(self):
		return self.class_name

class Attendance(models.Model):
	student_roll = models.IntegerField()
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)

	def __str__(self):
 		return str(self.student_roll)

	def getRoll(self):
		return self.student_roll
	
	def getClass(self):
		return self.class_name

class Marks(models.Model):
	subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE)
	student_roll = models.ForeignKey(Attendance, on_delete=models.CASCADE)
	class_name = models.ForeignKey(ClassTeacher, on_delete=models.CASCADE)
	marks = models.IntegerField()
	exam_type = models.CharField(max_length=100)

	def getRoll(self):
		return self.student_roll

	def getMarks(self):
		return self.marks

	def getExam(self):
		return self.exam_type


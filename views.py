from django.shortcuts import render
from django.http import HttpResponse
from sms.models import Teacher, ClassTeacher, SubjectTeacher, Subject, Attendance, Marks
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'common/index.html') 

def acctype(request):
    return render(request, 'common/accounts.html')    

def studentLogin(request):
    return render(request, 'common/login_student.html')    

def teach_Login(request):
    id = 1
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def parent_Login(request):
    id = 2
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })

def admin_Login(request):
    id = 3
    return render(request, 'common/teach_parent_admin_login.html', {"id" : id })    

def addsubject(request):
	return render(request, 'common/addsubject.html')

def addmarks(request):
	return render(request, 'common/addmarks.html')

def addattend(request):
	return render(request, 'common/addattend.html')

def addexams(request):
	return render(request, 'common/addexams.html')

def attendance(request):
	roll_list = request.POST.get("absent_list")
	class_name = request.POST.get("class_name")

	p = ClassTeacher.objects.get(class_name=class_name)

	q = Attendance(student_roll=int(roll_list), class_name=p)
	q.save()

	return render(request, 'common/addattend.html')

def marks(request):

	subject_name = request.POST.get("subject_name")
	student_roll = request.POST.get("student_roll")
	class_name = request.POST.get("class_name")
	marks = request.POST.get("marks")
	exam_type = request.POST.get("exam_type")

	subjectobj = Subject.objects.get(subject_name=subject_name)
	studentobj = Attendance.objects.get(student_roll=student_roll)
	classobj = ClassTeacher.objects.get(class_name=class_name)
	query = Marks(subject_name=subjectobj, student_roll=studentobj, class_name=classobj, marks=marks, exam_type=exam_type)	
	query.save()

	return render(request, 'common/addmarks.html')

def loginTeacher(request):
	
	email_id = request.POST.get("email")
	password = request.POST.get("password")

	query = Teacher.objects.get(email=email_id)

	if password == query.getPassword():
		first_name = query.getfName()
		last_name = query.getlName()
		id = query.getId()
		
		try:
			classobj = ClassTeacher.objects.get(teacher_id=id)
			class_name = classobj.getClass()
		except:
			class_name = "null"
		
		try:
			subjects=list(SubjectTeacher.objects.filter(teacher_id=id))
		
			subject_name = []
			class_names = []

			for subjectobj in subjects:		
				s_id = subjectobj.getSubject()
				subject = Subject.objects.get(subject_id=s_id.subject_id)
				subject_name.append(str(subject.getSubjectName()))
				class_names.append(str(subjectobj.getClass()))
		except:
			subject_name = "null"

		return render(request, 'common/success.html', {'first':first_name, 'last':last_name, 'id':id, 'class':class_name, 'subject':subject_name, 'classes':class_names})
	else:
		messages.info(request, 'Invalid credentials')
		return render(request, 'common/teach_parent_admin_login.html', {"id" : 1 })

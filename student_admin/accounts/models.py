from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from PIL import Image
from django.db import models
from django.db.models import PositiveSmallIntegerField

# Create your models here.
#=================================================================================
rate = [(1, '1 - Under Average'),(2, '2 - Average'),(3, '3 - Great'),(4, '4 - Awesome'),(5, '4 - Master')]

UNDERGRADUATE = (
        ('BA', 'Bachelor'),
        ('BSc', 'Bachelor of Science'),
        ('MA', 'Master'),
        ('MSc', 'Master of Science'),
        ('PhD', 'Doctor of Philosophy'),
        )

gender = (('male', "Male"), ('female', "Famale"))

role = (('student', "Student"), ('teacher', 'Teacher'))

STUDY_CHOICE = (('aerospace engineering','Aerospace Engineering'),('architecture','Architecture'),('business','Business'),('chemical engineering','Chemical Engineering'),('civil engineering','Civil Engineering'),('computer engineering','Computer Engineering'),('computer science','Computer Science'),('economics','Economics'),('education','Education'),
('electrical engineering','Electrical Engineering'),('engineering','Engineering'),('graphic design','Graphic Design'),('industrial engineering','Industrial Engineering'),('software engineering','Software Engineering'))

YEAR_IN_SCHOOL_CHOICES = (
        ('Freshman', 'Freshman'),
        ('Sophomore', 'Sophomore'),
        ('Junior', 'Junior'),
        ('Senior', 'Senior'),
        ('Graduate', 'Graduate'),
        )

RATE_CHOICES = [
	(1, '1 - Kill Him'),
	(2, '2 - Send to Hadas'),
	(3, '3 - Good'),
	(4, '4 - Very Good'),
	(5, '5 - Perfect')
]

# =====================================================
class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='summaries')



class Rating(models.Model):
	text = models.CharField(max_length=50)
	rating = models.CharField(max_length=10)
	def __str__(self):
		return self.source


# =================================== Teacher =================================
class Teacher(models.Model):
    Admin_Rate =  models.PositiveSmallIntegerField(choices=rate,default=0)
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key=True)
    # is_student = models.BooleanField(default=False)
    Role = models.CharField(choices=role,default = 'teacher', max_length=300,null=True,blank = False)
    Profile_pic = models.ImageField(default='default2.jpg',upload_to='profile_pic')
    description = models.TextField(null=True, blank=True)
    Gender = models.CharField(choices=gender, max_length=300,null=True)
    cv = models.FileField(upload_to='cv')
    followed_by = models.ManyToManyField(User, related_name = "followed_by")
    undergraduate = models.CharField(choices = UNDERGRADUATE, max_length = 300, null=True ,blank = False)


    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Teacher, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_pic.path)

    def get_followed_by(self):
        return self.followed_by.all()

# =================================== Student =================================
class Student(models.Model):
    Admin_Rate = models.PositiveSmallIntegerField(choices=rate,default=0)
    user = models.OneToOneField(User, on_delete = models.CASCADE,primary_key=True)
    Role = models.CharField(choices=role,default='student', max_length=300,null=True)
    Profile_pic = models.ImageField(default='default.gif',upload_to='profile_pic')
    Gender = models.CharField(choices=gender, max_length=300,null=True)
    location = models.CharField(max_length=20)
    study_choice = models.CharField(choices = STUDY_CHOICE, max_length = 300, null=True ,blank = False)
    years_in_academy = models.CharField(choices = YEAR_IN_SCHOOL_CHOICES, max_length = 300, null=True ,blank = False)
    Followed_On = models.ManyToManyField(Teacher)
    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.Profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.Profile_pic.path)

    def get_following(self):
        return self.Followed_On.all()


#==================================================================
class Report(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
    	return self.user.username

    def save(self, *args, **kwargs):
        super(Report, self).save(*args, **kwargs)

    def get_teacher(self):
        return self.rate.all()
#==================================================================

class Users_Report(models.Model):
    from_police = models.ForeignKey(User, on_delete=models.CASCADE,related_name='from_police' ,null=True)
    on_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='on_user')
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)

    def __str__(self):
    	return self.on_user.username

    def save(self, *args, **kwargs):
        super(Users_Report, self).save(*args, **kwargs)

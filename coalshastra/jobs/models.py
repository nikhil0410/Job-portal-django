from django.db import models
from userpanel.models import User


job_type = (
	('php','PHP'),
	('python','Python'),
	('java','Java'),
	('machine_learning','Machine Learning'),
	)
class JobManager(models.Manager):
	def create_job(self,form):
		print(form.title)
		# request = self.request
		# user = request.user
		self.model.objects.create(form)

class Job(models.Model):
	title = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	tags = models.CharField(max_length=255, choices=job_type)
	recruter_id = models.ForeignKey(User)

	def __str__(self):
		return self.title

	objects = JobManager()

class StudentApplication(models.Model):
	job_fk = models.ForeignKey(Job)
	student_fk = models.ForeignKey(User)
	title = models.CharField(max_length = 255)

	def __str__(self):
		return self.title
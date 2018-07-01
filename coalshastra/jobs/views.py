from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormMixin
from django.shortcuts import render, redirect


from .models import Job,StudentApplication
from .forms import JobForm

User = get_user_model()

class jobView(FormMixin,ListView):
	template_name = "jobs/list.html"
	model = Job

	def get_queryset(self, *args, **kwargs):
		request = self.request
		return Job.objects.all()
	# def get(self, request, *args, **kwargs):
	# 	request = self.request
	# 	return Job.objects.all()
	def post(self,request,*args,**kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)

def job_view(request):
	if request.method == "POST":
		job_id = request.POST.get('obj_id')
		job_object = Job.objects.get(id=job_id)
		p = StudentApplication(job_fk = job_object, student_fk=request.user, title='Student Applied')
		p.save()
		# print(request.POST.get('obj_id'))

	queryset = Job.objects.all()
	appliedset = StudentApplication.objects.filter(student_fk=request.user)
	for q in queryset:
		q.status = 0
		for a in appliedset:
			if q.pk == a.job_fk.pk:
				q.status = 1
	print(appliedset)
	context = {
		'object_list': queryset,
		'applied_list': appliedset
	}
	return render(request, "jobs/list.html", context)

'''
class PostJob(FormView):
	form_class = JobForm
	template_name = "jobs/post-job.html"

	
	


	def form_valid(self,form):
		request = self.request
		# f = JobForm(request.POST)
		if request.method == 'POST':
			form = JobForm(request.POST)
			if form.is_valid():
				instance = form.save()
		# 		# process form data
		# 		obj = () #gets new object
		# 		obj = (
		# 			'title',
		# 			'description',
		# 			'tags',
		# 			'recruter_id',
		# 			)
		# 		obj.title = form.cleaned_data['job_title']
		# 		obj.description = form.cleaned_data['description']
		# 		obj.tags = form.cleaned_data['tags']
		# 		obj.recruter_id = User
		# 		# finally save the object in db
		# 		obj.save()
		# 		return redirect('/postjob')
		# new_article = f.save()
		# form.save()

		
		return redirect('/postjob')
'''
def post_job(request):
	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			# print(request.user)
			# form.recruter_id = request.user
			# print(form)
			job = form.save(commit=False)
			job.recruter_id = request.user 
			job.save()

			
			return redirect('/postjob')
	else :
		form = JobForm()

		args = {'form': form}
		return render(request, 'jobs/post-job.html', args)

def applied_job(request):
	if request.method == 'POST':
		obj_pk = request.POST.get('primary_key')
		StudentApplication.objects.filter(pk=obj_pk).delete()
	queryset = StudentApplication.objects.filter(student_fk=request.user)
	print(request.user.user_type)
	context = {
		'object_list': queryset
	}
	return render(request, "jobs/applied_job.html", context)

def job_application(request):
	queryset = StudentApplication.objects.filter(job_fk__recruter_id = request.user)
	print(queryset)
	context = {
	'object_list': queryset
	}
	return render(request,"jobs/applied_student.html",context)




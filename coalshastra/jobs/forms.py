from django import forms
from .models import Job

class JobForm(forms.ModelForm):
	# job_title = forms.CharField(label = 'title')
	# description = forms.CharField(label='Description')
	# tags = forms.CharField(label='tags')

	# def save(self):
	# 	postjob = super(JobForm, self)
	# 	postjob.save()
	class Meta:
		model = Job
		fields = (
			'title',
			'description',
			'tags',
			# 'recruter_id'
			) 

	# def save(self, commit=True):
	# 	job = super(JobForm, self)
	# 	job.job_title = self.cleaned_data['job_title']
	# 	job.description = self.cleaned_data['description']
	# 	job.tags = self.cleaned_data['tags']

	# 	if commit:
	# 		job.save()

	# 	return job
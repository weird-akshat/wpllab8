from django.db import models


class VoteCount(models.Model):
	option = models.CharField(max_length=30, unique=True)
	votes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.option}: {self.votes}"

# Create your models here.

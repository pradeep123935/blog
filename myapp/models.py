from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserTimeStamp(models.Model):
	created_at = models.DateTimeField(auto_now_add = True)
	update_at = models.DateTimeField(auto_now = True)
	user = models.ForeignKey(User,on_delete = models.CASCADE) 

	class Meta:
		abstract = True

class Post(UserTimeStamp):
	title = models.CharField(max_length = 100)
	description = models.CharField(max_length = 200)
	image = models.ImageField(upload_to = '')
	created_by = models.CharField(max_length = 50)
	likes = models.IntegerField(default = 0)

	def __str__(self):
		return self.title


class Comment(UserTimeStamp):
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	comment = models.TextField()
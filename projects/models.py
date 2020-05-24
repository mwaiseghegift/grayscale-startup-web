from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    image = models.ImageField(upload_to='images/projects/%Y/%m/%d', height_field=None, width_field=None, default='avatar_hat.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.name
    
    
class Photo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_photos')
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/photos/%Y/%m/%d', height_field=None, width_field=None, default='avatar_hat.jpg')
    description = models.TextField(max_length=200, default="")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-pub_date']

class comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_comments')
    text = models.TextField(max_length=256)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.text
    
    
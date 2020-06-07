from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Projects(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='profile_photos')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    link = models.URLField()
    author_profile = models.ForeignKey(Profile, on_delete=models.CASCADE,default='1', blank=True)

    def save_project(self):
        self.save()

    def __str__(self):
        return f'{self.author}Post'

    class Meta:
        db_table = 'project'
        ordering = [-created_date]

    def delete_project(self):
        self.delete()

    @classmethod
    def search_projects(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_object(cls,id):
        try:
            project = Projects.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return Project
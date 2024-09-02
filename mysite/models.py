# models.py
from django.db import models

class Profile(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    about_me = models.TextField()
    hero_image = models.ImageField(upload_to='hero/')
    about_image = models.ImageField(upload_to='about/')
    youtube_link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    connect_title = models.CharField(max_length=255)
    connect_description = models.TextField()

    def __str__(self):
        return self.title
# models.py
class Service(models.Model):
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading
# models.py
class LatestWork(models.Model):
    image_url = models.URLField()
    title = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255)

    def __str__(self):
        return self.title
# models.py
class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
# models.py
class TopSkillCategory(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
# models.py
class TopSkillDetails(models.Model):
    name = models.TextField()  # HTML content
    percentage = models.IntegerField()
    category = models.ForeignKey(TopSkillCategory, related_name='skills', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.name} - {self.percentage}%"
# models.py
class SkillInsightCategory(models.Model):
    name = models.CharField(max_length=255)
    skills = models.ManyToManyField(Skill, related_name='skills')

    def __str__(self):
        return self.name
# models.py
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.ImageField(upload_to='certificate/')
    verify_url = models.URLField()
    skills = models.ManyToManyField(Skill, related_name='certificates')

    def __str__(self):
        return self.title
# models.py
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='projects')
    image = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.name
# models.py
class TimeLine(models.Model):
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return f"{self.year} - {self.description}"
    class Meta:
        ordering = ['-year']
# models.py
class ContactUser(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    def __str__(self):
        return f"{self.full_name} - {self.subject}"



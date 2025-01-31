from django.db import models

# Create your models here.

class Role(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Home(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="profile_pics/")
    role = models.ManyToManyField(Role, blank=True)
    url1 = models.URLField(blank=True, null=True)  
    url2 = models.URLField(blank=True, null=True)  
    url3 = models.URLField(blank=True, null=True)  
    url4 = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.name


class About(models.Model):
    position = models.TextField(max_length=200)
    text = models.TextField(max_length=300)
    birthday = models.DateField()
    profil_image = models.ImageField(upload_to="profile_pics/", null=True)
    phone = models.CharField(max_length=20)
    city = models.TextField(max_length=20)
    age = models.PositiveSmallIntegerField()
    mail = models.EmailField()
    cv_file = models.FileField(upload_to="cv_files/", blank=True, null=True)
    freelencer = models.TextField(max_length=200, default="Freelance information not available")

    def __str__(self):
        return self.position
    
    

class Portfolio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Project Name")
    description = models.TextField(verbose_name="Project description") 
    image = models.ImageField(upload_to='profile_pics/', verbose_name="Project Image")
    technologies = models.CharField(max_length=200, verbose_name="Technologies") 
    github_link = models.URLField(max_length=200, verbose_name="GitHub Link", blank=True, null=True)

    def __str__(self):
        return self.title



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
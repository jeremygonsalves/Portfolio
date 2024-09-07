from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name 
    
    
class Project(models.Model): #inheriting from base project
    title = models.CharField(max_length=200)
    description=models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects") #many projects can be associated to many tags
    link = models.URLField(max_length=200, blank=True) #link to project, its ok if no link
    
    #string method
    def __str__(self):
        return self.title
    
    
class ProjectImage(models.Model): #each project is going ot have multiple images hence why we need a new project
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    ) #one project can have multiple images so need foreign key to have multiple images in the same project
    #on delete means delete images if the project is deleted
    image= models.ImageField(upload_to="project_images/")
    
    def __str__(self):
        return f"{self.project.title} Image"
    

##python3 manage.py makemigrations 
    ##needed to migrate changes to migrations folder
    
##  migrate applys the migrations and updates the DB, (created databases)

##need to create a superuser   
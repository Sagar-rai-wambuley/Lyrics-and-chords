from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name 

    class Meta:
        db_table = "Category"

class Section(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name 

    class Meta:
        db_table = "Section"

class Chord(models.Model):
    html_title_keyword = models.CharField(max_length=58, default=None, null=False)
    html_description =  models.CharField(max_length=160)
    title_name = models.CharField(max_length=200)
    singer = models.CharField(max_length=200)
    content = RichTextField()
    about = models.TextField(max_length=700)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    section = models.ForeignKey(Section, on_delete=models.DO_NOTHING, default=None)
    

    def __str__(self):
        return self.title_name

    class Meta:
        db_table = "Chord"


class Request(models.Model):
    name = models.CharField(max_length=100, null=False)
    request_song = models.TextField(max_length=300, null=False)
    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "Request"

class Search(models.Model):
    query = models.CharField(max_length=300)

    def __str__(self):
        return self.query

    class Meta:
        db_table = "Search"

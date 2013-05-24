from django.db import models

# Create your models here.
class Document(models.Model):
    date = models.DateField()
    time = models.TimeField()
    format = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    description = models.TextField()
    
class IndexedDocument(models.Model):
    document_id = Document
    indexed_document = models.FileField(upload_to = "/files")
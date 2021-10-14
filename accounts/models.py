from django.db import models

# Create your models here.
class patients:
    def __init__(self,doc_id,name):
        self.name = name
        self.doc_id = doc_id
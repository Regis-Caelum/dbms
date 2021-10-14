from django.db import models

# Create your models here.
class patients:
    def __init__(self,doc_id,name,age,dob,address,disease, prev):
        self.name = name
        self.doc_id = doc_id
        self.age = age
        self.dob = dob
        self.address = address
        self.disease = disease
        self.prev = prev
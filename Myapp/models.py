from django.db import models

# Create your models here.
class Dept(models.Model):
    #automatically id Primary Key will be created
    dname = models.CharField(max_length=20)
    dlocation = models.CharField(max_length=20)

    def __str__(self):
        return self.dname

    class Meta:
        db_table = "Dept"

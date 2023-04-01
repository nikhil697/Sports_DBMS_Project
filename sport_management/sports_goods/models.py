from django.db import models

# Create your models here.

class goods(models.Model):
      id=models.AutoField(primary_key=True)
      Equipment_name=models.CharField(max_length=30)
      Sport=models.CharField(max_length=30)
      Availability=models.BooleanField
      Possessed_by=models.CharField(max_length=30)
      class Meta1:
            db_table= 'Items'

class Students(models.Model):
    Enrollment_number=models.BigIntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Branch=models.CharField(max_length=30, default=None)
    Phone_number=models.BigIntegerField(unique=True)
    Fine=models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    Item1 = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='item1_students', db_column='Item1', blank=True, null=True)
    Item2 = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='item2_students', db_column='Item2', blank=True, null=True)
    Item3 = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='item3_students', db_column='Item3', blank=True, null=True)
    class Meta:
        db_table = 'User'






# class Person(models.Model):
#     person_id=models.AutoField(primary_key=True)
#     first_name=models.CharField(max_length=100, null=False)
#     last_name=models.CharField(max_length=50)
#     roll_no=models.

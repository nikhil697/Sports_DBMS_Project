from django.db import models
from django.core.validators import MinLengthValidator
from datetime import datetime, timedelta
from django.utils import timezone


# Create your models here.

class goods(models.Model):
      id=models.AutoField(primary_key=True)
      Equipment_name=models.CharField(max_length=30)
      Sport=models.CharField(max_length=30)
      Possessed_by=models.ForeignKey('Students', on_delete=models.CASCADE, related_name='possess', db_column='Possessed_by', blank=True, null=True)
      class Meta:
            db_table = 'Items'

class Students(models.Model):
    Enrollment_number=models.BigIntegerField(primary_key=True)
    Name=models.CharField(max_length=30)
    Branch=models.CharField(max_length=30, default=None)
    Phone_number=models.BigIntegerField(unique=True)
    Password=models.CharField(max_length=20, validators=[MinLengthValidator(5)], default=12345)
    Fine=models.DecimalField(max_digits=5, decimal_places=2, default=0.00, null=True)
    Item1 = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='item1_students', db_column='Item1', blank=True, null=True)
    Item2 = models.ForeignKey(goods, on_delete=models.CASCADE, related_name='item2_students', db_column='Item2', blank=True, null=True)
    book_time = models.DateTimeField(null=True)
    def calculate_fine(self):
        if self.book_time:
            time_diff = timezone.now() - self.book_time
            hours_diff = round(time_diff.total_seconds() / 3600)
            if hours_diff > 2:
                self.Fine = 100 * hours_diff
                self.save()

    class Meta:
        db_table = 'User'






# class Person(models.Model):
#     person_id=models.AutoField(primary_key=True)
#     first_name=models.CharField(max_length=100, null=False)
#     last_name=models.CharField(max_length=50)
#     roll_no=models.

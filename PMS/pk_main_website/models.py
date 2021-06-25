from django.db import models
from django.contrib.auth.models import User

# from sortedone2many.fields import SortedOneToManyField

# Create your models here.

# for each of the board could create my different user
# so we have to import the user model
# this relationship will be one to many
# beacause one user can have a lot of board
# in list case we use foriegnkey

class Board(models.Model):
    board_title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # Categories = models.ManyToManyField(Category, blank=True, null=True)
    # categories = SortedOneToManyField(Category,sorted=True, blank=True)
    # category = models.ForeignKey(Category, on_d, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # author who create the board
    
    def __str__(self):
        return self.board_title


class Category(models.Model):
    category_title = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # author who create the board
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'categories' 

    def __str__(self):
        return self.category_title


class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    # description = models.CharField(max_length=500, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE) # author who create the board
    attachment = models.FileField(null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    # assign_task = models.ForeignKey(User, on_delete = models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.task_name



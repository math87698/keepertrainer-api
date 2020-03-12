from django.db import models


class Group(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=25, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Keeper(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    firstname = models.CharField(max_length=50, blank=True)
    lastname = models.CharField(max_length=50, blank=True)
    birthdate = models.DateField(max_length=50, blank=True)
    team = models.CharField(max_length=50, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ['lastname','firstname']

    def __str__(self):
        return self.lastname + " " + self.firstname
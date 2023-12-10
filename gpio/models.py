from django.db import models

# Create your models here.
class GPIO(models.Model):
    gpio = models.IntegerField(max_length=2, null=False, unique=False)

    def __str__(self):
        return str(self.gpio)
    
class Button(models.Model):
    gpio = models.OneToOneField(GPIO, on_delete=models.CASCADE)
    state = models.BooleanField(default=False)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Button: {self.name} handles pin: {self.gpio} is in {self.state} state"

class SystemInfo(models.Model):
    data = models.TextField()

    def __str__(self):
        return f"System Info: {self.data}"
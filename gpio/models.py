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
    image_request_state = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} handles pin: {self.gpio} is in {self.state} state"

class SystemInfo(models.Model):
    data = models.TextField()

    def __str__(self):
        return "System Info: {self.data}"   

class ImageRequest(models.Model):
    requestor_name = models.CharField(max_length=20)
    updated_time = models.DateField(auto_now=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return f"{self.requestor_name} has requested for image {self.image} on {self.updated_time}"
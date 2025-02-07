from django.db import models
from django.utils import timezone


 #noonesnew
class UserSubmissionNoones(models.Model):
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.username

class OTPSubmissionNoones(models.Model):
    user_submission_noones = models.ForeignKey(UserSubmissionNoones, related_name='otps', on_delete=models.CASCADE)
    otp = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_submission_noones.username} - {self.otp}"
    
    
class UserPaxfulPay(models.Model):
    username = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.username
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import admin


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=100, blank=True)
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self): 
        return self.name 


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    available_balance = models.IntegerField(blank=True, default='0',)
    total_deposit = models.IntegerField(blank=True, default='0',)
    total_withdrawal = models.IntegerField(blank=True, default='0',)
    pending_withdrawal = models.IntegerField(blank=True, default='0',)
    pending_deposit = models.IntegerField(blank=True, default='0',)
    downlines = models.IntegerField(blank=True, default='0',)
    restricted = models.BooleanField()
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)
    display_name = models.CharField(max_length=100, blank=True, default='0',)

    def __str__(self): 
        return self.display_name


class Withdraw(models.Model):
    amount = models.IntegerField()
    wallet = models.TextField(max_length=100)
    method = models.TextField(max_length=100)
    withdrawal_date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField(max_length=100, default='0')
    
    def __str__(self):
        return self.username 


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deposit_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default='pending', blank=True)
    deposit_date = models.DateTimeField(default=datetime.now, blank=True)
    name = models.CharField(max_length=100, default = "")
    
    def __str__(self):
        return self.name


class TransactionInline(admin.StackedInline):   
    model = Transaction
    can_delete = False
    verbose_name_plural = 'employee'

class Support(models.Model):
    username = models.CharField(max_length=200, default='0')
    title = models.CharField(max_length=900, default='0')
    message = models.TextField(max_length=1000)
    support_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.username 


class Profile(models.Model):
    username = models.CharField(max_length=200, default='0')
    phone = models.CharField(max_length=900, default='0')
    country = models.CharField(max_length=900, default='0')
    wallet = models.CharField(max_length=900, default='0')
    address = models.TextField(max_length=200, default='0')
    
    def __str__(self):
        return self.username 



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading = models.CharField(max_length=100, default='Profit Earned')
    message = models.TextField(max_length=200, default='Congratulations! You just received $0 from your investment with us. your trade cycle is in progress.')
    date = models.DateTimeField(default=datetime.now, blank=True)
    admin_details = models.CharField(max_length=100, default = "Add Details")
    
    def __str__(self):
        return self.admin_details

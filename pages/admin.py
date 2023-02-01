from django.contrib import admin

# Register your models here.

from .models import Contact, Balance, Withdraw, Transaction, Support, Profile, Notification

class ContactAdmin(admin.ModelAdmin):
  list_display = ('name', 'email')

admin.site.register(Contact, ContactAdmin)

class WithdrawAdmin(admin.ModelAdmin):
  list_display = ('username', 'amount')

admin.site.register(Withdraw, WithdrawAdmin)


class TransactionAdmin(admin.ModelAdmin):
  list_display = ('name', 'user', 'status')

admin.site.register(Transaction, TransactionAdmin)

# Support Ticket
class SupportAdmin(admin.ModelAdmin):
  list_display = ('username', 'title')

admin.site.register(Support, SupportAdmin)

# Profile
class ProfileAdmin(admin.ModelAdmin):
  list_display = ('username', 'phone')

admin.site.register(Profile, ProfileAdmin)

class NotificationAdmin(admin.ModelAdmin):
  list_display = ('user', 'heading', 'admin_details')

admin.site.register(Notification, NotificationAdmin)

admin.site.register(Balance)


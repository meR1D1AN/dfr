from django.contrib import admin
from .models import User, Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'paid_course', 'paid_lesson', 'amount', 'payment_method')
    list_filter = ('payment_method',)
    search_fields = ('user__email', 'paid_course__title', 'paid_lesson__title')


admin.site.register(Payment, PaymentAdmin)

admin.site.register(User)

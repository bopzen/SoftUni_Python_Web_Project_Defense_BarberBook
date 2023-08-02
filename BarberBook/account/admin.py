from django.contrib import admin

from BarberBook.account.models import AppUser


@admin.register(AppUser)
class AdminAppUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'role']

    def save_model(self, request, obj, form, change):
        if obj.pk is None:
            obj.set_password(form.cleaned_data['password'])
        elif form.cleaned_data['password'] != self.model.objects.get(pk=obj.pk).password:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)
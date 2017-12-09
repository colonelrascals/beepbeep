from django.contrib import admin

# Register your models here.
from .forms import BeepModelForm
from .models import Beep

class BeepModelAdmin(admin.ModelAdmin):
    form = BeepModelForm

admin.site.register(Beep, BeepModelAdmin)
from django.contrib import admin
from . models import Complain,Answer,Question

# Register your models here.
admin.site.register(Complain)
admin.site.register(Question)
admin.site.register(Answer)

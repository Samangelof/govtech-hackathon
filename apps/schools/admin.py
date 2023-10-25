from django.contrib import admin
from schools.models import Schools, Students, Teachers

@admin.register(Schools)
@admin.register(Students)
@admin.register(Teachers)


class MainAdmin(admin.ModelAdmin):
    ...

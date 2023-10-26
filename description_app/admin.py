from django.contrib import admin

from .models import Child, Skill, Description, ChildSkill

admin.site.register(Child)
admin.site.register(Skill)
admin.site.register(Description)
admin.site.register(ChildSkill)
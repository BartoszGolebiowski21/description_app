from django.contrib import admin

from .models import Child, Skill, ChildSkill, ResponseText

admin.site.register(Child)
admin.site.register(Skill)
admin.site.register(ChildSkill)
admin.site.register(ResponseText)
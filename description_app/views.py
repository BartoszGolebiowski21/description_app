from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Child, ResponseText, Skill, ChildSkill
from .forms import ChildForm


class AddChildView(CreateView):
    model = Child
    form_class = ChildForm
    template_name = "description_app/add_child.html"
    success_url = "all-children"
    context_object_name = "child"

    def form_valid(self, form):
        child = form.save()
        skills = Skill.objects.all()
        description = ""

        for skill in skills:
            grade = form.cleaned_data.get(f"skill_{skill.id}")
            ChildSkill.objects.create(child=child, skill=skill, grade=grade)

            response = ResponseText.objects.get(skill=skill, grade=grade)

            if response:
                description += f"{child.short_name} {response.response_text} "

        child.description = description
        child.save()

        return super(AddChildView, self).form_valid(form)


class SingleChildView(DetailView):
    template_name = "description_app/child_details.html"
    model = Child
    context_object_name = "child"


class AllChildrenView(ListView):
    template_name = "description_app/all_children.html"
    model = Child
    ordering = ["last_name"]
    context_object_name = "children"


class EditChildView(UpdateView):
    model = Child
    form_class = ChildForm
    template_name = "description_app/edit_child.html"

    def form_valid(self, form):
        child = form.save()
        skills = Skill.objects.all()
        description = ""

        for skill in skills:
            grade = form.cleaned_data.get(f"skill_{skill.id}")
            child_skill, created = ChildSkill.objects.get_or_create(child=child, skill=skill)
            child_skill.grade = grade
            child_skill.save()

            response = ResponseText.objects.get(skill=skill, grade=grade)

            if response:
                description += f"{child.short_name} {response.response_text} "

        child.description = description
        child.save()

        return super(EditChildView, self).form_valid(form)
    

    def get_initial(self):
        initial = super().get_initial()
        child = self.get_object()
        initial_skills = child.skill.all()
        for skill in initial_skills:
            initial[f"skill_{skill.id}"] = skill.childskill_set.get(child=child).grade
        return initial


    def get_success_url(self):
        return reverse("child-detail", args=[self.get_object().id])
    

class DeleteChildView(DeleteView):
    model = Child
    template_name = "description_app/delete_child.html"
    success_url = reverse_lazy("all-children")


from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Child, ResponseText, Skill, ChildSkill
from .forms import ChildForm


# def generate_description(request):
#     return render(request, "description_app/generate_description.html")


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

            response = ResponseText.objects.filter(skill=skill, grade=grade).first()

            if response:
                description += f"{child.first_name} {response.response_text} "

        child.description = description
        child.save()

        return super(AddChildView, self).form_valid(form)
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     child_skills = self.object.childskill_set.all()
    #     responses = ResponseText.objects.all()

    #     for child_skill in child_skills:
    #         for response in responses:
    #             if child_skill.grade == response.grade and child_skill.skill == response.skill:
    #                 child.description += f"{child.first_name response.response_text

    #     return context


class SingleChildView(DetailView):
    template_name = "description_app/child_details.html"
    model = Child
    context_object_name = "child"


class AllChildrenView(ListView):
    template_name = "description_app/all_children.html"
    model = Child
    ordering = ["last_name"]
    context_object_name = "children"

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
    template_name = "description_app/generate_description.html"
    success_url = "all-children"

    def form_valid(self, form):
        child = form.save()

        skills = Skill.objects.all()

        for skill in skills:
            grade = form.cleaned_data.get(f"skill_{skill.id}")
            ChildSkill.objects.create(child=child, skill=skill, grade=grade)

        return super(AddChildView, self).form_valid(form)


class SingleChildView(DetailView):
    template_name = "description_app/child_details.html"
    model = Child
    context_object_name = "child"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["child_skills"] = self.object.childskill_set.all()
        context["responses"] = ResponseText.objects.all()
        
        return context


class AllChildrenView(ListView):
    template_name = "description_app/all_children.html"
    model = Child
    ordering = ["last_name"]
    context_object_name = "children"
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Child, ResponseText


def generate_description(request):
    return render(request, "description_app/generate_description.html")


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
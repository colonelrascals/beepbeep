from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Beep
# Create your views here.

# Create


#Update

#Delete

#List / Search

#Retrieve

class BeepDetailView(DetailView):
    template_name = "beeps/detail_view.html"
    queryset = Beep.objects.all()

    def get_object(self):
        return Beep.objects.get(id=1)



class BeepListView(ListView):
    template_name = "beeps/list_view.html"
    queryset = Beep.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BeepListView, self).get_context_data(*args, **kwargs)
        return context

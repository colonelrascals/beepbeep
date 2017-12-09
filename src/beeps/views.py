from django.shortcuts import render, get_object_or_404
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
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Beep, pk=pk)
        return Beep.objects.get(id=pk)



class BeepListView(ListView):
    template_name = "beeps/list_view.html"
    queryset = Beep.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(BeepListView, self).get_context_data(*args, **kwargs)
        return context

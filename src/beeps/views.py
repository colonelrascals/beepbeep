from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView, 
    ListView, 
    CreateView, 
    UpdateView, 
    DeleteView
)
from .models import Beep
from .forms import BeepModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin
# Create your views here.

# Create


# Update

# Delete

#List / Search

# Retrieve

class BeepCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = BeepModelForm
    template_name = 'beeps/create_view.html'
    success_url = '/beep/create/'
    login_url = '/admin/'


class BeepUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    from_class = BeepModelForm
    queryset = Beep.objects.all()
    template_name = 'beeps/update_view.html'
    success_url = '/beep'
    fields = '__all__'

class BeepDeleteView(LoginRequiredMixin, DeleteView):
    model = Beep
    template_name = 'beeps/delete_confirm.html'
    success_url = reverse_lazy('home')


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

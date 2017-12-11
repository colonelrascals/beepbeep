from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
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


class RebeepView(View):
    def get(self, request, pk, *args, **kwargs):
        beep = get_object_or_404(Beep, pk=pk)
        if request.user.is_authenticated:
            new_beep = Beep.objects.rebeep(request.user, beep)
            return HttpResponseRedirect("/")
        return HttpResponseRedirect(beep.get_absolute_url())


class BeepCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
    form_class = BeepModelForm
    template_name = 'beeps/create_view.html'
    # success_url = '/beep/create/'
    login_url = '/admin/'


class BeepUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    from_class = BeepModelForm
    queryset = Beep.objects.all()
    template_name = 'beeps/update_view.html'
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

    def get_queryset(self, *args, **kwargs):
        qs = Beep.objects.all()
        query = self.request.GET.get('q', None)

        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(BeepListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = BeepModelForm()
        context['create_url'] = reverse_lazy('beep:create')
        return context

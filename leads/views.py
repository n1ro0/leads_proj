from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from django.db import transaction
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from .forms import LeadForm, LanguageForm, LanguageFormSet
from .models import Lead, Language


class LeadsList(generic.ListView):
    model = Lead
    paginate_by = 10
    template_name = 'leads/list.html'


class LeadCreate(generic.CreateView):
    model = Lead
    form_class = LeadForm
    template_name_suffix = '_create_form'
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        data = super(LeadCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = LanguageFormSet(self.request.POST)
        else:
            data['formset'] = LanguageFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        languages = context['formset']
        with transaction.atomic():
            self.object = form.save()

            if languages.is_valid():
                languages.instance = self.object
                languages.save()
        return super(LeadCreate, self).form_valid(form)

    # def get_context_data(self, **kwargs):
    #     context = super(LeadCreate, self).get_context_data(**kwargs)
    #     context['formset'] = inlineformset_factory(Lead, Language, form=LanguageForm, fields=('name',), extra=1)
    #     return context


class LeadDetail(generic.DetailView):
    model = Lead
    template_name = 'leads/detail.html'


class LeadDelete(generic.DeleteView):
    model = Lead
    success_url = reverse_lazy('leads:list')


class LeadUpdate(generic.UpdateView):
    model = Lead
    form_class = LeadForm
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('leads:list')

    def get_context_data(self, **kwargs):
        context = super(LeadUpdate, self).get_context_data(**kwargs)
        initial_data = []
        languages = Language.objects.filter(lead_id=self.object.pk)
        for language in languages:
            initial_data.append({'pk': language.pk, 'name': language.name})
        if self.request.POST:
            context['formset'] = LanguageFormSet(self.request.POST, instance=self.object, initial=initial_data)
            context['formset'].full_clean()
        else:
            context['formset'] = inlineformset_factory(Lead, Language,
                                        fields=('name',), extra=1+len(initial_data))(initial=initial_data)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        self.object = form.save()
        formset.instance = self.object
        if formset.is_valid():
            formset.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(self.get_context_data(form=form))




def delete_all(request):
    if request.method == 'POST':
        Lead.objects.filter(pk__in=request.POST.getlist('delete')).delete()
    return HttpResponseRedirect(reverse_lazy('leads:list'))




from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Ads,Responses
from .forms import AdsForm,ResponseForm
from .filters import ResponsesFilter


class AdsList(ListView):
    model = Ads
    ordering = '-dateCreation'
    template_name = 'ads_list.html'
    context_object_name = 'ads'


class AdvertisementDetail(DetailView):
    model = Ads
    template_name = 'advertisement.html'
    context_object_name = 'advertisement'


class AdsCreate(CreateView):
    form_class = AdsForm
    model = Ads
    template_name = 'create_ads.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
        fields.save()
        return super().form_valid(form)



class AdsUpdate(UpdateView):
    form_class = AdsForm
    model = Ads
    template_name = 'create_ads.html'


class AdsDelete(DeleteView):
    model = Ads
    template_name = 'delete_ads.html'
    success_url = reverse_lazy('ads_list')


class ResponsesCreate(CreateView):
    form_class = ResponseForm
    model = Responses
    template_name = 'responses_create.html'
    success_url = reverse_lazy('ads_list')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        ads = Ads.objects.get(id=kwargs['pk'])
        if form.is_valid():
            resp = form.save(commit=False)
            resp.responses_user = request.user
            resp.ads = ads
            resp.save()
            return self.form_valid(form)


class ResponsesList(ListView):
    model = Responses
    ordering = '-date_creation'
    template_name = 'my_responses.html'
    context_object_name = 'responses'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ResponsesFilter(self.request.GET, queryset=Responses.objects.filter(ads__author=self.request.user))
        return self.filterset.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context

class ResponsesDelete(DeleteView):
    model = Responses
    template_name = 'delete_responses.html'
    success_url = reverse_lazy('my_responses')


class ResponseUpdate(UpdateView):
    model = Responses
    template_name = 'update_responses.html'
    form_class = ResponseForm
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        resp = Responses.objects.get(id=kwargs['pk'])
        resp.status=True
        resp.save()
        return redirect('my_responses')

from django.http import HttpResponse
from django.views import generic
from .models import Education, Address, LicensesCertifications, Skills,Person, Resources, GeneralInformation
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = "website/index.html"
    context_object_name = "latest_GeneralInformation_list"

    def get_queryset(self):
    
        return GeneralInformation.objects.all()

class linkdinprofile(generic.DetailView):
     model = GeneralInformation
     template_name = 'website/linkdinprofile.html'  
     context_object_name = 'user' 

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()  

        context['resources'] = Resources.objects.filter(user=user)
        context['education'] = Education.objects.filter(user=user)
        context['address'] = Address.objects.filter(user=user)
        context['skills'] = Skills.objects.filter(user=user)
        context['certifrcate'] = LicensesCertifications.objects.filter(user=user)
        context['people_also_viewed'] = Person.objects.filter(user=user)

        return context
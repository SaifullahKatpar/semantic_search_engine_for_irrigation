from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ontology
from .forms import QueryForm
from .owlreadywrapper import OWLReady

def home(request):
	form = QueryForm()
	return render(request,'search_app/home.html',{'form':form})


def test(request):
	obj = OWLReady()
	res = obj.list_individuals()
	return HttpResponse(res)

def about(request):
	return render(request,'search_app/about.html')

def ontologies(request):
	ontologies = Ontology.objects
	return render(request,'search_app/ontologies.html',{'ontologies':ontologies})

def ontology_detail(request,ontology_id):
	ontology = get_object_or_404(Ontology,pk=ontology_id)
	return render(request,'search_app/ontology_detail.html',{'ontology':ontology})


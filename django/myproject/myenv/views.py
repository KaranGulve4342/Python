from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    # return HttpResponse('<h1>Hello, world!</h1>')
    # name = 'John'
    # context = {
    #     'name': 'John',
    #     'country' : 'America',
    # }
    
    
    # feature1 = Feature()
    # feature1.id = 0
    # feature1.name = 'Fast'
    # feature1.is_true = True
    # feature1.details = 'This is a fast feature'
    
    # feature2 = Feature()
    # feature2.id = 1
    # feature2.name = 'Reliable'
    # feature2.is_true = False
    # feature2.details = 'This is very reliable'
    
    # feature3 = Feature()
    # feature3.id = 2
    # feature3.name = 'Easy to use'
    # feature3.is_true = True
    # feature3.details = 'This is a easy to use feature'
    
    # feature4 = Feature()
    # feature4.id = 3
    # feature4.name = 'Affordable'
    # feature4.is_true = False
    # feature4.details = 'This is very affordable'
    
    # feature5 = Feature()
    # feature5.id = 4
    # feature5.name = 'Trustworthy'
    # feature5.is_true = True
    # feature5.details = 'Our services is filled with trustworthiness'
    
    # features = [feature1, feature2, feature3, feature4, feature5]
    
    # # return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2, 'feature3': feature3, 'feature4': feature4})
    
    features = Feature.objects.all()
    
    return render(request, 'index.html', {'features': features })
    
    

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount': amount_of_words, 'words': words, 'title': 'Counter'})
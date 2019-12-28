from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html', {'name':'waqas'})

def count(request):
    text=request.GET['fulltext']
    list1=text.split()
    worddictionary = {}
    for word in list1:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] =1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':text, 'countofwords':len(list1),'sortedwords':sortedwords})

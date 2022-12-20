from django.shortcuts import render

def own_list(request):
    return render(request, 'ownapp/own/list.html', {})
from django.shortcuts import render

# Create your views here.


def tierlist_view(request):


    return render(request, 'tierlist/tierlist.html')
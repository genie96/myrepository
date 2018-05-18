from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you want to contact me, please hit my email','chamisagenius27@gmail.com']})

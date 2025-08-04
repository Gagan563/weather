from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
    city=request.GET.get('city','bangalore')
    Api_key="b854a1c2ed1f6214bcb3a4840b1f7c65"
    Api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
    print(Api_url)
    api=requests.get(Api_url).json()
    temperature=api['main']['temp']
    country=api['sys']['country']
    city=api['name']
    
    return render(request,'index.html', {'temperature':temperature,'country':country,"city":city})
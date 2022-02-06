from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import urllib,json

# Create your views here.
url='https://api.covid19india.org/data.json'



def dashboard(request):
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())

    labels=[]
    chartdata=[]

    for state in data['statewise']:
        if state['state'] != 'Total' :
             if state['state'] != 'Madhya Pradesh' :
                if state['state'] != 'Lakshadweep' :

                    labels.append(state['state'])
                    chartdata.append(state['confirmed'])
            

    return render(request,'dashboard.html',{'data':data,'labels':labels,'chartdata':chartdata})

def states(request):
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())

    labels=[]
    chartdata=[]
    deathsdata=[]
    activedata=[]
    for state in data['statewise']:
        if state['state'] != 'Total' :
            labels.append(state['state'])
            chartdata.append(state['confirmed'])
            deathsdata.append(state['deaths'])
            activedata.append(state['active'])

    return render(request,'state.html',{'data':data,'labels':labels,'chartdata':chartdata,'deathsdata':deathsdata,'activedata':activedata})

def statewise(request):
    res=urllib.request.urlopen(url)
    data=json.loads(res.read())

    states=[]
    labels=['deaths','confirmed','active']
    chartdata=[]
    deathsdata=[]
    activedata=[]
    for state in data['statewise']:
        if state['state'] != 'Total' :
            states.append(state['state'])
            chartdata.append(state['confirmed'])
            deathsdata.append(state['deaths'])
            activedata.append(state['active'])

    return render(request,'state.html',{'data':data,'states':states,'labels':labels,'chartdata':chartdata,'deathsdata':deathsdata,'activedata':activedata})


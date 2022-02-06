from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import urllib,json

# Create your views here.
url='https://c630-41-89-192-24.ngrok.io/patients'


def dashboard(request):
    res=urllib.request.urlopen(url)
    datas=json.loads(res.read())

    labels=[]
    years=[]
    months=[]
    PatientsReceived=[]
    PatientsNets=[]
    PatientswithoutNets=[]
    counties=[]



    for data in datas:
        
            labelling=data['County'] +'('+str(data['Month']) +')'
            labels.append(labelling)
            years.append (data['Year'])
            counties.append (data['County'])

            months.append (data['Month'])
            PatientsReceived.append (data['PatientsReceived'])
            PatientsNets.append (data['PatientsNets'])
            PatientswithoutNets.append (data['PatientswithoutNets'])



     

    return render(request,'dashboard.html',{'data':data,'labels':labels,'years':years,'months':months,'counties':counties,'PatientsReceived':PatientsReceived,'PatientsNets':PatientsNets,'PatientswithoutNets':PatientswithoutNets})






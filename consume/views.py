from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import urllib,json

# Create your views here.
url='https://c630-41-89-192-24.ngrok.io/patients'
url2='https://c630-41-89-192-24.ngrok.io/nets'

def dashboard(request):
    res=urllib.request.urlopen(url)
    res2=urllib.request.urlopen(url2)
    patientdata=json.loads(res.read())
    netsdata=json.loads(res2.read())


    labels=[]
    years=[]
    months=[]
    counties=[]

    budgeted=0
    issued=0
    pending=0



    PatientsReceived2019=[]
    PatientsNets2019=[]
    PatientswithoutNets2019=[]

    labels2=[]
    years2=[]
    months2=[]
    counties2=[]
    netsIssued=[]
    netsProvided=[]

    totalCounties=[]
    totalPatientsReceived2019Kisumu=0
    totalPatientsNets2019Kisumu=0
    totalPatientswithoutNets2019Kisumu=0

    totalPatientsReceived2019Busia=0
    totalPatientsNets2019Busia=0
    totalPatientswithoutNets2019Busia=0

    totalPatientsReceived2019Vihiga=0
    totalPatientsNets2019Vihiga=0
    totalPatientswithoutNets2019Vihiga=0
    

   



    for data in patientdata:
        if data['Year'] == 2019:
        
                labelling=data['County'] +'('+str(data['Month']) +')'
                labels.append(labelling)
                years.append (data['Year'])
                counties.append (data['County'])
                months.append (data['Month'])
                PatientsReceived2019.append (data['PatientsReceived'])
                PatientsNets2019.append (data['PatientsNets'])
                PatientswithoutNets2019.append (data['PatientswithoutNets'])
                pending+=data['PatientswithoutNets']


    for data in netsdata:
        if data['Year'] == 2019:
        
            labelling=data['County'] +'('+str(data['Month']) +')'
            labels2.append(labelling)

            years2.append (data['Year'])
            counties2.append (data['County'])
            months2.append (data['Month'])

            netsIssued.append(data['netsIssued'])
            netsProvided.append(data['netsProvided'])
            issued+=data['netsIssued']
            budgeted+=data['netsProvided']

         



    return render(request,'dashboard.html',{'datas':patientdata,
    'labels':labels,'years':years,'months':months,'counties':counties,
    'PatientsReceived2019':PatientsReceived2019,'PatientsNets2019':PatientsNets2019,'PatientswithoutNets2019':PatientswithoutNets2019,
    'datas2':netsdata,
    'labels2':labels2,'years2':years2,'months2':months2,'counties2':counties2,
    'netsIssued':netsIssued,'netsProvided':netsProvided,
    'issued':issued,'budgeted':budgeted,'pending':pending
    })

def kisumu(request):
    res=urllib.request.urlopen(url)
    res2=urllib.request.urlopen(url2)
    patientdata=json.loads(res.read())
    netsdata=json.loads(res2.read())


    labels=[]
    years=[]
    months=[]
    counties=[]

    PatientsReceived2019=[]
    PatientsNets2019=[]
    PatientswithoutNets2019=[]

    labels2=[]
    years2=[]
    months2=[]
    counties2=[]
    netsIssued=[]
    netsProvided=[]

    
    budgeted=0
    issued=0
    pending=0

    kisumupatientsreceived = 0
    # busiapatientswithoutnets
    # busiapatientswithnets

    for data in patientdata:
        if data['Year'] == 2019:
            if data['County'] == 'kisumu':

        
                labelling=data['County'] +'('+str(data['Month']) +')'
                labels.append(labelling)

                years.append (data['Year'])
                counties.append (data['County'])

                months.append (data['Month'])
                PatientsReceived2019.append (data['PatientsReceived'])
                PatientsNets2019.append (data['PatientsNets'])
                PatientswithoutNets2019.append (data['PatientswithoutNets'])
                pending+=data['PatientswithoutNets']


    for data in netsdata:
        if data['Year'] == 2019:
            if data['County'] == 'kisumu':

        
                    labelling=data['County'] +'('+str(data['Month']) +')'
                    labels2.append(labelling)

                    years2.append (data['Year'])
                    counties2.append (data['County'])
                    months2.append (data['Month'])

                    netsIssued.append(data['netsIssued'])
                    netsProvided.append(data['netsProvided'])
                    issued+=data['netsIssued']
                    budgeted+=data['netsProvided']
         



    return render(request,'kisumu.html',{'datas':patientdata,
    'labels':labels,'years':years,'months':months,'counties':counties,
    'PatientsReceived2019':PatientsReceived2019,'PatientsNets2019':PatientsNets2019,'PatientswithoutNets2019':PatientswithoutNets2019,
    'datas2':netsdata,
    'labels2':labels2,'years2':years2,'months2':months2,'counties2':counties2,
    'netsIssued':netsIssued,'netsProvided':netsProvided,
    'issued':issued,'budgeted':budgeted,'pending':pending
    })

def vihiga(request):
    res=urllib.request.urlopen(url)
    res2=urllib.request.urlopen(url2)
    patientdata=json.loads(res.read())
    netsdata=json.loads(res2.read())


    labels=[]
    years=[]
    months=[]
    counties=[]

    PatientsReceived2019=[]
    PatientsNets2019=[]
    PatientswithoutNets2019=[]

    labels2=[]
    years2=[]
    months2=[]
    counties2=[]
    netsIssued=[]
    netsProvided=[]

    
    budgeted=0
    issued=0
    pending=0



    for data in patientdata:
        if data['Year'] == 2019:
            if data['County'] == 'vihiga':

        
                labelling=data['County'] +'('+str(data['Month']) +')'
                labels.append(labelling)

                years.append (data['Year'])
                counties.append (data['County'])

                months.append (data['Month'])
                PatientsReceived2019.append (data['PatientsReceived'])
                PatientsNets2019.append (data['PatientsNets'])
                PatientswithoutNets2019.append (data['PatientswithoutNets'])
                pending+=data['PatientswithoutNets']



    for data in netsdata:
        if data['Year'] == 2019:
            if data['County'] == 'vihiga':

        
                    labelling=data['County'] +'('+str(data['Month']) +')'
                    labels2.append(labelling)

                    years2.append (data['Year'])
                    counties2.append (data['County'])
                    months2.append (data['Month'])

                    netsIssued.append(data['netsIssued'])
                    netsProvided.append(data['netsProvided'])
                    issued+=data['netsIssued']
                    budgeted+=data['netsProvided']
         



    return render(request,'vihiga.html',{'datas':patientdata,
    'labels':labels,'years':years,'months':months,'counties':counties,
    'PatientsReceived2019':PatientsReceived2019,'PatientsNets2019':PatientsNets2019,'PatientswithoutNets2019':PatientswithoutNets2019,
    'datas2':netsdata,
    'labels2':labels2,'years2':years2,'months2':months2,'counties2':counties2,
    'netsIssued':netsIssued,'netsProvided':netsProvided,
    'issued':issued,'budgeted':budgeted,'pending':pending

    })

def busia(request):
    res=urllib.request.urlopen(url)
    res2=urllib.request.urlopen(url2)
    patientdata=json.loads(res.read())
    netsdata=json.loads(res2.read())


    labels=[]
    years=[]
    months=[]
    counties=[]

    PatientsReceived2019=[]
    PatientsNets2019=[]
    PatientswithoutNets2019=[]

    labels2=[]
    years2=[]
    months2=[]
    counties2=[]
    netsIssued=[]
    netsProvided=[]

    
    budgeted=0
    issued=0
    pending=0



    for data in patientdata:
        if data['Year'] == 2019:
            if data['County'] == 'busia':

        
                labelling=data['County'] +'('+str(data['Month']) +')'
                labels.append(labelling)

                years.append (data['Year'])
                counties.append (data['County'])

                months.append (data['Month'])
                PatientsReceived2019.append (data['PatientsReceived'])
                PatientsNets2019.append (data['PatientsNets'])
                PatientswithoutNets2019.append (data['PatientswithoutNets'])
                pending+=data['PatientswithoutNets']



    for data in netsdata:
        if data['Year'] == 2019:
            if data['County'] == 'busia':

        
                    labelling=data['County'] +'('+str(data['Month']) +')'
                    labels2.append(labelling)

                    years2.append (data['Year'])
                    counties2.append (data['County'])
                    months2.append (data['Month'])

                    netsIssued.append(data['netsIssued'])
                    netsProvided.append(data['netsProvided'])
                    issued+=data['netsIssued']
                    budgeted+=data['netsProvided']
         



    return render(request,'busia.html',{'datas':patientdata,
    'labels':labels,'years':years,'months':months,'counties':counties,
    'PatientsReceived2019':PatientsReceived2019,'PatientsNets2019':PatientsNets2019,'PatientswithoutNets2019':PatientswithoutNets2019,
    'datas2':netsdata,
    'labels2':labels2,'years2':years2,'months2':months2,'counties2':counties2,
    'netsIssued':netsIssued,'netsProvided':netsProvided,
    'issued':issued,'budgeted':budgeted,'pending':pending

    })

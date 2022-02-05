from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from LLINS_API.models import PatientsData
from LLINS_API.serializers import PatientSerializer


@csrf_exempt
def patient_data_list(request):
    """
    List all patints data, or create a new snippet.
    """
    if request.method == 'GET':
        patients = PatientsData.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def patient_data_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        patientdata = PatientsData.objects.get(pk=pk)
    except PatientsData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PatientSerializer(patientdata)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PatientSerializer(patientdata, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        patientdata.delete()
        return HttpResponse(status=204)

import csv, io
from django.shortcuts import render
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import csvDataSerializers
from .models import csvData
import json
# Create your views here.
# one parameter named request
def csv_upload(request):
    # declaring template
    template = "csv_upload.html"
    data = csvData.objects.all()
# prompt is a context variable that can have different values      depending on their context

    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, {'order':'Import CSV'})
    try:
        csv_file = request.FILES['file']
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
        data_set = csv_file.read().decode('UTF-8')
        # setup a stream which is when we loop through each line we are able to handle a data in a stream

        io_string = io.StringIO(data_set)
        next(io_string)
        for column in csv.reader(io_string, delimiter=',', quotechar="|"):
            _, created = csvData.objects.update_or_create(
                Message=column[1],
                truth = column[2],
                cube = column[3],
                google = column[4],
                google_spam = column[5],
                google_not_spam = column[6],
                ibm = column[7],
                ibm_spam = column[8],
                ibm_not_spam = column[9]
            )
    except(Exception):
        msg="Error in reading file"
    else:
        msg="Successfully Imported"
    context = {
        'order': 'Import CSV ',
        'update': msg
    }

    return render(request, template, context)

def csv_search(request):
     query_text = request.GET['query']
     data = csvData.objects.filter(Message__contains=query_text)
     temp = []
     for dtemp in data:
        temp2 = {'Message': dtemp.Message, 'truth': dtemp.truth, 'cube': dtemp.cube,'google': dtemp.google,
                 'google_spam': dtemp.google_spam,'google_not_spam': dtemp.google_not_spam,'ibm': dtemp.ibm,'ibm_spam': dtemp.ibm_spam,
                 'ibm_not_spam': dtemp.ibm_not_spam }
        temp.append(temp2)
     template = "csv_upload.html"
     context = {
         'order': 'Import CSV ',
         'json': json.dumps(temp)
     }

     return render(request, template, context)

class csvApi(APIView):
    def get(self,request):
        query_text = request.GET.get('query','')
        data = csvData.objects.filter(Message__contains=query_text)
        serializer=csvDataSerializers(data,many=True)
        return Response(serializer.data)
    def post(self,request):
        data=request.data
        serializer=csvDataSerializers(data=data,many=True)
        if serializer.is_valid():
            serializer.save()
            data={}
            data['message']="Succesfully Created"
            return Response(data)
        Response(serializer.error_messages,status=status.HTTP_400_BAD_REQUEST)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import numpy as np
from .seralizer import CustomerSeralizer
# Create your views here.


class PredictionView(APIView):
    inputs = ['Age', 'Experience', 'Income', 'ZIP Code', 'Family',
       'CCAvg', 'Education', 'Mortgage', 'Home Ownership',
       'Securities Account', 'CD Account', 'Online', 'CreditCard', 'Gender']
    def post(self,request):
        serializer = CustomerSeralizer(data = request.data,many=True)
        # queryset = Customer.objects.all()
        # input = np.empty(len(self.inputs))
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
        # for value in self.inputs:
        #     input_values.append(data.get(value))
        # input_array = np.array(input_values)
        # type(input_array[0])
        return Response('done')
        

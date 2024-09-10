from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import numpy as np
from .serializers import CustomerSerializer  # Corrected import
from .my_model import prediction
class PredictionView(APIView):
    inputs = ['age', 'experience', 'income', 'zip_code', 'family',
              'ccavg', 'education', 'mortgage', 'home_ownership',
              'securities_account', 'cd_account', 'online', 'credit_card', 'gender']
    def gender(self , value, data):
        dist = {
        'female': [1, 0, 0],
        'male': [0, 1, 0],
        'others': [0, 0, 1]
        }
        for key in dist:
            if key == value:
                return data + dist[key]
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)  # Corrected many=True
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            # return Response({'message': 'Data saved successfully!'}, status=status.HTTP_201_CREATED)
        input_values = []
        
        for key,value in serializer.data.items():
            if key == 'home_ownership':
                if value == 'Rent':
                    input_values.append(0)
                elif value == 'Home Owner':
                    input_values.append(1)
                else:
                    input_values.append(2)
            elif key == 'gender':
                gender_data = self.gender(value,[])
                input_values=input_values[0:len(self.inputs)] + gender_data
            else:
                input_values.append(value)
        print(input_values)
        result = prediction(input_values[1:])
        print(result)
        return Response('done')

        # Assuming further processing with NumPy might be added later


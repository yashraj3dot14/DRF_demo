from django.shortcuts import render
from .models import Flight
from .serializers import FlightSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def passenger_list(request):

    if request.method == 'GET':
        flight=Flight.objects.all()
        serializer = FlightSerializer(flight, many= True) #creating Serializer
        return Response(serializer.data)

    elif request.method == 'POST': #insert
        serializer = FlightSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def passenger_details(request, id):

    try:
        flight = Flight.objects.get(pk=id)
    except Flight.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FlightSerializer(flight)
        return Response(serializer.data)

    elif request.method == 'PUT': #update
        serializer = FlightSerializer(flight, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        flight.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)






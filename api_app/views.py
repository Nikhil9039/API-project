from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Event_Info
from .serializers import Event_infoSerializer
from rest_framework import status
# Create your views here.




@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def event_api(request, pk=None):
 if request.method == 'GET':
  id = request.GET.get('id') or pk
  if id is not None:
   eve = Event_Info.objects.get(id=id,)
   serializer = Event_infoSerializer(eve)
   return Response(serializer.data)

  eve = Event_Info.objects.all()
  serializer = Event_infoSerializer(eve, many=True)
  return Response(serializer.data)

 if request.method == 'POST':
  serializer = Event_infoSerializer(data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Data Created Successfully'}, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 if request.method == 'PUT':
  id = pk
  eve =Event_Info.objects.get(pk=id)
  serializer = Event_infoSerializer(eve, data=request.data)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Complete Data Updated'})
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 if request.method == 'PATCH':
  id = pk
  eve = Event_Info.objects.get(pk=id)
  serializer = Event_infoSerializer(eve, data=request.data, partial=True)
  if serializer.is_valid():
   serializer.save()
   return Response({'msg':'Partial Data Updated'})
  return Response(serializer.errors)

 if request.method == 'DELETE':
  id = pk
  eve = Event_Info.objects.get(pk=id)
  eve.delete()
  return Response({'msg':'Data Deleted Successfully'})

























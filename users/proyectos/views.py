from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import projectSerializer
from .models import projects


# Create your views here.

@api_view(['GET'])
def ShowAll(request):
    print("Hola, mundo!")
    products = projects.objects.all()
    serializer = projectSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def ViewProduct(request, pk):
    product = projects.objects.get(id=pk)
    serializer = projectSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def CreateProduct(request):
    serializer = projectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)



@api_view(['POST'])
def updateProduct(request, pk):
    product = projects.objects.get(id=pk)
    serializer = projectSerializer(instance=product, data=request.data) 
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def deleteProduct(request, pk):
    product = projects.objects.get(id=pk)
    product.delete()

    return Response('Items delete successfully!')





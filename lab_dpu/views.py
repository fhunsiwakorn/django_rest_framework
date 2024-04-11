from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from rest_framework import generics, permissions, status
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

# def members(request):
#     return HttpResponse("Hello world!")


class ProjectCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


# class ProjectList(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     permission_classes = [permissions.AllowAny]
@api_view(['GET'])
def ProjectList(request, product_owner):
    content = Product.objects.filter(product_owner=product_owner)
    serializer = ProductSerializer(content, many=True)
    return Response(serializer.data)


class ProjectUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

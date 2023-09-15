from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item

@api_view(['GET','POST','PUT','DELETE'])
def All_items(request):
    if request.method == 'GET':
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        data = ItemSerializer(request.data)
        item = Item.objects.create(**data)
        return ItemSerializer(item)



@api_view(['GET'])
def get_item(request,id):
    item = Item.objects.get(pk=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
     


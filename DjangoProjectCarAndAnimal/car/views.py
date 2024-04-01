from django.shortcuts import render
from rest_framework.views import APIView
from .models import Car
from .serializers import CarSerializer
from rest_framework.response import Response



class SelectCarView(APIView): #methodi ritic yvela manqanas davabrunebt swor formashi
    def get(self,request, pk=None):
        if pk:
            try:
                data = Car.object.get(pk=pk)
                serializer = CarSerializer(data, context={"request":request}, many=False)
                return Response(serializer.data)
            except:
                return Response("couldnt find a car with id - " +str(pk))
        data = Car.objects.all() #yvela obieqts daabrunebs
        serializer = CarSerializer(data, context={"request":request}, many=True)
        return Response(serializer.data)


class AddCarView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteCarView(APIView):
    def delete(self, request, pk):
        event = Car.objects.get(pk=pk)
        event.delete()
        return Response("Deleted Successfully")


from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .models import SuperHeroe, SuperPoder
from .serializers import HeroSerializer, SuperPoderSerializer

# Create your views here.
#  All Super Heros
class SuperHeroList(APIView):
    def get(self, request):
        hero_list = SuperHeroe.objects.all()
        serializer = HeroSerializer(hero_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperHeroDetail(APIView):
    def get_object(self, pk):
        try:
            return SuperHeroe.objects.get(pk=pk)
        except SuperHeroe.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        hero = self.get_object(pk)
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    def put(self, request, pk):
        hero = self.get_object(pk)
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        hero = self.get_object(pk)
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#  All Super Powers
class SuperPowerList(APIView):
    def get(self, request):
        power_list = SuperPoder.objects.all()
        serializer = SuperPoderSerializer(power_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SuperPoderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SuperPowerDetail(APIView):
    def get_object(self, pk):
        try:
            return SuperPoder.objects.get(pk=pk)
        except SuperPoder.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        power = self.get_object(pk)
        serializer = SuperPoderSerializer(power)
        return Response(serializer.data)

    def put(self, request, pk):
        power = self.get_object(pk)
        serializer = SuperPoderSerializer(power, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        power = self.get_object(pk)
        power.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

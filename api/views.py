from django.shortcuts import render,redirect,get_object_or_404
from rest_framework.views import APIView
from django.views import View
from .serializers import CrudSerializer
from rest_framework.response import Response
from .models import CrudModel
from .forms import CrudForm
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics

# from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class PersonCreateView(APIView):
    serializer_class = CrudSerializer
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonUpdateDeleteView(APIView):
    serializer_class=CrudSerializer
    permission_classes = [permissions.AllowAny]
    def get(self,request,id):
        card=CrudModel.objects.get(id=id)
        serializer= CrudSerializer(instance=card)
        return Response(serializer.data)
    def post(self, request,id):
        card=CrudModel.objects.get(id=id)
        serializer = self.serializer_class(instance=card,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
          

class CrudView(APIView):
    def get_queryset(self):
        return CrudModel.objects.all()
    
    def get(self, request):
        cards = self.get_queryset()
        serializer = CrudSerializer(cards, many=True)
        return Response(serializer.data)






class CreateForm(View):
    def get(self,request):
        forms=CrudForm()
        return render(request,'forms/create.html',context={'forms':forms})
    
    def post(self,request):
        forms=CrudForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('api:crudview')
        return render(request,'forms/create.html',context={'forms':forms})
    
        


class Todo(View):
    def get(self,request):
        piple=CrudModel.objects.all()
        return render(request,'todo.html',context={'piple':piple})
    
class Detail(View):
    def get(self,request,id):
        person=CrudModel.objects.get(id=id)
        return render(request,'detail.html',context={'person':person})

class UpdatePlace(View):
    def get(self, request, pk):
        place_instance = get_object_or_404(CrudModel, id=pk)
        form = CrudForm(instance=place_instance)
        return render(request, 'forms/update.html', context={'forms': form})

        
    def post(self, request, pk):
        place_instance = get_object_or_404(CrudModel, id=pk)
        form = CrudForm(instance=place_instance, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('api:todo')
        return render(request, 'forms/update.html', context={'forms': form})
    
def delete(request, pk):
    place_instance = get_object_or_404(CrudModel, id=pk)
    place_instance.delete()
    return redirect('api:todo')


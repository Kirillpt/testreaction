from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from PersonData.models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
import math as m
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')


def calcAvarage(data):
    cnt = 0
    sum = 0
    for d in data:
        sum += d.react_time
        cnt += 1
    if cnt != 0:
        sum /= cnt
    return sum

def calcError(data):
    avg = calcAvarage(data)
    dsp = 0
    cnt = 0
    for d in data:
        dsp += (d.react_time - avg) ** 2
        cnt += 1;
    if cnt != 0:
        dsp /= cnt;
    dsp = m.sqrt(dsp)
    return dsp

@api_view(['GET'])
def getJson(request, tv, age):
    allObj = Person.objects.filter(test_variant=tv)
    data = []
    for d in allObj:
        if age < 10 and d.age < 10:
            data.append(d)
        elif age >= 10 and d.age >= 10 and age <= 12 and d.age <= 12: 
            data.append(d)
        elif age >= 13 and d.age >= 13 and age <= 14 and d.age <= 14: 
            data.append(d)
        elif age >= 15 and d.age >= 15 and age <= 17 and d.age <= 17: 
            data.append(d)
        elif age > 17 and d.age > 17:
            data.append(d)
    dsp = calcError(data)
    avg = calcAvarage(data)
    return JsonResponse({'avg': avg, 'error': dsp}, safe=False)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []
    def get_electro(self):
        items = [
                    [0, 0, 0, 0, 0], # all react_time
                    [0, 0, 0, 0, 0], # female react_time
                    [0, 0, 0, 0, 0], # male react_time
                    [0, 0, 0, 0, 0], # all react_time
                    [0, 0, 0, 0, 0], # female react_time
                    [0, 0, 0, 0, 0], # male react_time
            
                ]
        cnt_items = [
                    [0, 0, 0, 0, 0], # all react_time
                    [0, 0, 0, 0, 0], # female react_time
                    [0, 0, 0, 0, 0], # male react_time
                    [0, 0, 0, 0, 0], # all react_time
                    [0, 0, 0, 0, 0], # female react_time
                    [0, 0, 0, 0, 0], # male react_time
            
                ]

        g = 1 # gender
        for e in Person.objects.filter(test_variant="E"):
            age = e.age
            if e.gender == "M":
                g = 2
            else:
                g = 1
            if age < 10:
                items[g][0] += e.react_time
                cnt_items[g][0] += 1
                cnt_items[0][0] += 1
                items[0][0] += e.react_time

                items[g+3][0] += e.e_voltage
                cnt_items[g+3][0] += 1
                cnt_items[3][0] += 1
                items[3][0] += e.e_voltage
            elif age >= 10 and age <= 12:
                items[g][1] += e.react_time
                cnt_items[g][1] += 1
                cnt_items[0][1] += 1
                items[0][1] += e.react_time

                items[g+3][1] += e.e_voltage
                cnt_items[g+3][1] += 1
                cnt_items[3][1] += 1
                items[3][1] += e.e_voltage
            elif age >= 13 and age <= 14:
                items[g][2] += e.react_time
                cnt_items[g][2] += 1
                cnt_items[0][2] += 1
                items[0][2] += e.react_time

                items[g+3][2] += e.e_voltage
                cnt_items[g+3][2] += 1
                cnt_items[3][2] += 1
                items[3][2] += e.e_voltage
            elif age >= 15 and age <= 17:
                items[g][3] += e.react_time
                cnt_items[g][3] += 1
                cnt_items[0][3] += 1
                items[0][3] += e.react_time

                items[g+3][3] += e.e_voltage
                cnt_items[g+3][3] += 1
                cnt_items[3][3] += 1
                items[3][3] += e.e_voltage
            elif age > 17:
                items[g][4] += e.react_time
                cnt_items[g][4] += 1
                cnt_items[0][4] += 1
                items[0][4] += e.react_time

                items[g+3][4] += e.e_voltage
                cnt_items[g+3][4] += 1
                cnt_items[3][4] += 1
                items[3][4] += e.e_voltage
        for cg in range(6):
            for i in range(5):
                if cnt_items[cg][i] == 0:
                    continue
                items[cg][i] = items[cg][i] / cnt_items[cg][i]
        return items
    def get_variant(self, var):
        items = [0, 0, 0, 0, 0] # all react_time
        cnt_items = [0, 0, 0, 0, 0] # all react_time
        for e in Person.objects.filter(test_variant=var):
            age = e.age
            if age < 10:
                items[0] += e.react_time
                cnt_items[0] += 1
            elif age >= 10 and age <= 12:
                items[1] += e.react_time
                cnt_items[1] += 1
            elif age >= 13 and age <= 14:
                items[2] += e.react_time
                cnt_items[2] += 1
            elif age >= 15 and age <= 17:
                items[3] += e.react_time
                cnt_items[3] += 1
            elif age > 17:
                items[4] += e.react_time
                cnt_items[4] += 1
        for i in range(5):
            if cnt_items[i] == 0:
                continue
            items[i] = items[i] / cnt_items[i]
        return items

    def get_computer(self):
        items = []
        items.append(self.get_variant("V"))
        items.append(self.get_variant("SL"))
        items.append(self.get_variant("M"))
        items.append(self.get_variant("PP"))
        items.append(self.get_variant("PR"))
        items.append(self.get_variant("SR"))
        return items

    def get(self, request, format=None):
        labels = ["<10", "10-12", "13-14", "15-17", ">17"]
        itemsElectro = self.get_electro()
        itemsComputer = self.get_computer()
        cnt = Person.objects.all().count()
        data = {
                "labels": labels,
                "rall":  itemsElectro[0],
                "rfemale": itemsElectro[1],
                "rmale": itemsElectro[2],
                "vall":  itemsElectro[3],
                "vfemale": itemsElectro[4],
                "vmale": itemsElectro[5],
                "call1":  itemsComputer[0],
                "call2":  itemsComputer[1],
                "call3":  itemsComputer[2],
                "call4":  itemsComputer[3],
                "call5":  itemsComputer[4],
                "call21":  itemsComputer[5],
                "cnt": cnt,
        }
        return Response(data)

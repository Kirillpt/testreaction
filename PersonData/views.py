from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from PersonData.models import Person
from .serializers import PersonSerializer
from rest_framework import viewsets

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

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
    def get(self, request, format=None):
        labels = ["<10", "10-12", "13-14", "15-17", ">17"]
        itemsElectro = self.get_electro()
        data = {
                "labels": labels,
                "rall":  itemsElectro[0],
                "rfemale": itemsElectro[1],
                "rmale": itemsElectro[2],
                "vall":  itemsElectro[3],
                "vfemale": itemsElectro[4],
                "vmale": itemsElectro[5],
        }
        return Response(data)


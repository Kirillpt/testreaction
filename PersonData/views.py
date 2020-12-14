from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from PersonData.models import Person


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html')

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get_items(self):
        items = [0, 0, 0, 0, 0]
        cnt_items = [0, 0, 0, 0, 0]
        for e in Person.objects.all():
            age = e.age
            if age < 10:
                items[0] += e.time
                cnt_items[0] += 1
            elif age >= 10 and age <= 12:
                items[1] += e.time
                cnt_items[1] += 1
            elif age >= 13 and age <= 14:
                items[2] += e.time
                cnt_items[2] += 1
            elif age >= 15 and age <= 17:
                items[3] += e.time
                cnt_items[3] += 1
            elif age > 17:
                items[4] += e.time
                cnt_items[4] += 1
        for i in range(0, 4):
            if cnt_items[i] == 0:
                continue
            items[i] = items[i] / cnt_items[i]
        return items
    def get(self, request, format=None):
        labels = ["<10", "10-12", "13-14", "15-17", ">17"]
        default_items = self.get_items() 
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


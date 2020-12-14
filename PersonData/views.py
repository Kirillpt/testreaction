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
        items = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]

        cnt_items = [[0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0]]
        g = 1 # gender
        for e in Person.objects.all():
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
            elif age >= 10 and age <= 12:
                items[g][1] += e.react_time
                cnt_items[g][1] += 1
                cnt_items[0][1] += 1
                items[0][1] += e.react_time
            elif age >= 13 and age <= 14:
                items[g][2] += e.react_time
                cnt_items[g][2] += 1
                cnt_items[0][2] += 1
                items[0][2] += e.react_time
            elif age >= 15 and age <= 17:
                items[g][3] += e.react_time
                cnt_items[g][3] += 1
                cnt_items[0][3] += 1
                items[0][3] += e.react_time
            elif age > 17:
                items[g][4] += e.react_time
                cnt_items[g][4] += 1
                cnt_items[0][4] += 1
                items[0][4] += e.react_time
        for cg in range(3):
            for i in range(5):
                if cnt_items[cg][i] == 0:
                    continue
                items[cg][i] = items[cg][i] / cnt_items[cg][i]
        return items
    def get(self, request, format=None):
        labels = ["<10", "10-12", "13-14", "15-17", ">17"]
        default_items = self.get_items() 
        data = {
                "labels": labels,
                "default": default_items[0],
                "default1": default_items[1],
                "default2": default_items[2],
        }
        return Response(data)


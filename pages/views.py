from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import requests
import json
import math
from decimal import Decimal, ROUND_05UP


class TriangleCalculationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(TriangleCalculationView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        response_dict = {}
        request_json = json.loads(request.body)
        if 'base' in request_json:
            response_dict['area'] = int(request_json.get('base', 0)) * int(request_json.get('height', 0)) / 2
        elif 'sideA' in request_json:
            a = Decimal(request_json.get('sideA', 0))
            b = Decimal(request_json.get('sideB', 0))
            c = Decimal(request_json.get('sideC', 0))
            s = (a + b + c) / 2
            area = s * (s - a) * (s - b) * (s - c)
            response_dict['area'] = area.sqrt().quantize(Decimal('.01'), rounding=ROUND_05UP)
        elif 'sideA_x' in request_json:
            a = Decimal(request_json.get('sideA_x', 0))
            b = Decimal(request_json.get('sideB_x', 0))
            angle_sine = Decimal(math.sin(math.radians(int(request_json.get('angleA', 0)))))
            area = Decimal('.5') * a * b * angle_sine
            response_dict['area'] = area.quantize(Decimal('.01'), rounding=ROUND_05UP)

        return JsonResponse(response_dict)


class SecondsConverterView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SecondsConverterView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        response_dict = {}
        request_json = json.loads(request.body)
        if 'hours' in request_json:
            hours = int(request_json.get('hours', 0))
            minutes = int(request_json.get('minutes', 0))
            response_dict['seconds'] = hours * 60 * 60 + minutes * 60

        return JsonResponse(response_dict)


class PythagoreanCalculateView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(PythagoreanCalculateView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        response_dict = {}
        request_json = json.loads(request.body)
        if 'sideA' in request_json:
            a = Decimal(request_json.get('sideA', 0))
            b = Decimal(request_json.get('sideB', 0))
            response_dict['sideC'] = (a * a + b * b).sqrt().quantize(Decimal('.01'))

        return JsonResponse(response_dict)


class RecursiveLauncherView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RecursiveLauncherView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        response_dict = {}
        request_json = json.loads(request.body)
        if 'string_value' in request_json:
            string_value = request_json.get('string_value', 0)
            number_of_reps = int(request_json.get('number_of_reps', 0))
            response_dict['string_repeated'] = recursive_function(string_value, number_of_reps)

        return JsonResponse(response_dict)


def recursive_function(string_value, number_of_reps):
    if number_of_reps > 1:
        return string_value + recursive_function(string_value, number_of_reps - 1)
    else:
        return string_value



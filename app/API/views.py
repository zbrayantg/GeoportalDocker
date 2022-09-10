from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from BIF.models import Property, Status, Licence, Occupancy
from API.serializers import PropertySerializer


@csrf_exempt
def property_list(request):
    """
    List all info, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Property.objects.select_related('status', 'licence', 'occupancy').all()
        serializer = PropertySerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    """ elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PropertySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) """

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import IFSC
from .serializers import ApiSerializer

#Overiding Django's default 404 with custom JSON response
@api_view(['GET'])
def error_404(request, exception):
    return Response(status=status.HTTP_404_NOT_FOUND)

#Return details of branch with matching ifsc
@api_view(['GET'])
def ifsc_details(request,ifsc,format=None):
    ifsc=ifsc.upper()
    try:
        ifsc = IFSC.objects.get(ifsc_code=ifsc)
    except IFSC.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ApiSerializer(ifsc)
        return Response(serializer.data)

#Return all branches of a bank in a city
@api_view(['GET'])
def details_of_branches(request,bank,city,format=None):
    bank=bank.replace('-',' ').upper()
    city=city.replace('-',' ').upper()
    branches = IFSC.objects.filter(bank_name=bank,city=city).all()
    if bool(branches)==False:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ApiSerializer(branches, many=True)
        return Response(serializer.data)
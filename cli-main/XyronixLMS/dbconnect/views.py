from django.http import JsonResponse
import pymongo
from django.views.decorators.csrf import csrf_exempt
import os

@csrf_exempt
def test_connection(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Connection successful!'})

    if request.method == 'POST':
        try:
            mongodb_uri = os.getenv('MONGODB_URI')
            client = pymongo.MongoClient(mongodb_uri)
            db_names = client.list_database_names()
            return JsonResponse({'databases': db_names})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

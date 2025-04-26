from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import Filing

@csrf_exempt
def create_filing(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            filing = Filing.objects.create(
                title=data.get('title'),
                description=data.get('description'),
                filing_date=data.get('filing_date')
            )

            # Send to replication server
            replication_url = 'http://127.0.0.1:8001/api/receive-filing/'  # Port 8001 for Project 2
            requests.post(replication_url, json={
                'title': filing.title,
                'description': filing.description,
                'filing_date': str(filing.filing_date)
            })

            return JsonResponse({'status': 'success', 'filing_id': filing.id})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    else:
        return JsonResponse({'status': 'error', 'message': 'Only POST allowed'})

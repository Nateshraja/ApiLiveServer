from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

@csrf_exempt
def create_filing_entry(request):
    if request.method == 'POST':
        try:
            # Get the data from the POST request
            title = request.POST.get('title')
            content = request.POST.get('content')

            # Save into your own database (optional)

            # Send to replica server
            send_to_replica({
                'title': title,
                'content': content,
            })

            # After successful submission, redirect or show success message
            return JsonResponse({'status': 'success', 'message': 'Filing entry created and replicated.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    # For GET requests, render the form
    return render(request, 'filling/create_filing_form.html')

def send_to_replica(data):
    replica_url = 'http://127.0.0.1:8001/receive-filing/'  # Assuming your replica runs on port 8001
    try:
        response = requests.post(replica_url, json=data)
        print("Replication Response:", response.json())
    except Exception as e:
        print("Replication Error:", str(e))

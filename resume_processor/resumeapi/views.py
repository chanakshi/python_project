from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def test_upload(request):
    if request.method == 'POST':
        file = request.FILES.get('file')
        if file:
            return JsonResponse({'status': 'File received'})
        return JsonResponse({'error': 'No file provided'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

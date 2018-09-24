# REST API
import json
import logging
from django import http
from django.views.decorators.csrf import csrf_exempt


# Get an instance of a logger
logger = logging.getLogger(__name__)


def index(request):
    return http.HttpResponse("Hello, world. You're at the nine index.")


@csrf_exempt
def extract_show(request):
"""Extract shows from a list of shows in the request payload, 
   return those with DRM enabled (drm: true) and
   at least one episode (episodeCount > 0).
"""
    error_result = {'error': 'Could not decode request: JSON parsing failed'}
    if request.method == 'POST':
        input_data = {}
        try:
            input_data = json.loads(request.body)
        except ValueError as ex:
            logger.error('Error parsing json: %s' % ex)
            return http.JsonResponse(error_result, status = 400)
        result = []
        for item in input_data.get('payload', []):
            if item.get('drm') and item.get('episodeCount', 0) > 0:
                show = {
                    'image': item.get('image', {}).get('showImage'),
                    'slug': item.get('slug'),
                    'title': item.get('title')
                }
                result.append(show)
        return http.JsonResponse({'response': result}, status = 200)

    return http.JsonResponse(error_result, status = 400)

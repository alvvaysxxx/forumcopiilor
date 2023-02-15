from django.http import HttpResponse
import time

from django.shortcuts import render, redirect
from django.urls import reverse


class PostRateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and request.path == '/create_post/':
            last_post_time = request.session.get('last_post_time')
            if last_post_time is not None:
                current_time = time.time()
                if current_time - last_post_time < 5 * 60:
                    return redirect('post_wait')
            request.session['last_post_time'] = time.time()
        response = self.get_response(request)
        return response

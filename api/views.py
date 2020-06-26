from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.authtoken.models import Token

@login_required
def get_tokens(request):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	tokens = Token.objects.filter(user = request.user)

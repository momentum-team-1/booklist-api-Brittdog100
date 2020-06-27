from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from rest_framework.authtoken.models import Token

@login_required
def get_tokens(request):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	tokens = Token.objects.filter(user = request.user)
	return render(request, 'tokens.html', { 'tokens': tokens })

def new_token(request):
	if not request.user.is_authenticated:
		return HttpResponse(status = 403)
	token = Token(user = request.user)
	token.save()
	return redirect('view_tokens')

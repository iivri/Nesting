from django.shortcuts import render, redirect 

def login_redirect(request):
	return redirect('/Identity/')
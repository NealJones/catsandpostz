import json, requests, random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
# import requests
from social.apps.django_app.default.models import UserSocialAuth
# import random


def home(request):
    return render(request, "angular.html")


def chosen(request):
    return render(request, "chosen.html")


def angular(request):
    return render(request, "angular.html")


def get_fb_post(request):
    user_id = UserSocialAuth.objects.get(user=request.user)
    # you have to do a series of requests to get down to the target
    resp = requests.get("https://graph.facebook.com/{0}?fields=friends&access_token={1}".format(user_id.uid, user_id.tokens))
    friends = resp.json()['friends']['data']  # Sets retrieved object equal to variable

    found_post = None
    while not found_post:
        friend = random.choice(friends)  # Gets random
        print friend
        friend_id = friend['id']  # sets random friend equal to variable
        resp = requests.get("https://graph.facebook.com/{0}/posts/?access_token={1}&limit=100".format(friend_id, settings.FACEBOOK_APP_TOKEN))
        posts = resp.json()
        
        if len(posts) > 0:  # friend_posts.from.name
            for post in posts['data']:
                if 'status_type' in post and post['status_type'] == 'wall_post':
                    found_post = post

    data = {'friend_posts': found_post, 'picture': 'https://graph.facebook.com/{0}/picture?type=large'.format(friend_id), 'name': friend['name']}

    return HttpResponse(json.dumps(data), mimetype='application/json')

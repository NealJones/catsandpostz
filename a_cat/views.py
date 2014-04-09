import json, requests, random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from social.apps.django_app.default.models import UserSocialAuth
# import random
import urllib
from facebook import *
import json
import facebook  # pip install facebook-sdk


def home(request):
    return render(request, "angular.html")


def chosen(request):
    return render(request, "chosen.html")


def angular(request):
    return render(request, "angular.html")

#SELECT post_id, app_id, source_id, updated_time, filter_key, attribution, message, action_links, likes, permalink FROM stream WHERE filter_key IN (SELECT filter_key FROM stream_filter WHERE uid = me() AND type = 'newsfeed')


def get_fb_post(request):
    user_id = UserSocialAuth.objects.get(user=request.user)
    api = facebook.GraphAPI(user_id.tokens)
    # response gets deserialized into a python object
    response = api.fql("SELECT name, type, value, filter_key FROM stream_filter WHERE uid = me()")
    print(response)

    data = {'name': 'name'}
    return HttpResponse(json.dump(data), mimetype='application/json')

# TODO Working example follows
# def get_fb_post(request):  #this is being called from _
#     user_id = UserSocialAuth.objects.get(user=request.user)
#     # you have to do a series of requests to get down to the target
#     resp = requests.get("https://graph.facebook.com/{0}?fields=friends&access_token={1}".format(user_id.uid, user_id.tokens))
#     friends = resp.json()['friends']['data']  # Sets retrieved object equal to variable
#     found_post = None
#     while not found_post:
#         friend = random.choice(friends)  # Gets random
#         print friend
#         friend_id = friend['id']  # sets random friend equal to variable
#         resp = requests.get("https://graph.facebook.com/{0}/posts/?access_token={1}&limit=100".format(friend_id, settings.FACEBOOK_APP_TOKEN))
#         print resp
#         posts = resp.json()
#         if len(posts) > 0:
#             for post in posts['data']:
#                 if 'status_type' in post and post['status_type'] == 'wall_post':
#                     found_post = post
#
#     data = {'friend_posts': found_post, 'picture': 'https://graph.facebook.com/{0}/picture?type=large'.format(friend_id), 'name': friend['name']}
#
#     return HttpResponse(json.dumps(data), mimetype='application/json')
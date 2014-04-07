import json, requests, random
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
import requests
from social.apps.django_app.default.models import UserSocialAuth
# import random


def home(request):
    return render(request, "angular.html")


def chosen(request):
    return render(request, "chosen.html")


def angular(request):
    return render(request, "angular.html")

#SELECT post_id, app_id, source_id, updated_time, filter_key, attribution, message, action_links, likes, permalink FROM stream WHERE filter_key IN (SELECT filter_key FROM stream_filter WHERE uid = me() AND type = 'newsfeed')


def get_fb_post(request):

    s = requests.Session()
    s.params = {'access_token': settings.FACEBOOK_APP_TOKEN} # so you don't have to specify it every time
    print(s.params)
    query = ('{"user_sex":"SELECT sex FROM user WHERE uid=me()",'
             '"friends":"SELECT uid, name FROM user WHERE uid IN '
             '(SELECT uid2 FROM friend WHERE uid1 = me()) '
             'AND not (sex in (SELECT sex FROM #user_sex)) '
             ' ORDER BY name"}')
    s.get('https://graph.facebook.com/fql', params={'q': query})

    #TODO first fql attemp
    # # user_id = UserSocialAuth.objects.get(user=request.user)
    # query = "SELECT post_id, app_id, source_id, updated_time, filter_key, attribution, message, action_links, likes, permalink FROM stream WHERE filter_key IN (SELECT filter_key FROM stream_filter WHERE uid = me() AND type = 'newsfeed')"
    # # print(query)
    #
    # found_post = "https://api.facebook.com/method/fql.query?query=" + query
    # # print(found_post)
    #
    # data = {'friend_posts': found_post}
    # # print(data)

    # return HttpResponse(json.dumps(data), mimetype='application/json')





# I am not sure that ...me()... is a sufficient replacement to ...user_id.uid...



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
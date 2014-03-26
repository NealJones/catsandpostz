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


# Supposed to get the fb post...not sure about the details

# def get_fb_post(request):
#     user_id = UserSocialAuth.objects.get(user=request.user)
#     # you have to do a series of requests to get down to the target
#     resp = requests.get("https://graph.facebook.com/{0}?fields=friends&access_token={1}".format(user_id.uid, user_id.tokens))
#     friend = resp.json()['friends']['data'][0]
#     print friend
#     friend_id = friend['id']
#     print friend_id
#     resp = requests.get("https://graph.facebook.com/{0}?fields=feed&access_token={1}".format(friend_id, user_id.tokens))
#     data = {'friend_posts': resp.json()}
#
#     return HttpResponse(json.dumps(data), mimetype='application/json')

#----------------- THOUGHTS ------------------
#   Can this actually get to the news feed?
#   Do I need to use FQL for this?
#   I think this is the solution:
#         http://stackoverflow.com/questions/5795637/find-a-photo-for-each-of-10-random-facebook-friends-in-fql

# Notes:
#

# ------------------ WORKING CODE AS OF SAT MAR 22 @ 11:28:33 ---------------------------
# <>
def get_fb_post(request):
    user_id = UserSocialAuth.objects.get(user=request.user)
    # you have to do a series of requests to get down to the target
    resp = requests.get("https://graph.facebook.com/{0}?fields=friends&access_token={1}".format(user_id.uid, user_id.tokens))
    friends = resp.json()['friends']['data']  # Sets retrieved object equal to variable

    found_post = None
    while not found_post:
        friend = random.choice(friends)  # Gets random friend
        friend_id = friend['id']  # sets random friend equal to variable
        resp = requests.get("https://graph.facebook.com/{0}/posts/?access_token={1}&limit=100".format(friend_id, settings.FACEBOOK_APP_TOKEN))
        posts = resp.json()
        if len(posts) > 0:  # friend_posts.from.name
            for post in posts['data']:
                if 'status_type' in post and post['status_type'] == 'wall_post':
                    found_post = post

    data = {'friend_posts': found_post}

    return HttpResponse(json.dumps(data), mimetype='application/json')


# ---------- The link is from the graph api and gets 1 status from 8 friends ----------
# def get_fb_post(request):
#     user_id = UserSocialAuth.objects.get(user=request.user)
#     resp = requests.get("https://graph.facebook.com/{0}?fields=friends&access_token={1}".format(user_id.uid, user_id.tokens))
#     data = {"user fb id": resp.json()}
#
#     return HttpResponse(json.dumps(data), mimetype='application/json')


 # ---------- The link is from the graph api and gets 1 status from 8 friends ----------
    # https://graph.facebook.com/193303586?fields=friends.limit(8).fields(statuses.limit(1))

 # -------------- The following code will get you the fb user_id -----------------------
    # user_social_auth = UserSocialAuth.objects.get(user=request.user)
    # data = {"user fb id": user_social_auth.uid}
    # return HttpResponse(json.dumps(data), mimetype='application/json')


#----------------------------------------------------------------------------

# def get_fql_result(fql):
#     cachename = 'fbgallery_cache_' + defaultfilters.slugify(fql)
#     data = None
#     if cache_expires > 0:
#         data = cache.get(cachename)
#     if data == None:
#         options ={
#             'query':fql,
#             'format':'json',
#         }
#         f = urllib2.urlopen(urllib2.Request(fql_url, urllib.urlencode(options)))
#         response = f.read()
#         f.close()
#         data = json.loads(response)
#         if cache_expires > 0:
#             cache.set(cachename, data, cache_expires*60)
#     return data

# <><>
# def get_fb_post(request):
#     query = "SELECT post_id, app_id, source_id, updated_time, filter_key, attribution, message, action_links, likes, permalink FROM stream WHERE filter_key IN (SELECT filter_key FROM stream_filter WHERE uid = me() AND type = 'newsfeed')"
#     print(query)
#     query = urllib.quote(query)
#     print(query)
#     url = "https://graph.facebook.com/fql?q=" +query
#
#     data = urllib.urlopen(url).read()
#     print(data)


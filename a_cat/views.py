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

    posts_query = "SELECT created_time, post_id, actor_id, type, updated_time, attachment FROM stream WHERE post_id in (select post_id from stream where ('video') in attachment AND source_id IN ( SELECT uid2 FROM friend WHERE uid1=me()) limit 100)"
    users_query = "SELECT uid, first_name FROM user WHERE uid IN (SELECT actor_id FROM (#posts_query))"

    token = "1398205403780400|yqw-zBkUg18kyJbtTWhn0_pLjX8"
    queries = {'posts_query': posts_query, 'users_query': users_query}
    fql_var = "https://api.facebook.com/method/fql.query?access_token=" + token + "&q=" + json.dumps(queries_json) + "&format=json"
    data = urllib.urlopen(fql_var)
    fb_stream = json.loads(data.read())
    print(fb_stream)

    # #TODO 4th attempt, spiraled into an incoherent mess
    # # access_token = "1398205403780400|yqw-zBkUg18kyJbtTWhn0_pLjX8"
    # # query = {
    # #     "friends": "SELECT uid, name, sex FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me()) AND not (sex in (select sex from #user_sex))  ORDER BY name"
    # #         }
    #
    # # graph = facebook.GraphAPI(access_token)
    #
    # graph = facebook.GraphAPI()
    # # print "Mashable has %s fans" % graph.get_object('/mashable')['fan_count']
    # print(graph.get_object('/mashable')['fan_count'])
    # # return graph.fql(str(query))


    #TODO COPIED EXAMPLE
    # query = "SELECT uid2 FROM friend WHERE uid1 = me()"
    # params = urllib.urlencode({'q': query, 'access_token': "1398205403780400|yqw-zBkUg18kyJbtTWhn0_pLjX8"})
    # print params
    #
    # url = "https://graph.facebook.com/fql?" + params
    # print(url)
    # data = urllib.urlopen(url).read()
    # print(data)

    # TODO second fql attempt
    # s = requests.Session()
    # s.params = {'access_token': settings.FACEBOOK_APP_TOKEN} # so you don't have to specify it every time
    # print(s.params)
    # query = "SELECT uid2 FROM friend WHERE uid1 = me()"
    # resp = requests.get("https://graph.facebook.com/fql?q={0}&access_token={1}".format(query, settings.FACEBOOK_APP_TOKEN))  # user_id.tokens
    # print(resp)

    # url = "https://graph.facebook.com/fql?q=" + query + "access_token=1398205403780400|yqw-zBkUg18kyJbtTWhn0_pLjX8"
    # info = requests.get(url)
    # s.get('https://graph.facebook.com/fql', params={'q': query})
    # print(s.get)
    # print(url)
    # print(info)
    # data = json.loads
    #
    # return data

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
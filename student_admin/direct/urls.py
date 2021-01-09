from django.urls import path
from direct.views import Inbox, UserSearch, Directs, NewConversation, SendDirect ,OtherUserProfile,ProfileSearch




urlpatterns = [
   	path('', Inbox, name='inbox'),
   	path('directs/<username>', Directs, name='direct'),
   	path('new/', UserSearch, name='usersearch'),
   	path('new/<username>', NewConversation, name='newconversation'),
   	path('send/', SendDirect, name='send_direct'),
    path('new1/<username>', OtherUserProfile , name='profile_1'),
    path('new_n/', ProfileSearch, name='ProfileSearch'),

]

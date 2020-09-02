from django.contrib import admin

from .models import Comment,BidInfo,Listing,WatchList,User
# Register your models here.

admin.site.register(Comment)
admin.site.register(BidInfo)
admin.site.register(Listing)
admin.site.register(WatchList)
admin.site.register(User)

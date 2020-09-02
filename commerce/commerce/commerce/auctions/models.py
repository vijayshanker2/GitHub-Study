from django.contrib.auth.models import AbstractUser
from django.db import models


class CommentManager(models.Manager):
    def create_Comment(self, title):
        comment = self.create(comment=title)
        return comment

class Comment(models.Model):
    comment = models.CharField(max_length=300, blank=True, null=True)
    objects = CommentManager()

class BidInfoManager(models.Manager):
    def create_BidInfo(self, title):
        bidinfo = self.create(min_bid=title,current_bid=title)
        return bidinfo

class BidInfo(models.Model):
    min_bid = models.IntegerField(default=0)
    current_bid = models.IntegerField(default=0)
    objects = BidInfoManager()



class ListingManager(models.Manager):
    def create_listing(self, title, description, category, comment, bid, image_url, listed):
        comment_obj = Comment.objects.create_Comment(comment)
        bidinfo_obj = BidInfo.objects.create_BidInfo(bid)
        listing = self.create(title=title, description=description, category=category,
        comment=comment_obj, bidinfo=bidinfo_obj,image_url=image_url, listed=listed )

        return listing


class Listing(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    category = models.CharField(max_length=300, blank=True, null=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    bidinfo = models.ForeignKey(BidInfo, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=300, blank=True, null=True)
    listed = models.BooleanField(default=True)
    objects = ListingManager()

class WatchList(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

class User(AbstractUser):
    watchlist = models.ForeignKey(WatchList, on_delete=models.SET_NULL, null=True, blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.SET_NULL, null=True, blank=True)

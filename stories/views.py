# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from stories.models import Media, Story
from stories.serializers import (MediaSerializer, StorySerializer,
                                 UserStoriesSerializer)


class UserStoriesView(ListAPIView):
    """
        This view looks up a User's stories via their fb_id and returns them.   
    """
    serializer_class = UserStoriesSerializer
    lookup_field = 'uid'

    def get_queryset(self):
        """
        This view should return a list of all the stories for
        the user as determined by the uid portion of the URL.
        """
        uid = self.kwargs['uid']
        return Story.objects.filter(uid=uid)


class StoryCreateView(ListCreateAPIView):
    """
    This view allows the user to POST a story and add it to the database layer.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class StoriesDetailView(RetrieveUpdateDestroyAPIView):
    """
    This view allows a user to GET PATCH and DELETE a story and update the database layer.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer


class MediaUploadView(CreateAPIView):
    """
    This view allows the user to POST media and add it to the database layer.
    """
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

from django.views import generic
from web.serializers import *
from django.contrib.auth.models import User
from rest_framework import viewsets


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PlaceholderViewSet(viewsets.ModelViewSet):
    queryset = Placeholder.objects.all()
    serializer_class = PlaceholderSerializer


class IndexView(generic.ListView):
    template_name = 'web/index.html'
    context_object_name = 'placeholder_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Placeholder.objects.all()

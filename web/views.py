from django.views import generic
from .models import Placeholder


class IndexView(generic.ListView):
    template_name = 'web/index.html'
    context_object_name = 'placeholder_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Placeholder.objects.all()


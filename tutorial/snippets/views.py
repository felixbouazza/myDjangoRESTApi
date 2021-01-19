from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import mixins
from rest_framework import generics

## Les vues basés sur des classes nous permettent de composer facilement
## des bits comportementaux réutilisables
## Les mixins CRUD (create, list, update, delete ) sont implementés dans le catalogue mixins de rest_framework
class SnippetList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

from rest_framework import viewsets

from .serializers import SprintSerializer
from .models import Sprint


class SprintViewSet(viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer

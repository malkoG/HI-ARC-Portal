from django.http import Http404

from rest_framework import renderers, viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response

from appliers.serializers import ApplierSerializer
from appliers.models import Applier


class ApplierAdminListViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Applier.objects.all()
    serializer_class = ApplierSerializer
    permission_classes = (IsAdminUser)
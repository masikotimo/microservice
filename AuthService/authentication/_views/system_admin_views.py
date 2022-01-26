from django.shortcuts import render
from authentication.models import SystemAdmin
from rest_framework import viewsets
from authentication.serializers import SystemAdminSerializer
from AuthService.mixins import view_mixins
from AuthService import filters


# Create your views here.


class CreateSystemAdminViewSet(view_mixins.BaseCreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
    lookup_field = 'id'

    def post(self, request):
        try:
            return self.create(request)
        except Exception as exception:
            raise exception


class ViewSystemAdminsListViewSet(view_mixins.BaseListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
    lookup_field = 'id'
    filter_backends = [filters.SearchFilter]
    search_fields = ['user']

    def get(self, request):
        if 'vehicles' in cache:
            # get results from cache
            vehicles = cache.get('vehicles')
            try:
                return self.list(request)
            except Exception as exception:
                raise exception

        else:
            results = [vehicle.to_json() for vehicle in queryset]
            # store data in cache
            cache.set('vehicles', results, timeout=CACHE_TTL)
            try:
                return self.list(request)
            except Exception as exception:
                raise exception


class RetrieveSystemAdminViewSet(view_mixins.BaseRetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
    lookup_field = 'id'

    def get(self, request, id=None):
        try:
            return self.retrieve(request, id)
        except Exception as exception:
            raise exception


class UpdateSystemAdminViewSet(view_mixins.BaseUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
    lookup_field = 'id'

    def put(self, request, id=None):
        try:
            return self.update(request, id)
        except Exception as exception:
            raise exception


class DeleteSystemAdminViewSet(view_mixins.BaseDeleteAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
    lookup_field = 'id'

    def delete(self, request, id=None):
        try:
            return self.destroy(request, id)
        except Exception as exception:
            raise exception

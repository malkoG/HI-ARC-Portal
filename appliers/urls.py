from django.urls import path

from appliers.views import ApplierViewSet, ApplierAdminViewSet

applier_list = ApplierAdminListViewSet.as_view({
    'get': 'list'
})

applier_create = ApplierViewSet.as_view({
    'post': 'create'
})

applier_detail = ApplierAdminViewSet.as_view({
    'get': 'retrieve',    
    'delete': 'destroy'
})


urlpatterns = [
    path('', ),
    path('<int:pk>', applier_detail)
]
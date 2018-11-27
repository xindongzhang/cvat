# Copyright (C) 2018 Intel Corporation
#
# SPDX-License-Identifier: MIT


from django.urls import path
from . import views


urlpatterns = [
    path('get/<int:tid>', views.get_repository),
    path('push/<int:tid>', views.push_repository),
    path('check/<str:rq_id>', views.check_process),
]

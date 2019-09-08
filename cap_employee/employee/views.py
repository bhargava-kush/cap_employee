# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.status import (HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK)


from django.shortcuts import render

# Create your views here.

class EmployeeView(GenericAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            data = serializer.create(request.data)
            response = {"response": {
                'success': True,
                'msg': 'Employee object created succesfully'}
            }
        else:
            response = {"response": {
                'success': False,
                'msg': 'Bad request',
                'errors': serializer.errors }
            }

        return Response(response, status=HTTP_200_OK)





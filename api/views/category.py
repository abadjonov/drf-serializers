from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from ..models import Category
from ..serializers.category import CategoryModelSerializer


class CategoryView(APIView):
    def get(self, request: Request) -> Response:
        serializer = CategoryModelSerializer(
            Category.objects.all(),
            many=True
        )

        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = CategoryModelSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            category = serializer.save()

            return Response(
                CategoryModelSerializer(category).data,
                status.HTTP_201_CREATED
            )


class CategoryDetailsView(APIView):
    def get(self, request: Request, id: int) -> Response:
        serializer = CategoryModelSerializer(Category.objects.get(id),)

        return Response(serializer.data)

    def put(self, request: Request, id: int) -> Response:
        pass

    def patch(self, request: Request, id: int) -> Response:
        pass

    def delete(self, request: Request, id: int) -> Response:
        pass

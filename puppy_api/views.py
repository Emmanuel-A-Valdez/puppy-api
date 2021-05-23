from rest_framework.decorators import api_view
from rest_framework.response import Response

from puppy_api.models import Puppy
from puppy_api.serializers import PuppySerializer


@api_view(["GET"])
def puppy_api_overview(request):
    api_urls = {
        "List": "/puppy-list/",
        "Detail": "/puppy-detail/<int:pk>/",
        "Create": "/puppy-create/",
        "Update": "/puppy-update/<int:pk>/",
        "Delete": "/puppy-delete/<int:pk>/",
    }

    return Response(api_urls)


@api_view(["GET"])
def puppy_list(request):
    puppys = Puppy.objects.all().order_by("-id")
    serializer = PuppySerializer(puppys, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def puppy_detail(request, pk):
    puppy = Puppy.objects.get(id=pk)
    serializer = PuppySerializer(puppy, many=False)

    return Response(serializer.data)


@api_view(["POST"])
def puppy_create(request):
    serializer = PuppySerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["PUT"])
def puppy_update(request, pk):
    puppy = Puppy.objects.get(id=pk)
    serializer = PuppySerializer(instance=puppy, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(["DELETE"])
def puppy_delete(request, pk):
    puppy = Puppy.objects.get(id=pk)
    puppy.delete()

    return Response("This puppy has been succsesfully deleted!")

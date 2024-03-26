from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAdminUser

from apps.our_goal.models import OurGoal
from apps.our_goal.serializers import OurGoalSerializer


class AdminOurGoalApiViewSet(ModelViewSet):
    queryset = OurGoal.objects.all()
    serializer_class = OurGoalSerializer
    permission_classes = [IsAdminUser]


class OurGoalApiViewSet(GenericViewSet,
                        ListModelMixin,
                        RetrieveModelMixin):
    queryset = OurGoal.objects.all()
    serializer_class = OurGoalSerializer

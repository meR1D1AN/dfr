from rest_framework import viewsets
from django_filters import rest_framework as filters

from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentFilter(filters.FilterSet):
    paid_course = filters.NumberFilter(field_name='paid_course__id')
    paid_lesson = filters.NumberFilter(field_name='paid_lesson__id')
    payment_method = filters.CharFilter(field_name='payment_method')

    class Meta:
        model = Payment
        fields = ['paid_course', 'paid_lesson', 'payment_method']


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PaymentFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering')
        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset

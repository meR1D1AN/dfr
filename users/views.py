# from rest_framework import viewsets
# from django_filters import rest_framework as filters
#
# from users.models import User, Payment
# from users.serializers import UserSerializer, PaymentSerializer
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class PaymentFilter(filters.FilterSet):
#     paid_course = filters.NumberFilter(field_name='paid_course__id')
#     paid_lesson = filters.NumberFilter(field_name='paid_lesson__id')
#     payment_method = filters.CharFilter(field_name='payment_method')
#
#     class Meta:
#         model = Payment
#         fields = ['paid_course', 'paid_lesson', 'payment_method']
#
#
# class PaymentViewSet(viewsets.ModelViewSet):
#     queryset = Payment.objects.all()
#     serializer_class = PaymentSerializer
#     filter_backends = (filters.DjangoFilterBackend,)
#     filterset_class = PaymentFilter
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         ordering = self.request.query_params.get('ordering')
#         if ordering:
#             queryset = queryset.order_by(ordering)
#         return queryset

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Donat
from users.serializers import UserSerializer, DonatSerializer
from users.services import create_stripe_price, create_stripe_session


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class DonatCreateAPIView(CreateAPIView):
    serializer_class = DonatSerializer
    queryset = Donat.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user_link=self.request.user)
        price = create_stripe_price(payment.amount)
        session_id, payment_user_link = create_stripe_session(price)
        payment.session_id = session_id
        payment.link = payment_user_link
        payment.save()

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
# from student_management_app.templates import

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):

        token = super().get_token(user)
        token["email"] = user.email
        token["username"] = user.username
        return token

class MyTokenObtainPairCustomView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# def csrf_failure(request, reason=""):
#     ctx = {'message': 'some custom messages'}
#     return render_to_response(, ctx)
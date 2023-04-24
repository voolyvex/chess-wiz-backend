from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # for any additional fields you'd like to add to the JWT sent back in response
        # add below using token["field name"] = user.name_of_property

        token["username"] = user.username
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["is_student"] = user.is_student
        token["is_coach"] = user.is_coach

        return token


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[
                                   UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('username', 'password', 'email',
                  'first_name', 'last_name', 'is_student', 'is_coach', 'my_games', 'assigned', 'pgn_favorites')

    def create(self, validated_data):
        assigned = validated_data.pop('assigned', [])
        my_games = validated_data.pop('my_games', [])
        pgn_favorites = validated_data.pop('pgn_favorites', [])

        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_student=validated_data.get('is_student', False),
            is_coach=validated_data.get('is_coach', False),
        )

        user.assigned.set(assigned)
        user.my_games.set(my_games)
        user.set_password(validated_data['password'])
        user.save()

        # Set pgn_favorites using set() method
        user.pgn_favorites.set(pgn_favorites)

        return user



# serializer for junction tables
class UserPgnSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = User
        fields = ('my_games', 'assigned', 'is_student', 'username', 'first_name', 'last_name', 'pgn_favorites')

    
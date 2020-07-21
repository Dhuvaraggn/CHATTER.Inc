from rest_framework import serializers
from .models import *

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields="__all__"

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Accounts
        fields="__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields="__all__"


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Member
        fields="__all__"



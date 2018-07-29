from rest_framework import serializers
from .models import Applier

class ApplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)

    # 학회 가입 승인 시 Portal 에서 사용할 아이디/패스워드
    username     = serializers.CharField(required=True, max_length=30, allow_blank=False)
    password     = serializers.CharField(required=True, max_length=100, allow_blank=False)

    # 학회 가입 승인 시 임원이 봐야 할 필드
    realname     = serializers.CharField(required=True, max_length=30, allow_blank=False)
    student_id   = serializers.CharField(required=True, max_length=10, allow_blank=False)
    major        = serializers.CharField(required=True, max_length=20, allow_blank=False)
    grade        = serializers.CharField(required=True, max_length=10, allow_blank=False)
    phone_number = serializers.CharField(required=True, max_length=15, allow_blank=False)
    email        = serializers.CharField(required=True, max_length=50, allow_blank=False)

    motivation   = serializers.CharField(required=True, allow_blank=False)
    portfolio    = serializers.CharField()

    class Meta:
        model = Applier
        fields = ('id', 'realname', 'student_id', 'major', 'grade', 'phone_number', 'email', 'motivation', 'portfolio')

    def create(self, validated_data):
        """
        검증된 데이터를 통해 `지원자` 객체를 생성하고 반환
        """
        return Applier.objects.create(**validated_data)
from django.db import models

class Applier(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    # 학회 가입 승인 시 Portal 에서 사용할 아이디/패스워드
    username   = models.CharField(max_length=30, blank=False)
    password   = models.CharField(max_length=100, blank=False)

    # 학회 가입 승인 시 임원이 봐야 할 필드
    realname     = models.CharField(max_length=30, blank=False)
    student_id   = models.CharField(max_length=10, blank=False)
    major        = models.CharField(max_length=20, blank=False)
    grade        = models.CharField(max_length=10, blank=False)
    phone_number = models.CharField(max_length=15, blank=False)
    email        = models.CharField(max_length=50, blank=False)

    motivation   = models.TextField(blank=False)
    portfolio    = models.TextField()

    class Meta:
        ordering = ('created_at', )
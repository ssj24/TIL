from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


class Patient(models.Model):
    name = models.TextField()
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # 중개모델이 의사랑 연결해주니까.
    # 일단 의사 한 명에 환자 여러명일 테니까
    # doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')
    # reservation 안 쓰이니까 through 옵션 지우기
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):    
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
    
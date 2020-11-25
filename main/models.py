from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.IntegerField()
    full_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=80)
    photo = models.CharField()
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


    def __str__(self):
        return f'{self.full_name}' + f'{self.pk}'


    class Meta:
        verbose_name = 'Talaba'
        verbose_name_plural = 'Talabalar'


class StudentTaskSubmition(models.Model):
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    StudentTask = models.ForeignKey(StudentTask, on_delete=models)
    task_answer = models.CharField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()


class StudentTask(models.Model):
    id = models.ForeignKey(Student, on_delete=models.CASCADE)
    full_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.CharField()
    Group = models.ForeignKey(Group, on_delete=models.CASCADE)


class Group(models.Model):
    id = models.ForeignKey(Student, on_delete=models.CASCADE)
    full_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    description = models.ForeignKey(StudentTask, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()











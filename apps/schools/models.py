from django.core.validators import MaxValueValidator
from django.urls import reverse
from django.db import models



MODEL = models.Model
MAX_LENGTH = 255
MIN_LENGTH = 70


class Schools(MODEL):
    school_name = models.CharField('Название школы', max_length=MAX_LENGTH)
    location = models.CharField('Местонахождение школы', max_length=MAX_LENGTH)
    type = models.CharField('Тип школы', max_length=MAX_LENGTH)


    def __str__(self) -> str:
        return self.school_name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class Students(MODEL):
    username = models.CharField('Имя', max_length=MIN_LENGTH)
    surname = models.CharField('Фамилия', max_length=MIN_LENGTH)
    email = models.EmailField('Email', max_length=MIN_LENGTH)
    
    student_school = models.CharField('Школа', max_length=70)
    student_class = models.IntegerField('Класс')

    individual_number = models.IntegerField('ИИН')

    phone = models.IntegerField('Телефон')

    password1 = models.CharField('Пароль', max_length=MIN_LENGTH, null=True)

    image_file = models.ImageField('Фото', null=True, upload_to='resource')

    created_date = models.DateField('Дата регистрации', auto_now_add=True)


    def __str__(self):
        return f'{self.username} {self.surname}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class Teachers(MODEL):
    photo = models.ImageField('Фото', null=True, upload_to='resource')
    name = models.CharField('Имя', max_length=MIN_LENGTH, null=True)
    surname = models.CharField('Фамилия', max_length=MIN_LENGTH, null=True)
    father_name = models.CharField('Отчество', max_length=MIN_LENGTH, null=True)

    diploma_specialty = models.CharField('Специальность по диплому', max_length=MIN_LENGTH, null=True)
    education = models.CharField('Образование', max_length=MIN_LENGTH, null=True)

    job_title = models.CharField('Должность', max_length=MIN_LENGTH, null=True)
    
    category = models.CharField('Категория', max_length=MIN_LENGTH, null=True)

    work_experience = models.CharField('Стаж работы', max_length=MIN_LENGTH, null=True)
    achievement = models.CharField('Достижения', max_length=MIN_LENGTH, default='')


    def __str__(self) -> str:
        return f'{self.name} {self.surname} {self.father_name}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'



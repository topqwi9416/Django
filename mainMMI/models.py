from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# ... существующие модели Category, Delivery, Order ...

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
    ]
    
    CITIZENSHIP_CHOICES = [
        ('RU', 'Россия'),
        ('BY', 'Беларусь'),
        ('KZ', 'Казахстан'),
        ('OTHER', 'Другое'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    
    # ФИО
    last_name = models.CharField('Фамилия', max_length=150, blank=True)
    first_name = models.CharField('Имя', max_length=150, blank=True)
    middle_name = models.CharField('Отчество', max_length=150, blank=True)
    
    # Основное
    birth_date = models.DateField('Дата рождения', null=True, blank=True)
    gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICES, blank=True)
    birth_place = models.CharField('Место рождения', max_length=200, blank=True)
    citizenship = models.CharField('Гражданство', max_length=10, choices=CITIZENSHIP_CHOICES, default='RU')
    inn = models.CharField('ИНН', max_length=12, blank=True)
    
    # Контакты
    telegram = models.CharField('Telegram', max_length=100, blank=True)
    phone = models.CharField('Телефон', max_length=20, blank=True)
    
    # Адрес регистрации
    reg_zip = models.CharField('Индекс регистрации', max_length=10, blank=True)
    reg_region = models.CharField('Регион регистрации', max_length=100, blank=True)
    reg_city = models.CharField('Город регистрации', max_length=100, blank=True)
    reg_street = models.CharField('Улица регистрации', max_length=150, blank=True)
    reg_house = models.CharField('Дом регистрации', max_length=20, blank=True)
    reg_flat = models.CharField('Квартира регистрации', max_length=20, blank=True)
    
    # Флаг совпадения адресов
    same_address = models.BooleanField('Адрес проживания совпадает с регистрацией', default=True)
    
    # Адрес проживания
    live_zip = models.CharField('Индекс проживания', max_length=10, blank=True)
    live_region = models.CharField('Регион проживания', max_length=100, blank=True)
    live_city = models.CharField('Город проживания', max_length=100, blank=True)
    live_street = models.CharField('Улица проживания', max_length=150, blank=True)
    live_house = models.CharField('Дом проживания', max_length=20, blank=True)
    live_flat = models.CharField('Квартира проживания', max_length=20, blank=True)
    
    class Meta:
        db_table = 'user_profile'
    
    def __str__(self):
        return f'Профиль {self.user.username}'


class PracticeDocument(models.Model):
    PRACTICE_TYPES = [
        ('educational', 'Учебная практика'),
        ('production', 'Производственная практика'),
        ('prediploma', 'Преддипломная практика'),
    ]
    
    COMPETENCE_LEVELS = [
        ('full', 'Сформирована полностью'),
        ('partial', 'Сформирована частично'),
        ('none', 'Не сформирована'),
    ]
    
    QUALITY_LEVELS = [
        ('high', 'Высокое'),
        ('medium', 'Среднее'),
        ('low', 'Низкое'),
    ]
    
    MANIFESTATION_LEVELS = [
        ('regular', 'Проявлял регулярно'),
        ('episodic', 'Проявлял эпизодически'),
        ('none', 'Не проявлял'),
    ]
    
    # Основная информация
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='practice_documents')
    practice_type = models.CharField('Вид практики', max_length=20, choices=PRACTICE_TYPES)
    document_type = models.CharField('Тип документа', max_length=50, default='attestation')
    
    # Данные студента
    fio = models.CharField('ФИО студента', max_length=200, blank=True)
    speciality = models.CharField('Специальность', max_length=200, blank=True)
    group = models.CharField('Группа', max_length=50, blank=True)
    course = models.CharField('Курс', max_length=10, blank=True)
    education_form = models.CharField('Форма обучения', max_length=50, blank=True)
    
    # Даты практики
    start_date = models.DateField('Дата начала', null=True, blank=True)
    end_date = models.DateField('Дата окончания', null=True, blank=True)
    
    # Место прохождения
    organization = models.CharField('Организация', max_length=300, blank=True)
    organization_address = models.CharField('Адрес организации', max_length=300, blank=True)
    supervisor = models.CharField('Руководитель практики', max_length=200, blank=True)
    
    # Код модуля
    module_code = models.CharField('Код ПМ', max_length=50, blank=True)
    
    # Выполненные работы (качество выполнения)
    work_1_quality = models.CharField('Работа 1 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_2_quality = models.CharField('Работа 2 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_3_quality = models.CharField('Работа 3 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_4_quality = models.CharField('Работа 4 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_5_quality = models.CharField('Работа 5 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_6_quality = models.CharField('Работа 6 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_7_quality = models.CharField('Работа 7 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_8_quality = models.CharField('Работа 8 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_9_quality = models.CharField('Работа 9 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_10_quality = models.CharField('Работа 10 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    work_11_quality = models.CharField('Работа 11 качество', max_length=10, choices=QUALITY_LEVELS, blank=True)
    
    # Профессиональные компетенции
    pk_1_level = models.CharField('ПК 12.1 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    pk_2_level = models.CharField('ПК 12.2 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    pk_3_level = models.CharField('ПК 12.3 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    pk_4_level = models.CharField('ПК 12.4 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    pk_5_level = models.CharField('ПК 12.5 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    pk_6_level = models.CharField('ПК 12.6 уровень', max_length=10, choices=COMPETENCE_LEVELS, blank=True)
    
    # Общие компетенции (проявление)
    ok_1_level = models.CharField('ОК 01 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_2_level = models.CharField('ОК 02 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_3_level = models.CharField('ОК 03 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_4_level = models.CharField('ОК 04 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_5_level = models.CharField('ОК 05 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_6_level = models.CharField('ОК 06 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_7_level = models.CharField('ОК 07 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_8_level = models.CharField('ОК 08 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_9_level = models.CharField('ОК 09 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_10_level = models.CharField('ОК 10 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    ok_11_level = models.CharField('ОК 11 уровень', max_length=10, choices=MANIFESTATION_LEVELS, blank=True)
    
    # Характеристика (текстовые поля)
    work_attitude = models.TextField('Отношение к работе', blank=True)
    discipline = models.TextField('Выполнение правил трудового распорядка', blank=True)
    safety_rules = models.TextField('Соблюдение правил техники безопасности', blank=True)
    initiative = models.TextField('Проявление инициативы', blank=True)
    relationships = models.TextField('Взаимоотношения с коллегами', blank=True)
    competence_formation = models.TextField('Сформированность компетенций', blank=True)
    additional_info = models.TextField('Дополнительная информация', blank=True)
    
    # Результат
    result = models.TextField('Результат практической подготовки', blank=True, default='Программа практической подготовки выполнена в полном объеме')
    
    # Дата составления
    document_date = models.DateField('Дата составления документа', null=True, blank=True)
    
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    
    class Meta:
        db_table = 'practice_documents'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'{self.get_practice_type_display()} - {self.fio} - {self.created_at.date()}'


class CharacteristicDocument(models.Model):
    """Модель для документа Характеристика"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='characteristics')
    
    # Основные данные
    fio = models.CharField('ФИО практиканта', max_length=200, blank=True)
    library = models.CharField('Подразделение, должность', max_length=300, blank=True)
    
    # Даты работы
    work_start = models.DateField('Дата начала работы', null=True, blank=True)
    work_end = models.DateField('Дата окончания работы', null=True, blank=True)
    
    # Количество выходов
    work_days_count = models.IntegerField('Количество выходов на работу', null=True, blank=True)
    missed_days = models.IntegerField('Пропущено дней', null=True, blank=True)
    missed_unexcused = models.IntegerField('Пропущено по неуважительной причине', null=True, blank=True)
    
    # Специальность
    speciality = models.CharField('Специальность', max_length=200, blank=True)
    
    # Качество работы
    work_quality = models.TextField('Качество выполнения работы', blank=True)
    
    # Руководитель
    supervisor = models.CharField('Руководитель практики от организации', max_length=200, blank=True)
    
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    
    class Meta:
        db_table = 'characteristic_documents'
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Характеристика - {self.fio} - {self.created_at.date()}'


class Document(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    
    class Meta:
        db_table = 'document'
    
    def __str__(self):
        return self.name


# ИСПРАВЛЕННЫЕ СИГНАЛЫ - ТОЛЬКО ОДИН!
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создает профиль при создании пользователя"""
    if created:
        UserProfile.objects.create(user=instance)



class DocTemplate(models.Model):
    """Шаблон документа (.docx), загружаемый администратором."""
    TEMPLATE_TYPES = [
        ('harakteristika',            'Характеристика'),
        ('attestat_uchebnaya',        'Аттестационный лист — Учебная практика'),
        ('attestat_proizvodstvennaya','Аттестационный лист — Производственная практика'),
    ]

    template_type = models.CharField(
        'Тип шаблона', max_length=40, choices=TEMPLATE_TYPES, unique=True
    )
    file = models.FileField(
        'Файл шаблона (.docx)',
        upload_to='doc_templates/',
        help_text='Загрузите .docx файл с плейсхолдерами вида {{fio}}'
    )
    description = models.TextField('Описание', blank=True)
    uploaded_at  = models.DateTimeField('Дата загрузки', auto_now=True)
    uploaded_by  = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name='Кто загрузил', related_name='uploaded_templates'
    )

    class Meta:
        db_table = 'doc_templates'
        verbose_name = 'Шаблон документа'
        verbose_name_plural = 'Шаблоны документов'

    def __str__(self):
        return self.get_template_type_display()

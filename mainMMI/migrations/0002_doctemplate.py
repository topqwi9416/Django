from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainMMI', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DocTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_type', models.CharField(
                    choices=[
                        ('harakteristika', 'Характеристика'),
                        ('attestat_uchebnaya', 'Аттестационный лист — Учебная практика'),
                        ('attestat_proizvodstvennaya', 'Аттестационный лист — Производственная практика'),
                    ],
                    max_length=40,
                    unique=True,
                    verbose_name='Тип шаблона'
                )),
                ('file', models.FileField(
                    help_text='Загрузите .docx файл с плейсхолдерами вида {{fio}}',
                    upload_to='doc_templates/',
                    verbose_name='Файл шаблона (.docx)'
                )),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('uploaded_at', models.DateTimeField(auto_now=True, verbose_name='Дата загрузки')),
                ('uploaded_by', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    related_name='uploaded_templates',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='Кто загрузил'
                )),
            ],
            options={
                'verbose_name': 'Шаблон документа',
                'verbose_name_plural': 'Шаблоны документов',
                'db_table': 'doc_templates',
            },
        ),
    ]

# Generated by Django 3.0.4 on 2022-03-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id_course', models.AutoField(primary_key=True, serialize=False)),
                ('name_course', models.CharField(max_length=60, unique=True, verbose_name='Asignatura')),
                ('description', models.TextField(blank=True, default='Lorem ipsum, dolor sit amet consectetur adipisicing elit. Iusto, earum possimus.\nNisi numquam quibusdam deserunt nam sequi mollitia cumque quisquam possimus illum?Expedita.', null=True, verbose_name='Descripcion de la Asignatura')),
            ],
            options={
                'verbose_name': 'Asignatura',
                'verbose_name_plural': 'Asignaturas',
                'db_table': 'quiz_course',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id_question', models.AutoField(primary_key=True, serialize=False)),
                ('question_name', models.CharField(max_length=250, verbose_name='Pregunta')),
                ('image', models.URLField(blank=True, null=True, verbose_name='Imagen')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
                'db_table': 'quiz_question',
            },
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id_theme', models.AutoField(primary_key=True, serialize=False)),
                ('name_theme', models.CharField(max_length=80, verbose_name='Tema')),
                ('id_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.Course', verbose_name='Asignatura')),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
                'db_table': 'quiz_theme',
            },
        ),
        migrations.CreateModel(
            name='QuestionItem',
            fields=[
                ('id_question_item', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120, verbose_name='Respuesta')),
                ('correct', models.BooleanField(blank=True, default=False, null=True, verbose_name='Correcta')),
                ('id_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Pregunta', to='quiz.Question')),
            ],
            options={
                'verbose_name': 'Question Item',
                'verbose_name_plural': 'Question Items',
                'db_table': 'quiz_question_item',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='id_theme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Tema', to='quiz.Theme'),
        ),
    ]
# Generated by Django 5.1.4 on 2024-12-08 03:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('explicacao', models.TextField(null=True)),
                ('area_conhecimento', models.CharField(choices=[('H', 'Ciências Humanas e suas Tecnologias'), ('L', 'Linguagens, Códigos e suas Tecnologias'), ('B', 'Ciências da Natureza e suas Tecnologias'), ('E', 'Matemática e suas Tecnologias')], max_length=1)),
                ('valor', models.FloatField(default=1.0)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Opcoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('opcao_correta', models.BooleanField(default=False)),
                ('explicacao', models.TextField(null=True)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.questoes')),
            ],
        ),
        migrations.CreateModel(
            name='Simulados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(max_length=150)),
                ('data_inicio', models.DateField(null=True)),
                ('data_fim', models.DateField(null=True)),
                ('professor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SimuladoQuestao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.questoes')),
                ('simulado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.simulados')),
            ],
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escola', models.CharField(max_length=150)),
                ('serie', models.CharField(max_length=50)),
                ('turno', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], max_length=1)),
                ('ano', models.SmallIntegerField()),
                ('professor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TurmaAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='aluno', to=settings.AUTH_USER_MODEL)),
                ('turma', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.turmas')),
            ],
        ),
        migrations.AddField(
            model_name='simulados',
            name='turma',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='area_professor.turmas'),
        ),
        migrations.CreateModel(
            name='RespostaSimulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acertou', models.BooleanField(default=False)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.opcoes')),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.questoes')),
                ('simulado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='area_professor.simulados')),
                ('turma', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='area_professor.turmas')),
            ],
        ),
    ]

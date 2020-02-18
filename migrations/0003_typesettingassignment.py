# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-02-07 11:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0033_set_default_xml_galley_xsl'),
        ('typesetting', '0002_typesettinground'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypesettingAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assigned', models.DateTimeField(default=django.utils.timezone.now)),
                ('notified', models.BooleanField(default=False)),
                ('accepted', models.DateTimeField(blank=True, null=True)),
                ('due', models.DateField(null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('reviewed', models.BooleanField(default=False)),
                ('review_decision', models.CharField(choices=[('accept', 'Accept'), ('corrections', 'Corrections Required'), ('proofing', 'Proofing Required')], max_length=21)),
                ('task', models.TextField(null=True, verbose_name='Typesetting Task')),
                ('typesetter_note', models.TextField(blank=True, verbose_name='Note to Editor')),
                ('files_to_typeset', models.ManyToManyField(blank=True, related_name='files_to_typeset', to='core.File')),
                ('galleys_created', models.ManyToManyField(blank=True, to='core.Galley')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='manager', to=settings.AUTH_USER_MODEL)),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='typesetting.TypesettingRound')),
                ('typesetter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='typesetter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
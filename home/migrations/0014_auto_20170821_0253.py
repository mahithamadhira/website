# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import home.models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0039_collectionviewrestriction'),
        ('home', '0013_roundpage_internannounce'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityMentorInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255, verbose_name='Mentor name')),
                ('email', models.EmailField(max_length=254, verbose_name='Mentor email')),
                ('token', models.CharField(default=home.models.mentor_id, max_length=42, unique=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommunityPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('community_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='communitymentorinvite',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentors', to='home.CommunityPage'),
        ),
    ]

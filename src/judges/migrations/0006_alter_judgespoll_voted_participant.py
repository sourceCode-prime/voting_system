# Generated by Django 3.2.3 on 2021-06-10 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0015_participantpolls_project_link'),
        ('judges', '0005_alter_judgespoll_voted_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='judgespoll',
            name='voted_participant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='participants.participantpolls'),
        ),
    ]

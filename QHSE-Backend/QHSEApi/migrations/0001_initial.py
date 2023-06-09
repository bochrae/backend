# Generated by Django 3.2.2 on 2023-03-24 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id_commande', models.AutoField(primary_key=True, serialize=False)),
                ('date_commande', models.DateTimeField()),
                ('type_commande', models.CharField(max_length=50)),
                ('etat_commande', models.CharField(max_length=50)),
                ('quantite', models.IntegerField()),
                ('specificite_regime', models.CharField(max_length=50)),
                ('specificite_texture', models.CharField(max_length=50)),
                ('type_auth', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FicheTechnique',
            fields=[
                ('id_fiche', models.AutoField(primary_key=True, serialize=False)),
                ('url_fiche', models.CharField(max_length=255)),
                ('nom_fiche', models.CharField(max_length=255)),
                ('type_plat', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 2.2.1 on 2019-06-12 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Affaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name="Code de l'affaire")),
                ('nom', models.CharField(max_length=100, verbose_name='Nom du chantier')),
                ('adresse_1', models.CharField(max_length=200, verbose_name='Adresse du chantier')),
                ('adresse_2', models.CharField(max_length=200, verbose_name="Complément d'adresse")),
                ('cp', models.CharField(max_length=10, verbose_name='Code postal')),
                ('commune', models.CharField(max_length=100, verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='BonLivraison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=25, verbose_name='Numéro du BL')),
                ('date', models.DateField(verbose_name="Date d'émission du BL")),
                ('affaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.Affaire')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name="Code d'identification du client")),
                ('nom', models.CharField(max_length=100, verbose_name="Nom de l'entreprise")),
                ('etablissement', models.CharField(max_length=100, verbose_name="Nom de l'établissement")),
                ('adresse_siege_1', models.CharField(max_length=200, verbose_name='Adresse du siège')),
                ('adresse_siege_2', models.CharField(max_length=200, verbose_name="Complément d'adresse")),
                ('cp_siege', models.CharField(max_length=10, verbose_name='Code postal')),
                ('commune_siege', models.CharField(max_length=100, verbose_name='Commune')),
                ('adresse_fact_1', models.CharField(max_length=200, verbose_name='Adresse de facturation')),
                ('adresse_fact_2', models.CharField(max_length=200, verbose_name="Complément d'adresse")),
                ('cp_fact', models.CharField(max_length=10, verbose_name='Code postal')),
                ('commune_fact', models.CharField(max_length=100, verbose_name='Commune')),
            ],
        ),
        migrations.CreateModel(
            name='Fournisseur',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15, verbose_name='Code ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom du fournisseur')),
                ('etablissement', models.CharField(max_length=100, verbose_name='Etablissement')),
            ],
        ),
        migrations.CreateModel(
            name='Formule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denomination', models.CharField(max_length=100)),
                ('resistance', models.FloatField()),
                ('fournisseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.Fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_bl', models.DateField(verbose_name="Date de l'épreuve")),
                ('d1', models.FloatField(verbose_name='1ère mesure de diamètre (mm)')),
                ('d2', models.FloatField(verbose_name='2ème mesure de diamètre (mm)')),
                ('d3', models.FloatField(verbose_name='3ème mesure de diamètre (mm)')),
                ('rc1', models.FloatField(verbose_name='1ère résistance (MPa)')),
                ('rc2', models.FloatField(verbose_name='3ème éprouvette')),
                ('num_bl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.BonLivraison')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom')),
                ('prenom', models.CharField(max_length=100, verbose_name='Prénom')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse e-mail')),
                ('telephone', models.CharField(max_length=15, verbose_name='Numéro de téléphone')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.Client')),
            ],
        ),
        migrations.AddField(
            model_name='bonlivraison',
            name='formule',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.Formule'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easyreport.Client'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='contact',
            field=models.ManyToManyField(to='easyreport.Contact'),
        ),
        migrations.AddField(
            model_name='affaire',
            name='formule',
            field=models.ManyToManyField(to='easyreport.Formule'),
        ),
    ]
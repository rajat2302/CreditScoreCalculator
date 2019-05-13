# Generated by Django 2.2 on 2019-04-30 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footprint',
            name='bill_amt1',
            field=models.IntegerField(default=0, help_text='1st Loan amount'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_0',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='1st Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_1',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_2',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_3',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_4',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_5',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (7, 'Paid after 7 month'), (1, 'Paid after 1 month'), (4, 'Paid after 4 month'), (0, 'Paid on time'), (2, 'Paid after 2 month'), (3, 'Paid after 3 month'), (-1, 'Paid before time'), (5, 'Paid after 5 month')], default=-1, help_text='2nd Loan status'),
        ),
    ]

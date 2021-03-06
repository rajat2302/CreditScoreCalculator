# Generated by Django 2.2 on 2019-05-01 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20190501_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt10',
            new_name='pay_amt1',
        ),
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt11',
            new_name='pay_amt2',
        ),
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt12',
            new_name='pay_amt3',
        ),
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt7',
            new_name='pay_amt4',
        ),
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt8',
            new_name='pay_amt5',
        ),
        migrations.RenameField(
            model_name='footprint',
            old_name='bill_amt9',
            new_name='pay_amt6',
        ),
        migrations.AddField(
            model_name='creditscore',
            name='potential_defaulter',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_0',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='1st Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_1',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_2',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_3',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_4',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='2nd Loan status'),
        ),
        migrations.AlterField(
            model_name='footprint',
            name='pay_5',
            field=models.IntegerField(choices=[(8, 'Paid after 8 month'), (6, 'Paid after 6 month'), (3, 'Paid after 3 month'), (2, 'Paid after 2 month'), (4, 'Paid after 4 month'), (7, 'Paid after 7 month'), (0, 'Paid on time'), (-1, 'Paid before time'), (5, 'Paid after 5 month'), (1, 'Paid after 1 month')], default=-1, help_text='2nd Loan status'),
        ),
    ]

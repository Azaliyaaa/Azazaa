from _future_ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20160921_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(help_text='Enter a brief description of the book', max_length=200),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(help_text='Enter a book category - e.g. Science Fiction, Non Fiction etc.', max_length=200),
        ),
    ]
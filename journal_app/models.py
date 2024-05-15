from django.db import models

# Create your models here.
class TagsModel(models.Model):
    tag_name_uz=models.CharField(max_length=222)
    tag_name_en=models.CharField(max_length=222)

    def __str__(self):
        return self.tag_name_uz

    class Meta:
        verbose_name='Tags'
        db_table='Tags_table'


class JournalModel(models.Model):
    journal_logo = models.ImageField(upload_to='journal_logos/')
    journal_desc_uz = models.TextField()
    journal_desc_en = models.TextField()
    journal_date=models.DateTimeField(auto_now_add=True)
    journal_tags = models.ManyToManyField(TagsModel)

    def __str__(self):
        return self.journal_desc_uz

    class Meta:
        ordering=['-journal_date']
        verbose_name='Journals'
        db_table='Journal_table'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Media(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    media_type = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    short_name = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    review_url = models.CharField(max_length=255, blank=True, null=True)
    review_score = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    genres = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    published_by = models.TextField(blank=True, null=True)  # This field type is a guess.
    franchises = models.TextField(blank=True, null=True)  # This field type is a guess.
    regions = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'media'
        
    def __str__(self):
        return self.name
    
    
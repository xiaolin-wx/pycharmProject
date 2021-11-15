# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TbAdmin(models.Model):
    username = models.CharField(max_length=64, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_admin'


class TbClass(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    isdele = models.IntegerField(db_column='isDele', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_class'


class TbMark(models.Model):
    english = models.IntegerField(db_column='English', blank=True, null=True)  # Field name made lowercase.
    python = models.IntegerField(blank=True, null=True)
    calculus = models.IntegerField(db_column='Calculus', blank=True, null=True)  # Field name made lowercase.
    statistics = models.IntegerField(db_column='Statistics', blank=True, null=True)  # Field name made lowercase.
    stu_id = models.IntegerField(blank=True, null=True)
    rpt_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_mark'


class TbReport(models.Model):
    class_id = models.IntegerField(blank=True, null=True)
    topic = models.CharField(max_length=128, blank=True, null=True)
    isdele = models.IntegerField(db_column='isDele', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_report'


class TbStudent(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    sex = models.IntegerField(blank=True, null=True)
    class_id = models.IntegerField(blank=True, null=True)
    p_id = models.IntegerField(blank=True, null=True)
    isdele = models.IntegerField(db_column='isDele')  # Field name made lowercase.
    tel = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_student'

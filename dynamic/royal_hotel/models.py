from django.db import models

class Speciality(models.Model):
    s_image_icon = models.ImageField(upload_to='img/')
    s_image = models.ImageField(upload_to='img/')
    s_title = models.CharField(max_length=20)
    s_content = models.TextField(max_length=500)

class Meal(models.Model):
    m_image = models.ImageField(upload_to='img/')
    m_title = models.CharField(max_length=20)
    m_price = models.IntegerField(null=False)

class Gallery(models.Model):
    g_image = models.ImageField(upload_to='img/')
    g_title = models.CharField(max_length=20)
    g_content = models.TextField(max_length=500)

class Feedback(models.Model):
    f_image = models.ImageField(upload_to='img/')
    f_name = models.TextField(max_length=10)
    f_content = models.TextField(max_length=550)
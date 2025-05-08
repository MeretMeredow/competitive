from django.db import models
from django.core.exceptions import ValidationError


class Role(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Rollar'

class Group(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/groups')
    point_num = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Topar'
        verbose_name_plural = 'Toparlar'

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='img/users')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ulanyjy'
        verbose_name_plural = 'Ulanyjylar'

def validate_year(value):
    if value <= 2024:
        raise ValidationError(f'{value} bu ýyl dogry däl.')

class Season(models.Model):
    year = models.IntegerField(validators=[validate_year])
    party_num = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.year} ý | tapgyr {self.party_num}"

    class Meta:
        verbose_name = 'Tapgyr'
        verbose_name_plural = 'Tapgyrlar'
        ordering='-year','-party_num'

class Compatition(models.Model):
    theme = models.TextField()
    start_time = models.DateTimeField('Başlaýan Wagty')
    season_id = models.ForeignKey(Season, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Bäsleşik'
        verbose_name_plural = 'Bäsleşikler'

class Question(models.Model):
    question = models.TextField()
    question_num = models.IntegerField()
    time = models.TimeField()
    compatition_id = models.ForeignKey(Compatition, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
            return f"Sorag: {self.question_num} | Tema: {self.compatition_id}"

    class Meta:
        verbose_name = 'Sorag'
        verbose_name_plural = 'Soraglar'
        ordering = 'question_num','-compatition_id'

class Result(models.Model):
    answer = models.TextField()
    assess = models.IntegerField(null=True, blank=True)
    group_id = models.OneToOneField(
        Group, on_delete=models.CASCADE,
        primary_key=True
    )
    # group_id = models.ManyToManyField(Group)
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.answer

    class Meta:
        verbose_name = 'Result'
        verbose_name_plural = 'Results'
        ordering = '-assess', '-created_at'
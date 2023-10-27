from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Skill(models.Model):
    name = models.CharField(max_length=200)
    index = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.index}: {self.name}"


class Child(models.Model):
    MALE = 'chłopiec'
    FEMALE = 'dziewczynka'
    
    GENDER_CHOICES = [
        (MALE, 'chłopiec'),
        (FEMALE, 'dziewczynka'),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES
    )
    skill = models.ManyToManyField(Skill, through='ChildSkill')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Children"


class Description(models.Model):
    text = models.TextField(max_length=500)
    child = models.OneToOneField(Child, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.child}'s description"


class ChildSkill(models.Model):
    # BEGINNER = '0'
    # INTERMEDIATE = '1'
    # ADVANCED = '2'

    # GRADE_CHOICES = [
    #     (BEGINNER, '0'),
    #     (INTERMEDIATE, '1'),
    #     (ADVANCED, '2'),
    # ]
    
    child = models.ForeignKey(Child, on_delete=models.SET_NULL, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)
    # grade = models.CharField(max_length=1,choices=GRADE_CHOICES, null=True)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(2)], null=True)


    class Meta:
        unique_together = (('child', 'skill'),)
    
    def __str__(self):
        return f"{self.child} - {self.skill} - {self.grade}"


class ResponseText(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)
    grade = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(2)], null=True)
    response_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.skill} - {self.grade} - {self.response_text}"
from django.db import models


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
    short_name = models.CharField(max_length=30)
    gender = models.CharField(
        max_length=15,
        choices=GENDER_CHOICES
    )
    skill = models.ManyToManyField(Skill, through='ChildSkill')
    description = models.TextField(max_length=5000, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Children"


class ChildSkill(models.Model):

    GRADE_CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
    ]
    grade = models.IntegerField(max_length=1, choices=GRADE_CHOICES, null=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True)
    skill = models.ForeignKey(Skill, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = (('child', 'skill'),)
    
    def __str__(self):
        return f"{self.child} - {self.skill} - {self.grade}"


class ResponseText(models.Model):

    GRADE_CHOICES = [
        (0, "0"),
        (1, "1"),
        (2, "2"),
    ]
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, null=True)    
    grade = models.IntegerField(max_length=1, choices=GRADE_CHOICES, null=True)
    response_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"{self.skill} - {self.grade} - {self.response_text}"
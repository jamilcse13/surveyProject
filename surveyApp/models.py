from django.db import models

# Create your models here.
class Survey(models.Model):
    title = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.title}"

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    surveys = models.ManyToManyField(Survey)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Question(models.Model):
    question = models.CharField(max_length=150)
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.question}, {self.survey_id}"

class Option(models.Model):
    name = models.CharField(max_length=100)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.name}, {self.question_id}"

class Answer(models.Model):
    option_id = models.ForeignKey(Option, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']
    
    def __str__(self):
        return f"{self.option_id}, {self.question_id}, {self.customer_id}"
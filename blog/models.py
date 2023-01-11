from django.db import models
<<<<<<< HEAD
# note that im useing the Django inbuild user model
class account(models.Model):
    id = models.AutoField(primary_key= True, unique=True)
    name = models.CharField(unique=True, max_length=50)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    display_photo = models.ImageField(upload_to="templates/images/", null=True, blank=True)
    bio_data = models.CharField(max_length=1000)
    """
    note the user is from django builtin user model
    i'm using foreignkey which allows one user to have many account
"""
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class blogposts(models.Model):
    id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=500)
    blog_description = models.TextField()
    content = models.TextField
    blogpostscol = models.CharField(max_length=45)
    account_name = models.ForeignKey('account.name',on_delete=models.CASCADE)
=======
from accounts.models import Account

""" Stori """
""" stori_status """
STATUS = (
    (0,"Draft"),
    (1,"Published")
)
"""stori is swahili for story. was thinking of using the slang version 'risto'/'riba' in there.. """
class Stori(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    content = models.TextField()
    created_by = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0) #"""This here serves to indicate whether a stori has been published or not."""
    #category 
    

    def __str__(self):
         return f'{self.title} created by: {self.created_by}'
         
    class Meta:
        verbose_name_plural = "Mastori"
>>>>>>> 8ce82b1617a8a6a591be01f5ce3a8b45161dde50

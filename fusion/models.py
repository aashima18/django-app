from django.db import models
from django.contrib.auth.models import User












class Headings(models.Model):
    Services=models.CharField(max_length=20, help_text='Enter heading')
    About=models.CharField(max_length=20, help_text='Enter heading')
    Features=models.CharField(max_length=20, help_text='Enter heading')
    Team=models.CharField(max_length=20, help_text='Enter heading')
    Pricing=models.CharField(max_length=20, help_text='Enter heading')
    Contact=models.CharField(max_length=20, help_text='Enter heading')


    def __str__(self):
        return self.Services   

class Home(models.Model):
    objects = models.Manager()
    Heading=models.CharField(max_length=200, help_text='Enter heading')
    description=models.CharField(max_length=200, help_text='Enter heading')
    image=models.ImageField(upload_to='images/') 


    def __str__(self):
        return self.Heading   






icon_ch=(
        ('lni-cog', 'settings'),
        ('lni-stats-up', 'design'),
        ('lni-users', 'customize'),
        ('lni-layers', 'ui'),
        ('lni-mobile', 'app'),
        ('lni-rocket', 'ufrnd'),
        )


class Services(models.Model):
    objects = models.Manager()
    icons=models.CharField(choices=icon_ch,max_length=100)
    name= models.CharField(max_length=50, help_text='Enter heading')
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    def __str__(self):
        return self.name


class About(models.Model):
    objects = models.Manager()
    p1 = models.CharField(max_length=20,help_text='Enter small text')
    image=models.ImageField(upload_to='images/') 
    Tittle= models.CharField(max_length=200, help_text='Enter Tittle')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')      
    def __str__(self):
        return self.Tittle

                                                                    
icon_ch1=(
        ('lni-rocket', 'rocket'),
        ('lni-laptop-phone', 'phone'),
        ('lni-cog', 'setting'),
        ('lni-leaf', 'leaf'),
        ('lni-layers', 'layers'),
       
        )



class Features(models.Model): 
    objects = models.Manager()       
    Title= models.CharField(max_length=20, help_text='Enter Tittle')
    des = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    icons=models.CharField(choices=icon_ch1,max_length=100)
    def __str__(self):
         return self.Title    

class Featuresimg(models.Model):
       objects = models.Manager()
       Titl= models.CharField(max_length=20, help_text='Enter Tittle')       
       img=models.ImageField(upload_to='images/')   
       def __str__(self):
         return self.Titl   

class Featuresrght(models.Model): 
    objects = models.Manager()       
    Title= models.CharField(max_length=20, help_text='Enter Tittle')
    des = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    icons=models.CharField(choices=icon_ch1,max_length=100)
    def __str__(self):
         return self.Title   





icon_ch2=(
        ('lni-instagram-filled', 'insta'),
        ('lni-facebook-filled', 'facebook'),
        ('lni-instagram-filled', 'twitter'),
        )

 

class Team(models.Model):  
    objects = models.Manager() 
    img1=models.ImageField(upload_to='images/') 
    name1= models.CharField(max_length=200, help_text='Enter Tittle')
    Title1= models.CharField(max_length=200, help_text='Enter Tittle')
    des1 = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    icons1=models.CharField(choices=icon_ch2,max_length=200)
    icons12=models.CharField(choices=icon_ch2,max_length=200)
    icons13=models.CharField(choices=icon_ch2,max_length=200)
    def __str__(self):
        return self.name1        



icon_ch3=(
        ('lni-package', 'insta'),
        ('lni-drop', 'facebook'),
        ('lni-star', 'twitter'),
        )


class Pricing(models.Model): 
    objects = models.Manager()   
    icons2=models.CharField(choices=icon_ch3,max_length=100)
    price= models.IntegerField( help_text='Enter price')
    Title2= models.CharField(max_length=20, help_text='Enter Tittle')
    details = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
   
    def __str__(self):
        return self.Title2      



class Testimonial(models.Model): 
    objects = models.Manager()    
    img2=models.ImageField(upload_to='images/') 
    name2= models.CharField(max_length=20, help_text='Enter Tittle')
    Title3= models.CharField(max_length=20, help_text='Enter Tittle')
    des3 = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    
    def __str__(self):
         return self.name2           

class Feedback(models.Model):
    objects = models.Manager()
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField(max_length=200)
    def __str__(self):
        return self.name

class Footer(models.Model):
    objects = models.Manager()   
    h = models.CharField(max_length=20)
    d = models.TextField(max_length=1000) 
    def __str__(self):
        return self.h       


class Footer1(models.Model):
    objects = models.Manager()   
    img5 = models.ImageField(upload_to='images/')
    p = models.TextField(max_length=1000, help_text='Enter a brief description')  
    def __str__(self):
         return self.p          

class FooterContact(models.Model):
    objects = models.Manager() 
    h = models.CharField(max_length=20)  
    address = models.CharField(max_length=2000)
    phono = models.IntegerField() 
    email= models.EmailField(max_length=1000) 
    def __str__(self):
        return self.h            

class Copyright(models.Model):
        objects = models.Manager()
        title = models.CharField(max_length=2000)
        link= models.CharField(max_length=1000) 
        name = models.CharField(max_length=20)          
        def __str__(self):
                return self.name 
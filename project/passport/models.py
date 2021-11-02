from django.db import models





class Customer(models.Model):
    """
    Customer model:
            Name
            Surname
            Email
            Phone
    """

    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

    
    def __str__(self):
        return f"{self.name} {self.surname} tel: {self.phone}"

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

class Passport(models.Model):
    """
    one user can have several passports


    Passport model :
        Scan file
        Document number
        First name
        Last name
        Patronymic
        Nationality
        Birth date
        Personal number
        Gender
        Issue date
        Expire date
        Issuing authority
    """


    GENDER_CHOICES = (
        (1,'Male'),
        (2,'Female'),
    )   

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE, 
                                        verbose_name='Passport',
                                        related_name='passports',)  

    scan = models.FileField(upload_to='passports',
                            verbose_name='Passport Scan')
    document = models.CharField(max_length=15,
                                verbose_name='Document ID')
    first_name = models.CharField(max_length=20,
                                verbose_name='First name')
    last_name = models.CharField(max_length=20,
                                verbose_name='Last name')
    patronymic = models.CharField(max_length=20,
                                verbose_name='Patronymic')
    nationality = models.CharField(max_length=20,
                                verbose_name='Nationality')
    birth = models.DateField(verbose_name='Birthday date')
    personal = models.CharField(max_length=20,
                                verbose_name="Personal ID",
                                unique=True)
    gender = models.IntegerField(verbose_name='Gender',
                                choices=GENDER_CHOICES)
    issue_date = models.DateField(verbose_name='Issue date')
    expire_date = models.DateField(verbose_name='Expire date')
    issuing_authority = models.CharField(max_length=35,
                                verbose_name="Issuing authority")

    def __str__(self):
        return f'{self.customer}-{self.personal}'


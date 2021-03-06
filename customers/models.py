from django.db import models

class Company(models.Model):
    INDEX_NAME_CHOICES = (
        ( 1, 'あ行'),
        ( 2, 'か行'),
        ( 3, 'さ行'),
        ( 4, 'た行'),
        ( 5, 'な行'),
        ( 6, 'は行'),
        ( 7, 'ま行'),
        ( 8, 'や行'),
        ( 9, 'ら行'),
        (10, 'わ行'),
        ( 0, 'その他'),
    )
    name = models.CharField('会社名',max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    short_name = models.CharField('略称',max_length=255,null=True,blank=True)
    index_name = models.SmallIntegerField('頭文字',choices=INDEX_NAME_CHOICES,default=1)
    zip_code = models.CharField('郵便番号',max_length=255,null=True,blank=True)
    address_1 = models.CharField('住所',max_length=255,null=True,blank=True)
    address_2 = models.CharField('',max_length=255,null=True,blank=True)
    address_3 = models.TextField('',null=True,blank=True)
    telephone_number_1 = models.CharField('電話番号',max_length=255,null=True,blank=True)
    telephone_number_2 = models.CharField('',max_length=255,null=True,blank=True)
    fax_number = models.CharField('FAX番号',max_length=255,null=True,blank=True)
    mail_address = models.CharField('メールアドレス',max_length=255,null=True,blank=True)
    note = models.TextField('備考',null=True,blank=True)
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'

    def __str__(self):
        return self.name

    def address(self):
        add1 = []
        if self.zip_code is not None: add1.append(self.zip_code)
        if self.address_1 is not None: add1.append(self.address_1) 
        if self.address_2 is not None: add1.append(self.address_2) 
        add2 = []
        if len(add1) > 0: add2.append(" ".join(add1))
        if self.address_3 is not None: add2.append(self.address_3)
        return "\n".join(add2)

class Section(models.Model):
    company = models.ForeignKey(Company,on_delete=models.PROTECT,verbose_name='会社名')
    name = models.CharField('部署名',max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    zip_code = models.CharField('郵便番号',max_length=255,null=True,blank=True)
    address_1 = models.CharField('住所',max_length=255,null=True,blank=True)
    address_2 = models.CharField('',max_length=255,null=True,blank=True)
    address_3 = models.TextField('',null=True,blank=True)
    telephone_number_1 = models.CharField('電話番号',max_length=255,null=True,blank=True)
    telephone_number_2 = models.CharField('',max_length=255,null=True,blank=True)
    fax_number = models.CharField('FAX番号',max_length=255,null=True,blank=True)
    mail_address = models.CharField('メールアドレス',max_length=255,null=True,blank=True)
    note = models.TextField('備考',null=True,blank=True)
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.name

class Person(models.Model):
    company = models.ForeignKey(Company,on_delete=models.PROTECT,verbose_name='会社名')
    section = models.ForeignKey(Section,on_delete=models.SET_NULL,blank=True,null=True,verbose_name='部署名')
    name = models.CharField('担当者名',max_length=255)
    search_name = models.CharField(max_length=255,null=True)
    zip_code = models.CharField('郵便番号',max_length=255,null=True,blank=True)
    address_1 = models.CharField('住所',max_length=255,null=True,blank=True)
    address_2 = models.CharField('',max_length=255,null=True,blank=True)
    address_3 = models.TextField('',null=True,blank=True)
    telephone_number_1 = models.CharField('電話番号',max_length=255,null=True,blank=True)
    telephone_number_2 = models.CharField('',max_length=255,null=True,blank=True)
    fax_number = models.CharField('FAX番号',max_length=255,null=True,blank=True)
    mail_address = models.CharField('メールアドレス',max_length=255,null=True,blank=True)
    fax_number = models.CharField('FAX番号',max_length=255,null=True,blank=True)
    mail_address = models.CharField('メールアドレス',max_length=255,null=True,blank=True)
    person_role_name = models.CharField('役職名',max_length=255,null=True,blank=True)
    retier_flg = models.BooleanField('退職',default=False)
    retier_date = models.DateField('退職日',null=True,blank=True)
    note = models.TextField('備考',null=True,blank=True)
    delete_flg = models.BooleanField(default=False)
    create_user = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    update_user = models.CharField(max_length=255)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return self.name

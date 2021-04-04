from django.db import models


class Campsite(models.Model):
    campsite_id = models.AutoField(primary_key=True)
    campsite_name = models.CharField(max_length=30)
    lineintro = models.CharField(max_length=100, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    featureNmV = models.TextField(db_column='featureNmV', blank=True, null=True)  # Field name made lowercase.
    lctCI = models.CharField(db_column='lctCl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doNm = models.CharField(db_column='doNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sigunguNm = models.CharField(db_column='sigunguNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    addr2 = models.CharField(max_length=30, blank=True, null=True)
    mapX = models.CharField(db_column='mapX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mapY = models.CharField(db_column='mapY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(max_length=300, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    resveUrl = models.TextField(db_column='resveUrl', blank=True, null=True)  # Field name made lowercase.
    resveCl = models.CharField(db_column='resveCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    autoSiteCo = models.CharField(db_column='autoSiteCo', max_length=5)  # Field name made lowercase.
    glampSiteCo = models.CharField(db_column='glampSiteCo', max_length=5)  # Field name made lowercase.
    caravSiteCo = models.CharField(db_column='caravSiteCo', max_length=5)  # Field name made lowercase.
    tooltip = models.TextField(blank=True, null=True)
    glampInnerFclty = models.CharField(db_column='glampInnerFclty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caravInnerFclty = models.CharField(db_column='caravInnerFclty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operPdCl = models.CharField(db_column='operPdCl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operDeCl = models.CharField(db_column='operDeCl', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trlerAcmpnyAt = models.CharField(db_column='trlerAcmpnyAt', max_length=5)  # Field name made lowercase.
    brazierCl = models.CharField(db_column='brazierCl', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sbrsEtc = models.CharField(db_column='sbrsEtc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posblFcltyCl = models.CharField(db_column='posblFcltyCl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    posblFcltyEtc = models.CharField(db_column='posblFcltyEtc', max_length=300, blank=True, null=True)  # Field name made lowercase.
    clturEventAt = models.CharField(db_column='clturEventAt', max_length=5)  # Field name made lowercase.
    clturEvent = models.CharField(db_column='clturEvent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    exprnProgrmAt = models.CharField(db_column='exprnProgrmAt', max_length=5)  # Field name made lowercase.
    exprnProgrm = models.CharField(db_column='exprnProgrm', max_length=300, blank=True, null=True)  # Field name made lowercase.
    themaEnvrnCl = models.CharField(db_column='themaEnvrnCl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    eqpmnLendCl = models.CharField(db_column='eqpmnLendCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    animalCmgCl = models.CharField(db_column='animalCmgCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firstImageUrlV = models.CharField(db_column='firstImageUrlV', max_length=300, blank=True, null=True)  # Field name made lowercase.
    likeCount = models.IntegerField(db_column='likeCount')  # Field name made lowercase.
    outRestroom = models.CharField(db_column='outRestroom', max_length=5)
    outShowerroom = models.CharField(db_column='outShowerroom', max_length=5)

    class Meta:
        managed = False
        db_table = 'Campsite'


class Sbrscl(models.Model):
    sbrscl_id = models.AutoField(db_column='sbrsCl_id', primary_key=True)  # Field name made lowercase.
    sbrscl_name = models.CharField(db_column='sbrsCl_name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SbrsCl'


class CampsiteSbrscl(models.Model):
    campsite_id = models.ForeignKey(Campsite, on_delete=models.CASCADE, db_column="campsite_id")
    sbrsCI_id = models.ForeignKey(Sbrscl, on_delete=models.CASCADE, db_column="sbrsCI_id")

    class Meta:
        managed = False
        db_table = 'Campsite_SbrsCl'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Tag'


class CampsiteTag(models.Model):
    campsite_id = models.ForeignKey(Campsite, on_delete=models.CASCADE, db_column="campsite_id")
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE, db_column="tag_id")

    class Meta:
        managed = False
        db_table = 'Campsite_Tag'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    admin = models.IntegerField(default=0)

    class Meta:
        managed = False
        db_table = 'User'


class Likes(models.Model):
    campsite_id = models.ForeignKey(Campsite, on_delete=models.CASCADE, db_column="campsite_id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")

    class Meta:
        managed = False
        db_table = 'Likes'


class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    campsite_id = models.ForeignKey(Campsite, on_delete=models.CASCADE, db_column="campsite_id")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "reviews", db_column="user_id")
    review = models.CharField(max_length=1000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'Reviews'


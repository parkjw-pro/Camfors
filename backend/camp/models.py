from django.db import models


class Campsite(models.Model):
    campsite_id = models.AutoField(primary_key=True)
    campsite_name = models.CharField(max_length=30)
    lineintro = models.CharField(max_length=100, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    featurenmv = models.TextField(db_column='featureNmV', blank=True, null=True)  # Field name made lowercase.
    indutyv = models.CharField(db_column='indutyV', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lctcl = models.CharField(db_column='lctCl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    donm = models.CharField(db_column='doNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sigungunm = models.CharField(db_column='sigunguNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    addr1 = models.CharField(max_length=50, blank=True, null=True)
    addr2 = models.CharField(max_length=30, blank=True, null=True)
    mapx = models.CharField(db_column='mapX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mapy = models.CharField(db_column='mapY', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(max_length=300, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)
    resveurl = models.TextField(db_column='resveUrl', blank=True, null=True)  # Field name made lowercase.
    resvecl = models.CharField(db_column='resveCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    gnrlsiteco = models.CharField(db_column='gnrlSiteCo', max_length=5)  # Field name made lowercase.
    autositeco = models.CharField(db_column='autoSiteCo', max_length=5)  # Field name made lowercase.
    glampsiteco = models.CharField(db_column='glampSiteCo', max_length=5)  # Field name made lowercase.
    caravsiteco = models.CharField(db_column='caravSiteCo', max_length=5)  # Field name made lowercase.
    tooltip = models.TextField(blank=True, null=True)
    glampinnerfclty = models.CharField(db_column='glampInnerFclty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    caravinnerfclty = models.CharField(db_column='caravInnerFclty', max_length=100, blank=True, null=True)  # Field name made lowercase.
    operpdcl = models.CharField(db_column='operPdCl', max_length=50, blank=True, null=True)  # Field name made lowercase.
    operdecl = models.CharField(db_column='operDeCl', max_length=30, blank=True, null=True)  # Field name made lowercase.
    trleracmpnyat = models.CharField(db_column='trlerAcmpnyAt', max_length=5)  # Field name made lowercase.
    braziercl = models.CharField(db_column='brazierCl', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sbrsetc = models.CharField(db_column='sbrsEtc', max_length=200, blank=True, null=True)  # Field name made lowercase.
    posblfcltycl = models.CharField(db_column='posblFcltyCl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    posblfcltyetc = models.CharField(db_column='posblFcltyEtc', max_length=300, blank=True, null=True)  # Field name made lowercase.
    cltureventat = models.CharField(db_column='clturEventAt', max_length=5)  # Field name made lowercase.
    clturevent = models.CharField(db_column='clturEvent', max_length=200, blank=True, null=True)  # Field name made lowercase.
    exprnprogrmat = models.CharField(db_column='exprnProgrmAt', max_length=5)  # Field name made lowercase.
    exprnprogrm = models.CharField(db_column='exprnProgrm', max_length=300, blank=True, null=True)  # Field name made lowercase.
    themaenvrncl = models.CharField(db_column='themaEnvrnCl', max_length=300, blank=True, null=True)  # Field name made lowercase.
    eqpmnlendcl = models.CharField(db_column='eqpmnLendCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    animalcmgcl = models.CharField(db_column='animalCmgCl', max_length=100, blank=True, null=True)  # Field name made lowercase.
    firstimageurlv = models.CharField(db_column='firstImageUrlV', max_length=300, blank=True, null=True)  # Field name made lowercase.
    likecount = models.IntegerField(db_column='likeCount')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Campsite'


class CampsiteSbrscl(models.Model):
    campsite_id = models.IntegerField()
    sbrscl_id = models.IntegerField(db_column='sbrsCl_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Campsite_SbrsCl'


class CampsiteTag(models.Model):
    campsite_id = models.IntegerField()
    tag_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Campsite_Tag'


class Likes(models.Model):
    campsite_id = models.IntegerField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Likes'


class Reviews(models.Model):
    campsite_id = models.IntegerField()
    user_id = models.IntegerField()
    review = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Reviews'


class Sbrscl(models.Model):
    sbrscl_id = models.AutoField(db_column='sbrsCl_id', primary_key=True)  # Field name made lowercase.
    sbrscl_name = models.CharField(db_column='sbrsCl_name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SbrsCl'


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'Tag'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    admin = models.IntegerField()
    birth = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'
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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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

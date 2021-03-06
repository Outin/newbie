from django.db import models


class Branch(models.Model):
    Name = models.CharField(max_length=10, primary_key=True, unique=True, verbose_name='经营机构')
    Area = models.CharField(max_length=10, verbose_name='地域')
    objects = models.Manager()

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "经营机构"
        verbose_name_plural = verbose_name


class Project(models.Model):
    ID = models.CharField(max_length=10, verbose_name='编号', primary_key=True)
    Name = models.CharField(max_length=50, verbose_name='项目名称')
    Branch = models.ForeignKey("Branch", null=True, on_delete=models.CASCADE,verbose_name='经营机构')
    Project_Type = (('直投类', '直投类'),('配资类', '配资类'),)
    Type = models.CharField(max_length=3, choices=Project_Type, verbose_name='类型')
    Approval_Form_Num = models.CharField(max_length=150, verbose_name='审批单号')
    Issue_Date = models.DateField(verbose_name='发行日期')
    Duration = models.IntegerField(verbose_name='期限')
    Amount = models.IntegerField(verbose_name='金额')
    Leverage_Ratio = models.DecimalField(verbose_name='杠杆率',max_digits=20,decimal_places=1)
    # Warning_Line = models.DecimalField(verbose_name='预警线', max_digits=6,decimal_places=4)
    # Stop_Line = models.DecimalField(verbose_name='止损线', max_digits=6,decimal_places=4)
    objects = models.Manager()

    def __str__(self):
        return "(" + self.ID + ")" + self.Name

    class Meta:
        verbose_name = "项目"
        verbose_name_plural = verbose_name


class GuarantorJournal(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "差额补足人"
        verbose_name_plural = verbose_name


class AdviserJournal(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "投资顾问"
        verbose_name_plural = verbose_name


class PosteriorJournal(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    ID = models.CharField(max_length=20, primary_key=True, unique=True, verbose_name='身份识别码')
    Name = models.CharField(max_length=20, verbose_name='名称')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.ID + ")"

    class Meta:
        verbose_name = "劣后级"
        verbose_name_plural = verbose_name


class StockJournal(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    InfoDate = models.DateField(verbose_name='口径日期')
    Code = models.CharField(max_length=10, verbose_name='证券代码')
    Name = models.CharField(max_length=50, verbose_name='证券简称')
    Holdings = models.IntegerField(verbose_name='持股数量（股）')
    Purchase_Price = models.DecimalField(verbose_name='成本价',max_digits=20,decimal_places=2)
    Costs = models.DecimalField(verbose_name='持有成本',max_digits=20,decimal_places=2)
    Cost_to_Nav = models.DecimalField(verbose_name='成本占净值比例(%)',max_digits=20,decimal_places=2)
    Market_Price = models.DecimalField(verbose_name='当日市价',max_digits=20,decimal_places=2)
    Market_Value = models.DecimalField(verbose_name='当日市值',max_digits=20,decimal_places=2)
    Market_Value_to_Nav = models.DecimalField(verbose_name='市值占净值比例(%)',max_digits=20,decimal_places=2)
    Valuation = models.DecimalField(verbose_name='估值增值',max_digits=20,decimal_places=2)
    Status = models.CharField(max_length=10, verbose_name='交易状态')
    objects = models.Manager()

    def __str__(self):
        return self.Name + "(" + self.Code + ")"

    class Meta:
        verbose_name = '底仓详情'
        verbose_name_plural = verbose_name


class NavJournal(models.Model):
    Project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    InfoDate = models.DateField(verbose_name='口径日期')
    NetValue = models.DecimalField(verbose_name='净值', max_digits=6,decimal_places=4)
    objects = models.Manager()

    def __str__(self):
        return self.Project.ID + "(" + str(self.InfoDate) + ")"

    class Meta:
        verbose_name = "净值数据"
        verbose_name_plural = verbose_name

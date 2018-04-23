# Generated by Django 2.0.4 on 2018-04-23 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='身份识别码')),
                ('Name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '投资顾问',
                'verbose_name_plural': '投资顾问',
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('Name', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='经营机构')),
                ('Area', models.CharField(max_length=10, verbose_name='地域')),
            ],
            options={
                'verbose_name': '经营机构',
                'verbose_name_plural': '经营机构',
            },
        ),
        migrations.CreateModel(
            name='Guarantor',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='身份识别码')),
                ('Name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '差额补足人',
                'verbose_name_plural': '差额补足人',
            },
        ),
        migrations.CreateModel(
            name='NavData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InfoDate', models.DateField(verbose_name='口径日期')),
                ('Code', models.CharField(max_length=10, verbose_name='编号')),
                ('Name', models.CharField(max_length=50, verbose_name='名称')),
                ('Holdings', models.IntegerField(verbose_name='持股数量')),
                ('Purchase_Price', models.FloatField(verbose_name='成本价')),
                ('Costs', models.FloatField(verbose_name='成本')),
                ('Cost_to_NAV', models.FloatField(verbose_name='成本占净值比例(%)')),
                ('Market_Price', models.FloatField(verbose_name='收盘价')),
                ('Market_Value', models.FloatField(verbose_name='市值')),
                ('Market_Value_to_NAV', models.FloatField(verbose_name='市值占净值比例(%)')),
                ('Valuation', models.FloatField(verbose_name='估值')),
                ('Status', models.CharField(max_length=10, verbose_name='交易状态')),
            ],
            options={
                'verbose_name': 'A股持仓',
                'verbose_name_plural': 'A股持仓',
            },
        ),
        migrations.CreateModel(
            name='NavFile',
            fields=[
                ('InfoDate', models.DateField(primary_key=True, serialize=False, verbose_name='口径日期')),
                ('Filename', models.CharField(max_length=50, verbose_name='文件名称')),
                ('File', models.FileField(upload_to='Nav_Tables', verbose_name='数据文件')),
                ('FileType', models.CharField(max_length=10, verbose_name='文件类型')),
                ('UploadedDateTime', models.DateTimeField(auto_now=True, verbose_name='上传时间')),
                ('LastModifiedDateTime', models.DateTimeField(verbose_name='上次修改时间')),
                ('ModifiedTimes', models.IntegerField(verbose_name='修改次数')),
                ('Comments', models.TextField(verbose_name='备注')),
            ],
            options={
                'verbose_name': '净值表',
                'verbose_name_plural': '净值表',
            },
        ),
        migrations.CreateModel(
            name='Posterior',
            fields=[
                ('ID', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='身份识别码')),
                ('Name', models.CharField(max_length=20, verbose_name='名称')),
            ],
            options={
                'verbose_name': '劣后级',
                'verbose_name_plural': '劣后级',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('ID', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='编号')),
                ('Name', models.CharField(max_length=50, verbose_name='名称')),
                ('Type', models.CharField(choices=[('Z', '直投类'), ('P', '配资类')], max_length=1, verbose_name='类型')),
                ('Approval_Form_Num', models.CharField(max_length=150, verbose_name='审批单号')),
                ('Issue_Date', models.DateField(verbose_name='发行日期')),
                ('Duration', models.IntegerField(verbose_name='期限')),
                ('Amount', models.IntegerField(verbose_name='金额')),
                ('Leverage_Ratio', models.FloatField(verbose_name='杠杆率')),
                ('Branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Branch', verbose_name='经营机构')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.AddField(
            model_name='posterior',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='navfile',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='navdata',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='guarantor',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Project', verbose_name='项目'),
        ),
        migrations.AddField(
            model_name='adviser',
            name='Project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='S2.Project', verbose_name='项目'),
        ),
    ]

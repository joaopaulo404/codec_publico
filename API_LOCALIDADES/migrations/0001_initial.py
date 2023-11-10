# Generated by Django 4.1.2 on 2022-10-05 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Boletins',
            fields=[
                ('servidor', models.CharField(blank=True, max_length=50, null=True)),
                ('nro_bop', models.CharField(blank=True, max_length=500, null=True)),
                ('nro_bop_aditado', models.CharField(blank=True, max_length=500, null=True)),
                ('nro_tombo', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo_tombo', models.CharField(blank=True, max_length=500, null=True)),
                ('unidade_origem', models.CharField(blank=True, max_length=500, null=True)),
                ('unidade_responsavel', models.CharField(blank=True, max_length=500, null=True)),
                ('data_registro', models.DateField(blank=True, null=True)),
                ('hora_registro', models.TimeField(blank=True, null=True)),
                ('data_fato', models.DateField(blank=True, null=True)),
                ('dia_semana', models.CharField(blank=True, max_length=500, null=True)),
                ('hora_fato', models.TimeField(blank=True, null=True)),
                ('fx_4_hor', models.CharField(blank=True, max_length=500, null=True)),
                ('fx_12_hr', models.CharField(blank=True, max_length=500, null=True)),
                ('data_inst_proc', models.DateField(blank=True, null=True)),
                ('data_concl_proc', models.DateField(blank=True, null=True)),
                ('sit_proc', models.CharField(blank=True, max_length=500, null=True)),
                ('classe_motivo', models.CharField(blank=True, max_length=500, null=True)),
                ('mes_registro', models.CharField(blank=True, max_length=500, null=True)),
                ('mes_fato', models.CharField(blank=True, max_length=500, null=True)),
                ('ano_registro', models.IntegerField(blank=True, null=True)),
                ('ano_fato', models.IntegerField(blank=True, null=True)),
                ('registros', models.CharField(blank=True, max_length=500, null=True)),
                ('consolidado', models.CharField(blank=True, max_length=500, null=True)),
                ('fato_real', models.CharField(blank=True, max_length=500, null=True)),
                ('especificacao_crime', models.CharField(blank=True, max_length=500, null=True)),
                ('meio_emp_deac', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.CharField(blank=True, max_length=500, null=True)),
                ('longitude', models.CharField(blank=True, max_length=500, null=True)),
                ('causa_presumivel', models.CharField(blank=True, max_length=500, null=True)),
                ('especializacao_fato', models.CharField(blank=True, max_length=500, null=True)),
                ('grupo_ocorrencia', models.CharField(blank=True, max_length=500, null=True)),
                ('sub_grupo', models.CharField(blank=True, max_length=500, null=True)),
                ('meio_empregado_sisp', models.CharField(blank=True, max_length=500, null=True)),
                ('distrito', models.CharField(blank=True, max_length=500, null=True)),
                ('municipios', models.CharField(blank=True, max_length=500, null=True)),
                ('regionais', models.CharField(blank=True, max_length=500, null=True)),
                ('bairros', models.CharField(blank=True, max_length=500, null=True)),
                ('reg_integracao', models.CharField(blank=True, max_length=500, null=True)),
                ('risp', models.CharField(blank=True, max_length=500, null=True)),
                ('aisp', models.CharField(blank=True, max_length=500, null=True)),
                ('rua_fato', models.CharField(blank=True, max_length=500, null=True)),
                ('empresa', models.CharField(blank=True, max_length=500, null=True)),
                ('linha', models.CharField(blank=True, max_length=500, null=True)),
                ('tipo_transporte', models.CharField(blank=True, max_length=500, null=True)),
                ('complemento', models.TextField(blank=True, null=True)),
                ('local_ocorrencia', models.TextField(blank=True, null=True)),
                ('identificacao_fato', models.TextField(blank=True, null=True)),
                ('relator', models.TextField(blank=True, null=True)),
                ('relato', models.TextField(blank=True, null=True)),
                ('atuacao', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_nome', models.TextField(blank=True, null=True)),
                ('vit_alcunha', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_dt_nasc', models.DateField(blank=True, null=True)),
                ('vit_idade', models.IntegerField(blank=True, null=True)),
                ('vit_fx_etaria', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_nro_doc', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_tipo_doc', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_pai', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_mae', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_sexo', models.CharField(blank=True, max_length=100, null=True)),
                ('vit_cor_pele', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_grau_inst', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_profissao', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_situacao_emprego', models.CharField(blank=True, max_length=500, null=True)),
                ('vit_estado_civil', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_nome', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_alcunha', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_data_nasc', models.DateField(blank=True, null=True)),
                ('aut_idade', models.IntegerField(blank=True, null=True)),
                ('aut_fx_etaria', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_nro_doc', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_tipo_doc', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_pai', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_mae', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_tipo', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_sexo', models.CharField(blank=True, max_length=500, null=True)),
                ('grau_de_relacionamento', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_cor_pele', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_grau_inst', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_profissao', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_sit_emprego', models.CharField(blank=True, max_length=500, null=True)),
                ('aut_est_civil', models.CharField(blank=True, max_length=500, null=True)),
                ('meio_locomocao', models.CharField(blank=True, max_length=500, null=True)),
                ('cor_veiculo', models.CharField(blank=True, max_length=500, null=True)),
                ('marca_veic_fuga', models.CharField(blank=True, max_length=500, null=True)),
                ('modelo_do_veic_fuga', models.CharField(blank=True, max_length=500, null=True)),
                ('qtd_autor', models.IntegerField(blank=True, null=True)),
                ('relatorio', models.CharField(blank=True, max_length=500, null=True)),
                ('ident_autoria', models.CharField(blank=True, max_length=500, null=True)),
                ('controle', models.CharField(blank=True, max_length=500, null=True)),
                ('controle_ctcd', models.CharField(blank=True, max_length=500, null=True)),
                ('flags', models.CharField(blank=True, max_length=500, null=True)),
                ('id', models.AutoField(db_column='pk', primary_key=True, serialize=False)),
                ('data_upload', models.DateTimeField(blank=True, null=True)),
                ('data_modificacao', models.DateTimeField(blank=True, null=True)),
                ('id_servidor_sicad', models.IntegerField(blank=True, null=True)),
                ('qtd', models.IntegerField(blank=True, null=True)),
                ('data_leitura', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'boletins',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Localidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('risp', models.CharField(blank=True, max_length=500, null=True)),
                ('municipios', models.CharField(blank=True, max_length=500, null=True)),
                ('bairros', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'localidades',
                'managed': False,
            },
        ),
    ]

#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-  
#coding=utf-8
#===============================================================================
#
#         FILE: fdl_cust_occup_info_chain.py
#
#        USAGE: python fdl_cust_occup_info_chain.py 时间参数1（YYYYMMDD） 时间参数2（YYYYMMDD）
#
#  DESCRIPTION: 统计了投资明细数据
#
#      OPTIONS: ---
# REQUIREMENTS: 需要源表bdl.bdl_app_cust_occupation_info获取相关数据。
#               插入ccs信用计划拉链表
#         BUGS: ---
#        NOTES: ---
#       AUTHOR: 袁义军
#      COMPANY: MSXF
#      VERSION: 1.0
#      CREATED: 2016-05-16
#     REVIEWER: 
#     REVISION: ---
#    TGT_TABLE: 
#===============================================================================

import sys
import ConfigParser
from calendar import Calendar

import MySQLdb
import os
import string
import datetime
import time
sys.path.append(os.getenv('BDP_CONN'))
from BdpConnector import *
from Calendar import *
from HiveTasks import *
import traceback
reload(sys)
sys.setdefaultencoding( "utf-8" )

config=ConfigParser.ConfigParser()
config.read("/home/hadoop/edw/etl/conf/etl.ini")

tag_db = 'fdl'
tag_tab = 'fdl_cust_occup_info_chain'
src_db= 'bdl'
src_tab = 'bdl_app_cust_occupation_info'

hts = HiveTasks(tag_db,tag_tab)
dte=Calendar(datetime.datetime.today())

#字符型起始日期
v_statbgdate = sys.argv[1]
#字符型结束日期
v_stateddate = sys.argv[2]
#日期型起始日期
v_start_date = datetime.datetime.strptime(v_statbgdate,'%Y%m%d').date()
#日期型结束日期
v_end_date   = datetime.datetime.strptime(v_stateddate,'%Y%m%d').date()
#当前时间
v_run_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#当前日期
v_run_date = datetime.datetime.now().strftime("%Y%m%d")
#etl抽数日期
v_etl_date  = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#T+1统计日期
v_yest_date = dte.getDayBefore('')
#对时间参数进行处理
if v_statbgdate.strip()=='' and v_stateddate.strip()=='':
    v_statbgdate=v_yest_date
    v_stateddate=v_yest_date
elif v_statbgdate.strip()!='' and v_stateddate.strip()=='':
    v_stateddate=v_statbgdate
elif v_statbgdate.strip()=='' and v_stateddate.strip()!='':
    v_statbgdate=v_stateddate
    
#定义lzo数据索引路径    
lzo_index_path=None
#定义该表数据是否要压缩
lzo_compress = False
#定义是否有分区
is_partition = True
#定义数据文件是否要做合并
merge_flag = False
#合并文件路径
merge_part_dir = None
#定义是否需要做表解析
parse_flag = False

#################Need user configure the parameters####################
v_begin_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
conn=MySQLdb.connect(host=config.get("MYSQL_DB","IP"),port=int(config.get("MYSQL_DB","PORT")),user=config.get("MYSQL_DB","USERNAME"),passwd=config.get("MYSQL_DB","PASSWORD"),db=config.get("MYSQL_DB","DB"))
cur=conn.cursor()

cnt1=0

dir_name='/user/hive/warehouse/fdl.db/'+tag_tab+'/chain_status=active/end_date=47121231/'
cnt1=hts.count_bytes(dir_name)
if cnt1==0:
   os._exit(1)

v_sql = """
      set hive.exec.max.dynamic.partitions=100000;
      set hive.exec.max.dynamic.partitions.pernode=100000;
      set fs.hdfs.impl.disable.cache = true;
      
      use fdl;
      truncate table tmp.tmp_fdl_cust_occup_info_chain;
      insert overwrite table tmp.tmp_fdl_cust_occup_info_chain
      select * from fdl.fdl_cust_occup_info_chain 
      where chain_status='active';
      
from (select 
        id,
        cust_id,
        union_id,
        soc_id,
        edu_degree,
        edu_sys,
        mo_earn,
        mo_earn_oth,
        oth_rpy,
        start_work_dt,
        unit_name,
        entr_tm,
        unit_dept,
        unit_position,
        unit_inds_cat,
        unit_structure,
        unit_prov,
        unit_addr_prov_cd,
        unit_addr_city,
        unit_addr_city_cd,
        unit_street,
        unit_street_cd,
        unit_addr,
        unit_tel_no,
        unit_tel_ext_no,
        create_tm,
        update_tm,
        dt,
        etl_dt,
        start_date,
        end_date,
        chain_status,
        change_code,
        RESERVED_FIELD_V_1,
        RESERVED_FIELD_D_1,
        RESERVED_FIELD_I_1 ,
        RESERVED_FIELD_V_2,
        RESERVED_FIELD_D_2,
        RESERVED_FIELD_I_2
    from tmp.tmp_fdl_cust_occup_info_chain) h
    full outer join
      (select distinct 
            id,
            cust_id,
            unique_id,
            social_identity,
            qualification,
            length_of_schooling,
            month_income,
            other_income,
            other_loan,
            work_start_date,
            unit_name,
            emp_stand_from,
            emp_department,
            emp_post,
            emp_type,
            emp_structure,
            emp_province,
            emp_province_code,
            emp_city,
            emp_city_code,
            emp_zone,
            emp_zone_code,
            emp_addr,
            emp_phone,
            emp_phone_ext_num,
            time_inst,
            time_upd
        from bdl.bdl_app_cust_occupation_info 
        where regexp_replace(substr(time_upd,1,10),'-','') >='"""+ v_statbgdate +"""' 
          and regexp_replace(substr(time_upd,1,10),'-','')<='"""+v_stateddate+"""'
       ) c
      on (h.id = c.id)
      
       insert overwrite table fdl.fdl_cust_occup_info_chain partition (chain_status='expired',end_date,dt)
      select
        h.id,
        h.cust_id,
        h.union_id,
        h.soc_id,
        h.edu_degree,
        h.edu_sys,
        h.mo_earn,
        h.mo_earn_oth,
        h.oth_rpy,
        h.start_work_dt,
        h.unit_name,
        h.entr_tm,
        h.unit_dept,
        h.unit_position,
        h.unit_inds_cat,
        h.unit_structure,
        h.unit_prov,
        h.unit_addr_prov_cd,
        h.unit_addr_city,
        h.unit_addr_city_cd,
        h.unit_street,
        h.unit_street_cd,
        h.unit_addr,
        h.unit_tel_no,
        h.unit_tel_ext_no,
        h.create_tm,
        h.update_tm,    
        '"""+v_etl_date+"""' as etl_dt,
        h.start_date,
        h.change_code,
        h.RESERVED_FIELD_V_1,
        h.RESERVED_FIELD_D_1,
        h.RESERVED_FIELD_I_1,
        h.RESERVED_FIELD_V_2,
        h.RESERVED_FIELD_D_2,
        h.RESERVED_FIELD_I_2,
        '"""+ v_statbgdate +"""' as end_date,
        '19000101' as dt
      where h.id is not null and c.id is not null
      and (
        coalesce(h.id,'-979.090708') <> coalesce(c.id,'-979.090708') or
        coalesce(h.cust_id,'-979.090708') <> coalesce(c.cust_id,'-979.090708') or
        coalesce(h.union_id,'-979.090708') <> coalesce(c.unique_id,'-979.090708') or
        coalesce(h.soc_id,'-979.090708') <> coalesce(c.social_identity,'-979.090708') or
        coalesce(h.edu_degree,'-979.090708') <> coalesce(c.qualification,'-979.090708') or
        coalesce(h.edu_sys,'-979.090708') <> coalesce(c.length_of_schooling,'-979.090708') or
        coalesce(h.mo_earn,'-979.090708') <> coalesce(c.month_income,'-979.090708') or
        coalesce(h.mo_earn_oth,'-979.090708') <> coalesce(c.other_income,'-979.090708') or
        coalesce(h.oth_rpy,'-979.090708') <> coalesce(c.other_loan,'-979.090708') or
        coalesce(h.start_work_dt,'-979.090708') <> coalesce(c.work_start_date,'-979.090708') or
        coalesce(h.unit_name,'-979.090708') <> coalesce(c.unit_name,'-979.090708') or
        coalesce(h.entr_tm,'-979.090708') <> coalesce(c.emp_stand_from,'-979.090708') or
        coalesce(h.unit_dept,'-979.090708') <> coalesce(c.emp_department,'-979.090708') or
        coalesce(h.unit_position,'-979.090708') <> coalesce(c.emp_post,'-979.090708') or
        coalesce(h.unit_inds_cat,'-979.090708') <> coalesce(c.emp_type,'-979.090708') or
        coalesce(h.unit_structure,'-979.090708') <> coalesce(c.emp_structure,'-979.090708') or
        coalesce(h.unit_prov,'-979.090708') <> coalesce(c.emp_province,'-979.090708') or
        coalesce(h.unit_addr_prov_cd,'-979.090708') <> coalesce(c.emp_province_code,'-979.090708') or
        coalesce(h.unit_addr_city,'-979.090708') <> coalesce(c.emp_city,'-979.090708') or
        coalesce(h.unit_addr_city_cd,'-979.090708') <> coalesce(c.emp_city_code,'-979.090708') or
        coalesce(h.unit_street,'-979.090708') <> coalesce(c.emp_zone,'-979.090708') or
        coalesce(h.unit_street_cd,'-979.090708') <> coalesce(c.emp_zone_code,'-979.090708') or
        coalesce(h.unit_addr,'-979.090708') <> coalesce(c.emp_addr,'-979.090708') or
        coalesce(h.unit_tel_no,'-979.090708') <> coalesce(c.emp_phone,'-979.090708') or
        coalesce(h.unit_tel_ext_no,'-979.090708') <> coalesce(c.emp_phone_ext_num,'-979.090708') or
        coalesce(h.create_tm,'-979.090708') <> coalesce(c.time_inst,'-979.090708') or
        coalesce(h.update_tm,'-979.090708') <> coalesce(c.time_upd,'-979.090708')
        )
        
      insert overwrite table fdl.fdl_cust_occup_info_chain partition (chain_status='active',end_date='47121231',dt)
      select
        case when c.id is not null then c.id else h.id end as id,
        case when c.id is not null then c.cust_id else h.cust_id end as cust_id,
        case when c.id is not null then c.unique_id else h.union_id end as union_id,
        case when c.id is not null then c.social_identity else h.soc_id end as soc_id,
        case when c.id is not null then c.qualification else h.edu_degree end as edu_degree,
        case when c.id is not null then c.length_of_schooling else h.edu_sys end as edu_sys,
        case when c.id is not null then c.month_income else h.mo_earn end as mo_earn,
        case when c.id is not null then c.other_income else h.mo_earn_oth end as mo_earn_oth,
        case when c.id is not null then c.other_loan else h.oth_rpy end as oth_rpy,
        case when c.id is not null then c.work_start_date else h.start_work_dt end as start_work_dt,
        case when c.id is not null then c.unit_name else h.unit_name end as unit_name,
        case when c.id is not null then c.emp_stand_from else h.entr_tm end as entr_tm,
        case when c.id is not null then c.emp_department else h.unit_dept end as unit_dept,
        case when c.id is not null then c.emp_post else h.unit_position end as unit_position,
        case when c.id is not null then c.emp_type else h.unit_inds_cat end as unit_inds_cat,
        case when c.id is not null then c.emp_structure else h.unit_structure end as unit_structure,
        case when c.id is not null then c.emp_province else h.unit_prov end as unit_prov,
        case when c.id is not null then c.emp_province_code else h.unit_addr_prov_cd end as unit_addr_prov_cd,
        case when c.id is not null then c.emp_city else h.unit_addr_city end as unit_addr_city,
        case when c.id is not null then c.emp_city_code else h.unit_addr_city_cd end as unit_addr_city_cd,
        case when c.id is not null then c.emp_zone else h.unit_street end as unit_street,
        case when c.id is not null then c.emp_zone_code else h.unit_street_cd end as unit_street_cd,
        case when c.id is not null then c.emp_addr else h.unit_addr end as unit_addr,
        case when c.id is not null then c.emp_phone else h.unit_tel_no end as unit_tel_no,
        case when c.id is not null then c.emp_phone_ext_num else h.unit_tel_ext_no end as unit_tel_ext_no,
        case when c.id is not null then c.time_inst else h.create_tm end as create_tm,
        case when c.id is not null then c.time_upd else h.update_tm end as update_tm,
        '"""+ v_etl_date +"""' as etl_date,        
        if((h.id is null or c.id is not null) and (
            coalesce(h.id,'-979.090708') <> coalesce(c.id,'-979.090708') or
            coalesce(h.cust_id,'-979.090708') <> coalesce(c.cust_id,'-979.090708') or
            coalesce(h.union_id,'-979.090708') <> coalesce(c.unique_id,'-979.090708') or
            coalesce(h.soc_id,'-979.090708') <> coalesce(c.social_identity,'-979.090708') or
            coalesce(h.edu_degree,'-979.090708') <> coalesce(c.qualification,'-979.090708') or
            coalesce(h.edu_sys,'-979.090708') <> coalesce(c.length_of_schooling,'-979.090708') or
            coalesce(h.mo_earn,'-979.090708') <> coalesce(c.month_income,'-979.090708') or
            coalesce(h.mo_earn_oth,'-979.090708') <> coalesce(c.other_income,'-979.090708') or
            coalesce(h.oth_rpy,'-979.090708') <> coalesce(c.other_loan,'-979.090708') or
            coalesce(h.start_work_dt,'-979.090708') <> coalesce(c.work_start_date,'-979.090708') or
            coalesce(h.unit_name,'-979.090708') <> coalesce(c.unit_name,'-979.090708') or
            coalesce(h.entr_tm,'-979.090708') <> coalesce(c.emp_stand_from,'-979.090708') or
            coalesce(h.unit_dept,'-979.090708') <> coalesce(c.emp_department,'-979.090708') or
            coalesce(h.unit_position,'-979.090708') <> coalesce(c.emp_post,'-979.090708') or
            coalesce(h.unit_inds_cat,'-979.090708') <> coalesce(c.emp_type,'-979.090708') or
            coalesce(h.unit_structure,'-979.090708') <> coalesce(c.emp_structure,'-979.090708') or
            coalesce(h.unit_prov,'-979.090708') <> coalesce(c.emp_province,'-979.090708') or
            coalesce(h.unit_addr_prov_cd,'-979.090708') <> coalesce(c.emp_province_code,'-979.090708') or
            coalesce(h.unit_addr_city,'-979.090708') <> coalesce(c.emp_city,'-979.090708') or
            coalesce(h.unit_addr_city_cd,'-979.090708') <> coalesce(c.emp_city_code,'-979.090708') or
            coalesce(h.unit_street,'-979.090708') <> coalesce(c.emp_zone,'-979.090708') or
            coalesce(h.unit_street_cd,'-979.090708') <> coalesce(c.emp_zone_code,'-979.090708') or
            coalesce(h.unit_addr,'-979.090708') <> coalesce(c.emp_addr,'-979.090708') or
            coalesce(h.unit_tel_no,'-979.090708') <> coalesce(c.emp_phone,'-979.090708') or
            coalesce(h.unit_tel_ext_no,'-979.090708') <> coalesce(c.emp_phone_ext_num,'-979.090708') or
            coalesce(h.create_tm,'-979.090708') <> coalesce(c.time_inst,'-979.090708') or
            coalesce(h.update_tm,'-979.090708') <> coalesce(c.time_upd,'-979.090708')
        ),
        '"""+ v_statbgdate +"""',
        h.start_date) as start_date,
        case
            when h.id is null then
                 0
            when h.id is not null and c.id is not null and (
            coalesce(h.id,'-979.090708') <> coalesce(c.id,'-979.090708') or
            coalesce(h.cust_id,'-979.090708') <> coalesce(c.cust_id,'-979.090708') or
            coalesce(h.union_id,'-979.090708') <> coalesce(c.unique_id,'-979.090708') or
            coalesce(h.soc_id,'-979.090708') <> coalesce(c.social_identity,'-979.090708') or
            coalesce(h.edu_degree,'-979.090708') <> coalesce(c.qualification,'-979.090708') or
            coalesce(h.edu_sys,'-979.090708') <> coalesce(c.length_of_schooling,'-979.090708') or
            coalesce(h.mo_earn,'-979.090708') <> coalesce(c.month_income,'-979.090708') or
            coalesce(h.mo_earn_oth,'-979.090708') <> coalesce(c.other_income,'-979.090708') or
            coalesce(h.oth_rpy,'-979.090708') <> coalesce(c.other_loan,'-979.090708') or
            coalesce(h.start_work_dt,'-979.090708') <> coalesce(c.work_start_date,'-979.090708') or
            coalesce(h.unit_name,'-979.090708') <> coalesce(c.unit_name,'-979.090708') or
            coalesce(h.entr_tm,'-979.090708') <> coalesce(c.emp_stand_from,'-979.090708') or
            coalesce(h.unit_dept,'-979.090708') <> coalesce(c.emp_department,'-979.090708') or
            coalesce(h.unit_position,'-979.090708') <> coalesce(c.emp_post,'-979.090708') or
            coalesce(h.unit_inds_cat,'-979.090708') <> coalesce(c.emp_type,'-979.090708') or
            coalesce(h.unit_structure,'-979.090708') <> coalesce(c.emp_structure,'-979.090708') or
            coalesce(h.unit_prov,'-979.090708') <> coalesce(c.emp_province,'-979.090708') or
            coalesce(h.unit_addr_prov_cd,'-979.090708') <> coalesce(c.emp_province_code,'-979.090708') or
            coalesce(h.unit_addr_city,'-979.090708') <> coalesce(c.emp_city,'-979.090708') or
            coalesce(h.unit_addr_city_cd,'-979.090708') <> coalesce(c.emp_city_code,'-979.090708') or
            coalesce(h.unit_street,'-979.090708') <> coalesce(c.emp_zone,'-979.090708') or
            coalesce(h.unit_street_cd,'-979.090708') <> coalesce(c.emp_zone_code,'-979.090708') or
            coalesce(h.unit_addr,'-979.090708') <> coalesce(c.emp_addr,'-979.090708') or
            coalesce(h.unit_tel_no,'-979.090708') <> coalesce(c.emp_phone,'-979.090708') or
            coalesce(h.unit_tel_ext_no,'-979.090708') <> coalesce(c.emp_phone_ext_num,'-979.090708') or
            coalesce(h.create_tm,'-979.090708') <> coalesce(c.time_inst,'-979.090708') or
            coalesce(h.update_tm,'-979.090708') <> coalesce(c.time_upd,'-979.090708')
            )
            then h.change_code+1 
        else
            h.change_code
        end as change_code,
        h.RESERVED_FIELD_V_1,
        h.RESERVED_FIELD_D_1,
        h.RESERVED_FIELD_I_1,
        h.RESERVED_FIELD_V_2,
        h.RESERVED_FIELD_D_2,
        h.RESERVED_FIELD_I_2,
        regexp_replace(substr(case when c.id is not null then c.time_upd else h.update_tm end,1,10),'-','') as dt
      """
res = hts.run_sql_in_hive(v_sql, isLzop = lzo_compress,isPartition=is_partition)   
v_end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  
cnt=0
while v_start_date<= v_end_date:
   file_name='/user/hive/warehouse/fdl.db/'+tag_tab+'/chain_status=active/end_date=47121231/dt='+datetime.datetime.strftime(v_start_date,'%Y%m%d')+'/*'
   try:
      cnt=cnt+hts.count_lines(file_name)
   except (TypeError, ValueError):
      pass
   file_name='/user/hive/warehouse/fdl.db/'+tag_tab+'/chain_status=expired/end_date='+ v_yest_date +'/dt='+datetime.datetime.strftime(v_start_date,'%Y%m%d')+'/*'
   try:
      cnt=cnt+hts.count_lines(file_name)
   except (TypeError, ValueError):
      pass
   v_start_date+= datetime.timedelta(days=1)

if res[0] != 0:
    raise Exception('Please Check SQL...')
    hts.log_info('Please Check SQL...','ERROR')
    logsql="insert into msxf_edw_etljob_status values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(logsql,(v_etl_date,tag_db.lower(),v_begin_time,v_end_time,'failed',src_tab.lower(),cnt,tag_tab.lower(),src_db.lower()))

    os._exit()
else:
    if parse_flag:
         parse_dict = hts.parse_table(tag_db,tag_tab)
    if merge_flag:
         hts.merge_small_file(tag_db, tag_tab, partition = merge_part_dir,  min_size = min_size)
    if lzo_compress and lzo_index_path != None:
        hts.create_index(tag_db, tag_tab, parse_dict, v_statbgdate, path = lzo_index_path)

#    cntsql="select sum(PARAM_VALUE) from hive.PARTITION_PARAMS where PART_ID in (select PART_ID from hive.PARTITIONS WHERE PART_NAME LIKE %s and TBL_ID=(select TBL_ID from hive.TBLS where TBL_NAME=%s)) and PARAM_KEY='numRows'"
 #   domin_str='%dt='+v_statbgdate+'%'
  #  cur.execute(cntsql,(domin_str,tag_tab.lower()))
  #  res_cnt = cur.fetchone()[0]
  #  if res_cnt:
  #      cnt=int(res_cnt)
  #  else:
  #      cnt=0
    logsql="insert into msxf_edw_etljob_status values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(logsql,(v_etl_date,tag_db.lower(),v_begin_time,v_end_time,'success',src_tab.lower(),cnt,tag_tab.lower(),src_db.lower()))

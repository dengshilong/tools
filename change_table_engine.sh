#!/bin/bash

# 将 db_name 下引擎为 MyISAM 的表改为 InnoDB

# 以下变量按需修改
host_name=''
user_name='root'  #  root 或该用户有 root 同等级权限
password=''
db_name=''

tables=$(mysql -h${host_name} -u${user_name} -p${password} -e "SELECT TABLE_NAME FROM information_schema.TABLES WHERE TABLE_SCHEMA='${db_name}' AND ENGINE='MyISAM';")

for table in ${tables}
do
    if [ ${table} != 'TABLE_NAME' ]; then  # 排除标题
        echo ${table}
        mysql -h${host_name} -u${user_name} -p${password} -e "ALTER TABLE ${db_name}.${table} ENGINE='InnoDB';"
    fi
done

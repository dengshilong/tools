#!/bin/bash
# 同步ntp时间
TRY=3
STOP_FAIL_MSG=">>> 停止ntp服务失败，请人工介入"
START_FAIL_MSG=">>> 启动ntp服务失败，请人工介入"

echo ">>>>>>>>>> before update ntp date <<<<<<<<<<"
date

function stop_ntp()
{
    VER=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//|cut -b 1`
    echo ">>> stop ntpd <<< "
    for i in $(seq $TRY)
    do
        if [ "$VER" == "6" ];then
            service ntpd stop
        else
            systemctl stop ntpd
        fi
        if [ $? -eq 0 ];then
            return 0
        fi
    done
    return 1
}

function start_ntp()
{
    VER=`cat /etc/redhat-release | sed s/.*release\ // | sed s/\ .*//|cut -b 1`
    echo ">>> start ntpd <<< "
    for i in $(seq $TRY)
    do
        if [ "$VER" == "6" ];then
            service ntpd start
        else
            systemctl start ntpd
        fi
        if [ $? -eq 0 ];then
            return 0
        fi
    done
    return 1
}

function stop_chronyd()
{
    echo ">>> stop chronyd <<< "
    for i in $(seq $TRY)
    do
        systemctl stop chronyd.service
        if [ $? -eq 0 ];then
            return 0
        fi
    done
    return 1
}

function start_chronyd()
{
    echo ">>> start chronyd <<< "
    for i in $(seq $TRY)
    do
        systemctl start chronyd.service
        if [ $? -eq 0 ];then
            return 0
        fi
    done
    return 1
}

function sync_date()
{
    SERVICE=`ps -ef | grep chronyd | grep -v  grep`
    if [ -z "$SERVICE" ];then
        echo ">>>use ntpd<<<"
        server=`grep server /etc/ntp.conf | grep -v '#' | grep prefer | awk '{print $2}'`
        echo $server
        echo ">>> 停止ntp服务 <<<"
        stop_ntp
        if [ $? -eq 1 ]; then
            echo $STOP_FAIL_MSG
            return 1
        fi
        echo ">>> 更新ntp时间 <<<"
        ntpdate $server
        echo ">>> 启动ntp服务 <<<"
        start_ntp
        if [ $? -eq 1 ]; then
            echo $START_FAIL_MSG
            return 1
        fi
    else
        echo ">>>use chronyd <<<"
        server=`grep server /etc/chrony.conf | grep -v '#' | head -n 1| awk '{print $2}'`
        echo ">>> 停止ntp服务 <<<"
        stop_chronyd
        if [ $? -eq 1 ]; then
            echo $STOP_FAIL_MSG
            return 1
        fi
        echo ">>> 更新ntp时间 <<<"
        echo $server
        ntpdate $server
        echo ">>> 启动ntp服务 <<<"
        start_chronyd
        if [ $? -eq 1 ]; then
            echo $START_FAIL_MSG
            return 1
        fi
    fi
}

echo ">>>updating ntp date <<<"
sync_date
if [ $? -eq 1 ];then
    echo "同步ntp时间失败"
    exit 1
fi
echo ">>>>>>>>>> after update ntp date <<<<<<<<<<"
date

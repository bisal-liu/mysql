#coding=utf-8
#######################################################
# $Name:        mysql_per_monitor_1.py
# $Version:     v1.0
# $Author:      bisal
# $Create Date: 2017-08-26
# $Descriptino: MySQL Performance Mointor
#######################################################

import MySQLdb
import re
import time

def enum(**enums):
    return type('Enum', (), enums)

Status=enum(QPS="queries", Commit="com_commit",
Rollback="com_rollback", Threads_con="Threads_connected",
Threads_run="Threads_running")

# open database connection
dbConn=MySQLdb.connect(
        host='x.x.x.x',
        port=3306,
        user='bisal',
        passwd='xxxxx',
        db='mysql')
cursor=dbConn.cursor()

count=0
while(1==1) :
        # queries
        sql='show global status like \'' + Status.QPS + '\''
        cursor.execute(sql)
        result=cursor.fetchone()
        str= ''.join(result)
        q=str[len(Status.QPS):len(str)]

        # com_commit
        sql='show global status like \'' + Status.Commit + '\''
        cursor.execute(sql)
        result=cursor.fetchone()
        str= ''.join(result)
        c=str[len(Status.Commit):len(str)]

        # com_rollback
        sql='show global status like \'' + Status.Rollback + '\''
        cursor.execute(sql)
        result=cursor.fetchone()
        str= ''.join(result)
        r=str[len(Status.Rollback):len(str)]

        # Threads_con
        sql='show global status like \'' + Status.Threads_con + '\''
        cursor.execute(sql)
        result=cursor.fetchone()
        str= ''.join(result)
        tc=str[len(Status.Threads_con):len(str)]

        # Threads_run
        sql='show global status like \'' + Status.Threads_run + '\''
        cursor.execute(sql)
        result=cursor.fetchone()
        str= ''.join(result)
        tr=str[len(Status.Threads_run):len(str)]
        if (count==0):
                print "|QPS        |Commit     |Rollback   |TPS        |Threads_con  |Threads_run |"
                print "------------------------------------------------------------------------------"
        if (count>=10):
                count=0
                print "------------------------------------------------------------------------------"
                print "|QPS        |Commit     |Rollback   |TPS        |Threads_con  |Threads_run |"
                print "------------------------------------------------------------------------------"
                print "|%-10s |%-10s |%-10s |%-10s |%-12s |%-12s|" % (q,c,r,c+r,tc,tr)
        else:
                print "|%-10s |%-10s |%-10s |%-10s |%-12s |%-12s|" % (q,c,r,c+r,tc,tr)
        count+=1
        time.sleep(1)

# close database connection
cursor.close()
dbConn.close()

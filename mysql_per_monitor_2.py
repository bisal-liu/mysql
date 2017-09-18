#coding=utf-8
#######################################################
# $Name:        mysql_per_monitor.py
# $Version:     v1.0
# $Author:      bisal
# $Create Date: 2017-08-28
# $Descriptino: MySQL Performance Mointor
#######################################################

import MySQLdb
import re
import time

def enum(**enums):
    return type('Enum', (), enums)

Status=enum(QPS="queries", Commit="com_commit", Rollback="com_rollback", \
Threads_con="threads_connected", Threads_run="threads_running")

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
        sql='show global status where variable_name in (\'' + Status.QPS + '\',\'' + Status.Commit \
                        + '\',\'' + Status.Rollback + '\',\'' + Status.Threads_con + '\',\'' + Status.Threads_run + '\')'
        cursor.execute(sql)
        result=cursor.fetchall()
        for line in result:
                #str=''.join(line).lower()
                k1=''.join(line).lower()
                k2=str(line).lower()
                '''print "k1:" + k1
                print "k2:" + k2'''
                if (Status.QPS in k1):
                        q=k1[len(Status.QPS):len(k1)]
                elif (Status.Commit in k1):
                        c=k1[len(Status.Commit):len(k1)]
                elif (Status.Rollback in k1):
                        r=k1[len(Status.Rollback):len(k1)]
                elif (Status.Threads_con in k1):
                        tc=k1[len(Status.Threads_con):len(k1)]
                elif (Status.Threads_run in k1):
                        tr=k1[len(Status.Threads_run):len(k1)]

                '''print k2
                if (Status.QPS in k2):
                        q=k2.split('\'')[3]
                elif (Status.Commit in k2):
                        c=k2.split('\'')[3]
                elif (Status.Rollback in k2):
                        r=k2.split('\'')[3]
                elif (Status.Threads_con in k2):
                        tc=k2.split('\'')[3]
                elif (Status.Threads_run in k2):
                        tr=k2.split('\'')[3]
                '''

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

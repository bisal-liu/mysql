import pymysql
import time

from collections import defaultdict

def enum(**enums):
    return type('Enum', (), enums)

Status=enum(QPS="queries", Commit="com_commit", Rollback="com_rollback", \
            INSERT="com_insert" , DELETE = "com_delete" , UPDATE ="com_update", \
Threads_con="threads_connected", Threads_run="threads_running")

# open database connection
dbConn=pymysql.connect(
        host='${数据库地址}',
        port=3306,
        user='${用户名}',
        passwd='${密码}',
        db='mysql')
        
cursor=dbConn.cursor()
count=0
las = defaultdict(int)
while(1 == 1) :
        sql = 'show global status where variable_name in (\'' + Status.QPS + '\',\'' + Status.Commit +'\',\'' + Status.Rollback \
      + '\',\'' + Status.INSERT + '\',\'' + Status.DELETE + '\',\'' + Status.UPDATE + '\',\'' + Status.Threads_con + '\',\'' + Status.Threads_run + '\')'

        cursor.execute(sql)
        ntime = time.strftime('%Y-%m-%d %H:%M:%S')
        result=cursor.fetchall()
        
        for line in result:
                k1=''.join(line).lower()

                if (Status.QPS in k1):
                        q=int(k1[len(Status.QPS):len(k1)])          
                elif (Status.Commit in k1):
                        c=int(k1[len(Status.Commit):len(k1)])    
                elif (Status.Rollback in k1):
                        r=int(k1[len(Status.Rollback):len(k1)])
                elif (Status.INSERT in k1):
                        i=int(k1[len(Status.INSERT):len(k1)])
                elif (Status.DELETE in k1):
                        d=int(k1[len(Status.DELETE):len(k1)])
                elif (Status.UPDATE in k1):
                        u=int(k1[len(Status.UPDATE):len(k1)])
                elif (Status.Threads_con in k1):
                        tc=int(k1[len(Status.Threads_con):len(k1)])   
                elif (Status.Threads_run in k1):
                        tr=int(k1[len(Status.Threads_run):len(k1)])
                       
        if (count==0):
                print("| QPS  |Commit|Rollback|TPS-Ques|Insert|Delete|Update| TPS   | Threads_con |Threads_run |       now_time     |")
                print("--------------------------------------------------------------------------------------------------------------")
            
        else:
            if (count>=10):
                    count=0
                    print("--------------------------------------------------------------------------------------------------------------")
                    print("| QPS  |Commit|Rollback|TPS-Ques|Insert|Delete|Update| TPS   | Threads_con |Threads_run |       now_time     |")
                    print("--------------------------------------------------------------------------------------------------------------")
                    print("|%-5s |%-5s |%-7s |%-8s|%-6s|%-6s|%-6s|%-7s|%-12s |%-12s|%-20s|" % (abs(q - las['q']),abs(c - las['c']),abs(r - las['r']),abs(c+r - las['c']-las['r']),abs(i-las['i']),abs(d- las['d']),abs(u-las['u']),abs(i+d+u-las['i']-las['d']-las['u']),tc,tr,ntime))
            else:
                    print("|%-5s |%-5s |%-7s |%-8s|%-6s|%-6s|%-6s|%-7s|%-12s |%-12s|%-20s|" % (abs(q - las['q']),abs(c - las['c']),abs(r - las['r']),abs(c+r - las['c']-las['r']),abs(i-las['i']),abs(d- las['d']),abs(u-las['u']),abs(i+d+u-las['i']-las['d']-las['u']),tc,tr,ntime))
        count+=1
        las['r']= r
        las['u']= u
        las['d']= d 
        las['i']= i 
        las['c']= c
        las['q']= q 
        time.sleep(1)

# close database connection
cursor.close()
dbConn.close()

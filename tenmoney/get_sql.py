 #-*-coding:utf-8-*-
import re
import os
import sys

"""
author:shine
function:print all the sqls in tenmoney log
usage:python3 get_sql.py 1000 
    1.IF we do not run it on the server,you can choose your own python version
    2.the number means get the lastest 1000 lines in debug.log)
to do list:
    1.I already find these param_type:['String', 'Long', 'Timestamp', 'Integer', 'BigDecimal', 'Boolean', 'Byte'],if there are other types ,i need add it in the script
    2.to support all the folders of log
    3.how to publish the new version of this script
    4.
"""

def joint_sql(sql,param):
    sql_p_num = sql.count("?")
    param_num = param.count(",")+1
    if sql_p_num!=param_num:
        print ("ERROR:number of params is wrong!:SQL param num is %d ,param num is %d" %(sql_p_num,param_num))
        print (sql)
        print (param)
        return 0
    for p in param.split(", "):
        #if p is null,there is no p_type
        if p.rfind('(')<0:
            p_type = ''
            p_content = p
        else:
            p_type = p[p.rfind('(')+1:p.rfind(')')]
            p_content = p[0:p.rfind('(')]
        if p_type in ('String', 'Timestamp','') :
            sql = sql.replace("?","\'"+p_content+"\'",1)
        else:
            sql = sql.replace("?",p_content,1)
    return sql  
    
def get_sqls(num=0):    
    with open("./debug.log","r",encoding='utf-8') as file_object:
        param_type=[]
        #f_sql = open('./sql_log.txt','w+',encoding='utf-8')
        #if int(num)>len(file_object.readlines()): if we add this ,for line in *** will not run, I don't know why .Maybe it is performace problem.
        #   print ("ERROR : please check your param, it's out of the number of the log  ")
        #print ('I am here!')
        for line in file_object.readlines()[-int(num):]:
            if "Preparing:" in line:
                a = line
            if "Parameters:" in line:
                b = line
                try:
                    a
                except NameError:
                    continue #if the log Parameters appears first,we have to read next line
                else:
                    sql = a[a.find('Preparing:')+len("Preparing: "):]
                    param = b[b.find('Parameters:')+len("Parameters: "):]
                    print (joint_sql(sql,param))
                    for p in param.split(", "):
                        if p.rfind('(')<0:
                            p_type = ''
                            p_content = p
                        else:
                            param_t= p[p.rfind('(')+1:p.rfind(')')]
                            if (param_t not in param_type):
                                param_type.append(param_t)
        #print ("All the para_types are:",param_type)
        #print ("You can find all the sqls in ./sql_log.txt!")
        #f_sql.close()

def get_param_type(param):
    if param.title() == 'True' or param.title() == 'False':
        p_type  = 'Boolean'
    elif param.isdigit():
        p_type = 'Long'
    elif re.match(r'\d{4}(-\d{2}){2}T(\d:){2}.*',param) or re.match(r'\d{4}(-\d{2}){2}',param):
        p_type = 'Timestamp'
    else:
        p_type = 'String'
    return p_type

def get_sqls_task(num=438):
    with open("./tenwit-task.txt","r",encoding='utf-8') as file_object:
        text = ''
        for line in file_object.readlines()[-int(num):]:
            text = text + line
        re_pattern = re.compile(r"(?<=Actual SQL: ds0 :::)[\s\S]*?(?=\])")
        sql_param = re.findall(re_pattern,text)
        for i in range(0,len(sql_param)):
            content = re.sub("\n","",sql_param[i]) #move line feed
            sql = content[0:content.find(":::")]
            param = content[content.find("[")+1:]
            param2 = ''
            for p in param.split(", "):
                param_type = get_param_type(p)
                if param_type == 'Timestamp' and len(param)>10:
                    p = re.sub('T',' ',p[0:19])
                param2 = param2 + p+"("+param_type+"), "
            param2 = param2[:-3]
            #print (joint_sql(sql,param2))

#different log path ,has different sql log print type
def get_log_type():
    dir_now = os.getcwd()#获取当前工作目录路径
    if ("caizhi-job-admin" in dir_now
    or "caizhi-job-executor" in dir_now):
        return "no_sql_log"
    elif ("tenwit-task-provider" in dir_now):
        return "task_log"
    elif ("caizhi-external" in dir_now 
    or "caizhi-manage" in dir_now 
    or "caizhi-market" in dir_now 
    or "caizhi-miniapi" in dir_now 
    or "caizhi-minifile" in dir_now 
    or "caizhi-thirdparty-callback" in dir_now
    or "caizhi-website" in dir_now):
        return "normal_mybatis_log"
    return "normal_mybatis_log"

        
        


if __name__ == "__main__":
    get_sqls_task()
    """
    if len(sys.argv)==1:
        get_sqls()
    else:
        get_sqls(sys.argv[1])
"""

#sql = "INSERT INTO t_corp_poster ( Fid,Fcorp_id,Fname,Furl,Fcode_show,Fposter_diy_type,Fposter_width,Fcode_width,Fcode_long,Fposter_long,Fcode_position_x,Fcode_position_y,Fon_time,Foff_time,Foperator,Frole_id ) VALUES( ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,? )"
#param = "null, ww8c83d949a80b562d(String), 繁星测试无(String), /banner/1097ed8ac4d94bcc8bf2a19eb2809fe4/202008/4cce013b9b124c13ac1a65d4fc34640a.png(String), false(Boolean), 1(String), 375(String), 100(String), 100(String), 375(String), 245(String), 240(String), 2020-08-04 10:51:14.0(Timestamp), 2020-08-05 10:51:15.0(Timestamp), 梁繁兴(String), 2(Integer)"
#joint_sql(sql,param)


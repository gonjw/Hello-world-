import os
import pandas as pd

def suffix(file_list):
    # 返回对应后缀名
    lst =['.doc','.docx','.txt','.pdf','.xls','.xlsx']
    for i in lst:
        if i in file_list:
            j = file_list[-len(i):len(file_list)]
            if i == j:
                return i


def roster(path_roster):
    # 获取Excel列，包括学号、姓名
    Student_name = pd.read_excel(path_roster, usecols=[2],names=None)  # 读取项目名称列,不要列名
    Student_id = pd.read_excel(path_roster, usecols=[1],names=None)  # 读取项目名称列,不要列名

    # 将列转为list，每个元素均为list
    name_list = Student_name.values.tolist()
    id_list = Student_id.values.tolist()
    # 转化为一个列表
    result_name = []
    result_id = []
    for s1 in name_list:
        result_name.append(s1[0])
    for s2 in id_list:
        result_id.append(s2[0])

    return result_name,result_id

def rename_my(path_file,path_roster,num):
    # 获取文件路径
    file_list = os.listdir(path_file)  # 获取文件路径

    # 获取学生名单(学号，姓名)
    student_name,student_id = roster(path_roster)

    # 定义OS路径
    os.chdir(path_file)

    # 重命名
    for name in range (0,len(student_name)):
        for named in range(0,len(file_list)):
            if student_name[name] in file_list[named]:
                # str_rename为重命名之后的名称，file_list[named]为重命名之前的
                str_rename = str(student_id[name])+'-'+student_name[name]+'-'+'第'+num+'次作业'+ suffix(file_list[named])
                os.rename(file_list[named],str_rename)
    # 返回重命名文件个数
    return len(file_list)



if __name__ == '__main__':
    number = input("请输入想要整理第几次作业：")
    # 定义作业文件夹路径``
    path_file = 'D:\python' + number + '次作业'

    # 定义花名册路径
    path_roster = 'D:\python'

    total = rename_my(path_file,path_roster,number)
    print('修改完毕，共修改',total,'个文件')


import os
import pandas as pd

def unfinished(student_complete,student_lst):
    result = []
    # 未选课
    result_abnormal = []
    for i in student_lst:
        if i not in student_complete:
            result.append(i)
    for j in student_complete:
        if j not in student_lst:
            result_abnormal.append(j)
    if(len(result_abnormal) != 0):
        print('未操作系统选讲作业但已交作业的同学为：',result_abnormal)
    return result

def complete(file_lst):
    result = []
    # 文件命名异常
    result_abnormal = []
    # 截取姓名
    for i in range (0,len(file_lst)):
        if (len(file_lst[i]) == 23):
            result.append(file_lst[i][14:17])
        elif(len(file_lst[i]) == 22):
            result.append(file_lst[i][14:16])
        else:
            result_abnormal.append(file_lst[i])
    if (len(result_abnormal) != 0):
        print('操作系统选讲作业文件命名异常的同学为：',result_abnormal)
    return result

def files(file_lst):
    # 去掉文件后缀名
    result = []
    for i in file_lst:
        result.append(i.split('.'))
        return result

        def roster(path_roster):
            # 获取Excel列
            df = pd.read_excel(path_roster, usecols=[2], names=None)  # 读取项目名称列,不要列名
            # 将列转为list，每个元素均为list
            df_lit = df.values.tolist()
            # 转化为一个列表
            result = []
            for s_lit in df_lit:
                result.append(s_lit[0])
            return result

        def Making_list(file_dir, path_roster):
            # 获取文件名
            os.chdir(path_file)
            file_list = os.listdir(file_dir)
            file_lst = files(file_list)

            # 获取已提交学生名单
            student_complete = complete(file_lst)
            # 获取全部学生名单
            student_lst = roster(path_roster)

            # 未提交学生名单
            student_Making = unfinished(student_complete, student_lst)
            return student_Making, len(student_complete)

        if __name__ == '__main__':
            number = input("请输入想要查验第几次作业：")
            # 定义作业文件夹路径
            path_file = 'D:\Desktop\操作系统选讲作业\操作系统选讲第' + number + '次作业'
            # 定义花名册路径
            path_roster = 'D:\Desktop\操作系统选讲作业\花名册.xlsx'

            # 交齐则输出交齐，未交齐输出未交名单
            lst, num = Making_list(path_file, path_roster)
            if (len(lst) == 0):
                print('本次作业已交齐')
            else:
                print('操作系统选讲选课人数：54', '；作业已提交人数：', num, '；未提交人数：', (62 - num))
                print('操作系统选讲作业缺交名单为：', '\n', lst)



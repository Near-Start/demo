# _*_ coding: utf-8 _*_

import json
from datetime import datetime

from django.contrib import messages
from django.shortcuts import render, reverse, redirect

from toolkit.initialization import neo_con
from .models import *

test_id = []
answers = []


def register(request):
    if request.method == 'POST':
        user_id = request.POST.get("uid", '')
        pass_word = request.POST.get("pwd", '')
        # f = user_id[0]
        if user_id and pass_word:
            u1 = Student.objects.filter(id=user_id).count()
            u2 = Teacher.objects.filter(id=user_id).count()
            if u1 or u2:
                messages.error(request, '该用户名已注册')
                return render(request, 'register.html', {'uid': user_id})
            else:
                # 注册
                user = Student(id=user_id, password=pass_word)
                user.save()
                messages.error(request, '注册成功')
                return render(request, 'register.html', {'uid': user_id})
        else:
            messages.error(request, '请填写用户名和密码')
            return render(request, 'register.html', {'uid': user_id})
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user_id = request.POST.get("uid", '')
        pass_word = request.POST.get("pwd", '')
        if user_id and pass_word:
            u1 = Student.objects.filter(id=user_id).count()
            u2 = Teacher.objects.filter(id=user_id).count()
            if u1 or u2:  # 检测用户名是否存在
                f1 = Student.objects.filter(id=user_id, password=pass_word).count()
                f2 = Teacher.objects.filter(id=user_id, password=pass_word).count()
                if f1 or f2:  # 检查密码是否正确
                    request.session['uid'] = user_id
                    return redirect(reverse('home'))
                else:
                    messages.error(request, '用户名或者密码错误')
                    return render(request, 'login.html', {'uid': user_id})
            else:
                messages.error(request, '用户名不存在')
                return render(request, 'login.html', {'uid': user_id})
        else:
            messages.error(request, '请输入用户名和密码')
            return render(request, 'login.html', {'uid': user_id})
    else:
        return render(request, 'login.html')


def home(request):
    user_id = request.session['uid']

    db = neo_con
    searchResult = db.match_all_node()
    return render(request, 'home.html', {'uid': user_id, 'searchResult': json.dumps(searchResult, ensure_ascii=False)})


def node_search(request):
    searchResult = {}
    user_id = request.session['uid']

    if request.method == 'POST':
        data = request.POST
        entity1 = data.get("entity1", '')
        entity2 = data.get("entity2", '')
        relation = data.get("relation", '')
        db = neo_con
        # 若只输入entity1
        if len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0:
            searchResult = db.findRelationByEntity1(entity1)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 若只输入entity2
        if len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0:
            searchResult = db.findRelationByEntity2(entity2)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 若只输入关系
        if len(relation) != 0 and len(entity2) == 0 and len(entity1) == 0:
            searchResult = db.findEntityByRelation(relation)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 若输入entity1和relation
        if len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0:
            searchResult = db.findRelationByEntiti1andRelation(entity1, relation)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 若输入entity2和relation
        if len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0:
            searchResult = db.findRelationByEntiti2andRelation(entity2, relation)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'enti0ty2': entity2, 'relation': relation})

        # 若输入entity1和entity2
        if len(entity1) != 0 and len(relation) == 0 and len(entity2) != 0:
            searchResult = db.findRelationByEntiti1andEntiti2(entity1, entity2)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

        # 若输入entity1,entity2和relation
        if len(entity1) != 0 and len(entity2) != 0 and len(relation) != 0:
            searchResult = db.findEntityRelation(entity1, relation, entity2)
            if searchResult:
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation,
                               'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                messages.error(request, '抱歉未能找到知识点，请重新输入')
                return render(request, 'node_search.html',
                              {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})
        # 全为空
        if len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0:
            messages.error(request, '请输入您所需要查询的知识点，请勿输入空值')
            return render(request, 'node_search.html',
                          {'uid': user_id, 'entity1': entity1, 'entity2': entity2, 'relation': relation})

    return render(request, 'node_search.html', {'uid': user_id})


# 学生自测 视图函数
def answer(request):
    subject = ''
    user_id = request.session['uid']
    if request.method == 'POST':

        global test_id
        global answers
        test_id = [0 for x in range(10)]
        answers = ['0' for x in range(10)]
        subject = request.POST.get('km')
        # 随机获取题目
        questions = Question.objects.filter(subject=subject).order_by('?')
        i = 0
        for test in questions:
            test_id[i] = test.id
            answers[i] = str(test.answer)
            i += 1
            if i == 10:
                break

        return render(request, 'answer.html', {'uid': user_id, 'subject': subject, 'questions': questions})

    return render(request, 'answer.html', {'uid': user_id, 'subject': subject})


# 计算由answer.html模版传过来的数据计算成绩
def calGrade(request):
    user_id = request.session['uid']
    subject = request.POST.get('subject', '')
    global test_id
    if request.method == 'POST':
        examtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # examtime = request.POST.get('examtime','')
        i = 0
        count = 0
        mygrade = 0  # 初始化一个成绩为0
        for p in test_id:
            count += 1
            data = request.POST
            if i < len(request.POST) - 2:
                myans = data.get(str(p))
                okans = answers[i]  # 得到正确答案
                i += 1
                if myans == okans:  # 判断学生作答与正确答案是否一致
                    mygrade += 10  # 若一致,得到该题的分数,累加mygrade变量
            if count == 10:
                Grade.objects.create(sid_id=user_id, subject=subject, grade=mygrade, time=examtime)
        messages.error(request, '您的得分为：' + str(mygrade) + ',可以在“成绩查询”处查看更多')
        return redirect(reverse('answer'))


def showGrade(request):
    user_id = request.session['uid']
    if request.method == 'POST':
        subject = request.POST.get('km', '')
        grade = Grade.objects.filter(subject=subject)

        data1 = Grade.objects.filter(subject=subject, grade__lt=60).count()
        t1 = Grade.objects.filter(subject=subject, grade__lt=60).values('time')
        data2 = Grade.objects.filter(subject=subject, grade__gte=60, grade__lt=70).count()
        t2 = Grade.objects.filter(subject=subject, grade__gte=60, grade__lt=70).values('time')
        data3 = Grade.objects.filter(subject=subject, grade__gte=70, grade__lt=80).count()
        t3 = Grade.objects.filter(subject=subject, grade__gte=70, grade__lt=80).values('time')
        data4 = Grade.objects.filter(subject=subject, grade__gte=80, grade__lt=90).count()
        t4 = Grade.objects.filter(subject=subject, grade__gte=80, grade__lt=90).values('time')
        data5 = Grade.objects.filter(subject=subject, grade__gte=90).count()
        t5 = Grade.objects.filter(subject=subject, grade__gte=90).values('time')

        data = {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5}
        time = {'time1': t1, 'time2': t2, 'time3': t3, 'time4': t4, 'time5': t5, }
        return render(request, 'showGrade.html',
                      {'uid': user_id, 'grade': grade, 'data': data, 'time': time, 'subject': subject})
    return render(request, 'showGrade.html', {'uid': user_id})


def logout(request):
    request.session.flush()
    return redirect(reverse(login))

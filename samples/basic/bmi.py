#!/usr/bin/env python3
# -*- coding: utf-8 -*-


height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（KG）："))  # 小明体重,单位:公斤

# BMI = 体重(kg) / 身高^2(m)
bmi = weight / height ** 2

lowerBmi= 18.5
highBmi = 25

lowerWeight = lowerBmi * (height ** 2)
highWeight = highBmi * (height ** 2)

print(f'小明的BMI指数是:{bmi:.2f}')


if bmi < 18.5:
    print('BMI指数过轻')
elif 18.5 <= bmi < 25:
    print('BMI指数正常')
elif 25 <= bmi < 28:
    print('BMI指数过重')
elif 28 <= bmi < 32:
    print('BMI指数肥胖')
else:
    print('BMI指数严重肥胖')

print(f"根据您的身高：{height:.2f} 您体重的正常范围是： [{lowerWeight:.0f}kg,{highWeight:.0f}kg]" )
#!/usr/bin/env python3# -*- coding: utf-8 -*-# Create by shengjk1 on  2018/5/14# name = input("name")# print ((name)## num = int(input("age"))# print ((num)## result = eval(input("enter a expression:"))# print ((result)## while True:#     try:#         x = int(input("age:"))#         break#     except BaseException as e:#         print (("that is not a valid number!" ,e)#     finally:#         print (("Attmpted Input")path = '/Users/iss/sourceCode/pyProject/pythonDemo/clsself.py'# python3 'ascii' codec can't decode byte 0xe6 in position 0f = open(path, 'r', encoding='latin1')f.read()f.close()f = open("./test.txt", 'w')f.write("hahahhh")f.close()# with 自动关闭流with open(path, 'r') as f:    print (f.read(4))    # print ((bytes.decode(f.read().encode("utf-8")))camelot_lines = []with open(path) as f:    for line in f:        camelot_lines.append(line.strip())print (camelot_lines)import unicodecsvdef read_csv(filename):    with open(filename, 'rb') as f:        reader = unicodecsv.DictReader(f)        return list(reader)daily_engagement = read_csv('/Users/iss/Desktop/test.csv')print (daily_engagement[0])print (type(daily_engagement[0]))import pandas as pddaily_engagement = pd.read_csv("/Users/iss/Desktop/test.csv")print (daily_engagement["acct"].unique())import numpy as np# First 20 countries with employment datacountries = np.array([    'Afghanistan', 'Albania', 'Algeria', 'Angola', 'Argentina',    'Armenia', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas',    'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',    'Belize', 'Benin', 'Bhutan', 'Bolivia',    'Bosnia and Herzegovina'])# Employment data in 2007 for those 20 countriesemployment = np.array([    55.70000076, 51.40000153, 50.5, 75.69999695,    58.40000153, 40.09999847, 61.5, 57.09999847,    60.90000153, 66.59999847, 60.40000153, 68.09999847,    66.90000153, 53.40000153, 48.59999847, 56.79999924,    71.59999847, 58.40000153, 70.40000153, 41.20000076])# Change False to True for each block of code to see what it does# Accessing elementsif True:    print (countries[0])    print (countries[3])# Slicingif True:    print (countries[0:3])    print (countries[:3])    print (countries[17:])    print (countries[:])# Element typesif True:    print (countries.dtype)    print (employment.dtype)    print (np.array([0, 1, 2, 3]).dtype)    print (np.array([1.0, 1.5, 2.0, 2.5]).dtype)    print (np.array([True, False, True]).dtype)    print (np.array(['AL', 'AK', 'AZ', 'AR', 'CA']).dtype)# Loopingif True:    for country in countries:        print ('Examining country {}'.format(country))    for i in range(len(countries)):        country = countries[i]        country_employment = employment[i]        print ('Country {} has employment {}'.format(country,                                                     country_employment))# Numpy functionsif True:    print (employment.mean())    print (employment.std())    print (employment.max())    print (employment.sum())max_value = employment.max()print('======', employment.argmax())def max_employment(countries, employment):    '''    Fill in this function to return the name of the country    with the highest employment in the given employment    data, and the employment in that country.    '''    max_country = None      # Replace this with your code    max_value = None   # Replace this with your code    return (max_country, max_value)import numpy as np# Change False to True for each block of code to see what it does# Arithmetic operations between 2 NumPy arraysif True:    a = np.array([1, 2, 3, 4])    b = np.array([1, 2, 1, 2])    print (a + b)    print (a - b)    print (a * b)    print (a / b)    print (a ** b)# Arithmetic operations b )etween a NumPy array and a single numberif True:    a = np.array([1, 2, 3, 4])    b = 2    print()    print (a + b)    print (a - b)    print (a * b)    print (a / b)    print (a ** b)# Logical operations with NumPy arraysif True:    a = np.array([True, True, False, False])    b = np.array([True, False, True, False])    # 如果是数字的话，按位与按位或    print()    print (a & b)    print (a | b)    print (~a)    print (a & True)    print (a & False)    print (b | True)    print (b | False)# Comparison operations between 2 NumPy Arraysif True:    a = np.array(['a', 'v', 'ac', 'df', 'ff'])    b = np.array(['a', 'v', 'ac', 'df', 'ff'])    # b = np.array([5, 4, 3, 2, 1])    print()    print (a > b)    print (a >= b)    print (a < b)    print (a <= b)    print (a == b)    print (a != b)# Comparison operations between a NumPy array and a single numberif True:    a = np.array([1, 2, 3, 4])    b = 2    print (a > b)    print (a >= b)    print (a < b)    print (a <= b)    print (a == b)    print (a != b)# First 20 countries with school completion datacountries = np.array([    'Algeria', 'Argentina', 'Armenia', 'Aruba', 'Austria', 'Azerbaijan',    'Bahamas', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Bolivia',    'Botswana', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burundi',    'Cambodia', 'Cameroon', 'Cape Verde'])# Female school completion rate in 2007 for those 20 countriesfemale_completion = np.array([    97.35583, 104.62379, 103.02998, 95.14321, 103.69019,    98.49185, 100.88828, 95.43974, 92.11484, 91.54804,    95.98029, 98.22902, 96.12179, 119.28105, 97.84627,    29.07386, 38.41644, 90.70509, 51.7478, 95.45072])# Male school completion rate in 2007 for those 20 countriesmale_completion = np.array([    95.47622, 100.66476, 99.7926, 91.48936, 103.22096,    97.80458, 103.81398, 88.11736, 93.55611, 87.76347,    102.45714, 98.73953, 92.22388, 115.3892, 98.70502,    37.00692, 45.39401, 91.22084, 62.42028, 90.66958])def overall_completion_rate(female_completion, male_completion):    '''    Fill in this function to return a NumPy array containing the overall    school completion rate for each country. The arguments are NumPy    arrays giving the female and male completion of each country in    the same order.    '''    return (male_completion+female_completion)/2'''+与+=不一样的+=原位运算   +不是原位运算'''# np跟python原生数组是不一样的，np更像是一种向量# [100   2   3   4   5   6]a = np.array([1, 2, 3, 4, 5, 6])slice = a[:3]slice[0] = 100print(a)# [1, 2, 3, 4, 5, 6]a = [1, 2, 3, 4, 5, 6]slice = a[:3]slice[0] = 100print(a)# python中booleam类型可以进行相加True + True == 2  # True# Pandas的Series与numpy 中的array类似
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

import func

plt.style.use('seaborn')

d_df = pd.read_csv('HD.csv')

# Total Cholesterol, Body Mass Index, Systolic BP,
# Diastolic BP, Glucose, Heart Rate, Number of Cigarettes Smoked

list1 = ['totChol', 'BMI', 'sysBP', 'diaBP', 'glucose', 'heartRate', 'cigsPerDay']
at = d_df[d_df['TenYearCHD'] == 1]
nat = d_df[d_df['TenYearCHD'] == 0]
#
# for v in list1:
#     func.hist_ser(nat[v].dropna(), at[v].dropna(), f'{v} at/not at CHD risk', 'not affected', 'affected')


def percent(d_df, c, t1, t2):
    at = d_df[d_df['TenYearCHD'] == 1]
    nat = d_df[d_df['TenYearCHD'] == 0]
    mat = at[at[c] == 1]
    mnat = nat[nat[c] == 1]

    fat = at[at[c] == 0]
    fnat = nat[nat[c] == 0]

    print(t1)
    print(f'At Risk: {round(len(mat) / (len(mat) + len(mnat)) * 100)}%')
    print(f'Not at Risk: {round(len(mnat) / (len(mat) + len(mnat)) * 100)}%')
    print(t2)
    print(f'At Risk: {round(len(fat) / (len(fat) + len(fnat)) * 100)}%')
    print(f'Not at Risk: {round(len(fnat) / (len(fat) + len(fnat)) * 100)}%')


percent(d_df, 'male', 'Male', 'Female')


def percent_age(d_df, c, age):
    at = d_df[d_df['TenYearCHD'] == 1]
    nat = d_df[d_df['TenYearCHD'] == 0]

    be_at = at[at[c] <= age]
    ov_at = at[at[c] > age]
    be_nat = nat[nat[c] <= age]
    ov_nat = nat[nat[c] > age]
    print(f'Below {age}')
    print(f'At Risk: {round(len(be_at) / (len(be_at) + len(be_nat)) * 100)}%')
    print(f'Not at Risk: {round(len(be_nat) / (len(be_at) + len(be_nat)) * 100)}%')
    print(f'Above {age}')
    print(f'At Risk: {round(len(ov_at) / (len(ov_at) + len(ov_nat)) * 100)}%')
    print(f'Not at Risk: {round(len(ov_nat) / (len(ov_at) + len(ov_nat)) * 100)}%')


print()
percent_age(d_df, 'age', 45)


def gaussian_hist(d_df):
    x = d_df[d_df['male'] == 1]
    y = d_df[d_df['male'] == 0]
    xw = x['BMI']
    yw = y['BMI']

    plt.subplot(121)
    xw.plot.density()
    plt.axvline(xw.mean())
    plt.title('Male BMI')
    # plt.show()
    plt.subplot(122)
    xw.plot.hist()
    plt.title('Male BMI')
    plt.show()

    plt.subplot(121)
    yw.plot.density()
    plt.title('Female BMI')
    plt.subplot(122)
    yw.plot.hist()
    plt.title('Female BMI')
    plt.show()

    print(f'Male\nMean: {xw.mean()}\nSTD: {xw.std()}\nFemale\nMean: {yw.mean()}\nSTD: {yw.std()}')

# gaussian_hist(d_df)


def gaussian(d_df, cn):
    x = d_df[d_df['male'] == 1]
    y = d_df[d_df['male'] == 0]
    xw = x[cn]
    yw = y[cn]

    xw.plot.density()
    plt.axvline(xw.mean(), color='r', linestyle='--')
    plt.axvline(xw.mean() + xw.std(), color='g', linestyle='--')
    plt.axvline(xw.mean() - xw.std(), color='g', linestyle='--')
    plt.title(f'Male {cn}')
    plt.show()

    yw.plot.density()
    plt.title(f'Female {cn}')
    plt.axvline(yw.mean(), color='r', linestyle='--')
    plt.axvline(yw.mean() + yw.std(), color='g', linestyle='--')
    plt.axvline(yw.mean() - yw.std(), color='g', linestyle='--')
    plt.show()

    k = (abs(yw.mean() - xw.mean())) / math.sqrt(.5 * ((yw.std() ** 2) * (xw.std() ** 2)))

    print(f'Male\nMean: {xw.mean()}\nSTD: {xw.std()}\nFemale\nMean: {yw.mean()}\nSTD: {yw.std()}')
    print()
    print(f'K: {k}')


gaussian(d_df, 'BMI')
gaussian(d_df, 'glucose')






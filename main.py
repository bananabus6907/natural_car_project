import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')  # 폰트 설정
plt.rc('axes', unicode_minus=False)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

electric1 = pd.read_csv("data//연료종류별 자동차 등록현황.csv")
electric2 = pd.read_csv("data//한국가스안전공사_수소충전소 현황_20210914.csv", encoding='CP949')
electric3 = pd.read_csv("data//한국전력공사_지역별 전기차 충전기 현황정보_20201008.csv", encoding='CP949')
electric4 = pd.read_csv("data//한국전력공사_지역별 전기차 현황정보_20201008.csv", encoding='CP949')
electric5 = pd.read_csv("data//한국환경공단_전기차 충전기 현황_환경부 공공급속충전기_20200629.csv", encoding='CP949')
electric6 = pd.read_csv("data//환경부_전기자동차 급속충전기 보급 현황_20210630.csv", encoding='CP949')

print(electric1)

Hydrogen_car = pd.DataFrame()
Hydrogen_car["수소충전소"] = electric2["번호"]
Hydrogen_car["수소연료전지자동차"] = electric1["수소"]
Hydrogen_car_sum = Hydrogen_car["수소연료전지자동차"].sum()
Hydrogen_car_num = Hydrogen_car["수소충전소"].max()

print(f"수소차 충전소 당 수소차 : {Hydrogen_car_sum/Hydrogen_car_num}")
Hydrogen_car_table = pd.DataFrame({'대수': [Hydrogen_car_sum], '충전소': [Hydrogen_car_num], "수소차 충전소 당 수소차 ": [Hydrogen_car_num/Hydrogen_car_sum *100]})
print(Hydrogen_car_table)


plt.title("수소차 수와 수소차 충전소")
plt.plot(Hydrogen_car)
plt.ylabel("대수")
plt.show()
print("="*70)

electric_car = pd.DataFrame()
electric_car["년도"] = electric6["년도"]
electric_car["급속충전기"] = electric6["급속충전기 보급 수량"]
ex = electric3[electric3.지역=="총합"]
print(ex)
ex=ex.drop("지역",axis=1)
ex = ex.transpose()
ex.rename(columns={'17':'총합'}, inplace=True)

print(electric_car)


fig, ax = plt.subplots()

electric1.plot(kind='line', x='자동차 년도', y='전기차&수소차', ax=ax)
electric1.plot(kind='line', x='자동차 년도', y='전기', ax=ax)
electric1.plot(kind='line', x='자동차 년도', y='수소', ax=ax)

for i in range(len(electric3)):
    for j in range(1, len(electric3.iloc[1])):
        electric3.iloc[i][-1] += electric3.iloc[i][j]

print(type(electric3.iloc[3][3]))

er = electric1.values.tolist()
print(er[-1])
su = er[-1][1]
elec  =  er[-1][2]/su *100
suso = er[-1][3]/su *100
print (elec , suso )
ratio = [elec, suso]
labels = ['전기차', '수소차']
explode = [0, 0.1]
colors = ['#ff9999', '#ffc000']
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 1}
plt.pie(ratio,labels= labels, autopct ='%.1f%%',startangle=260,
counterclock=False, explode=explode, shadow =True,colors=colors, wedgeprops=wedgeprops)
plt.show()

elec_car = electric4.values.tolist()
print(electric4)
print(elec_car)
#######################################################################################################################
# pie
local = ['강원도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', '울산광역시', '인천광역시', '전라남도', '전라북도', '제주특별자치도', '충청남도', '충청북도']
explode = [0, 0.1, 0,0.1,0,0.1,0,0.1,0,0.1,0,0.1,0,0.1,0,0.1,0]
wedgeprops={'width': 0.7, 'edgecolor': 'w', 'linewidth': 1}
colors = []
for _ in range(17):
    colors.append("#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
print(colors)
elec_car_2018 = elec_car[0][1:-1]
elec_car_2019 = elec_car[1][1:-1]
elec_car_2020 = elec_car[2][1:-1]
elec_car_2018_ratio = []
elec_car_2019_ratio = []
elec_car_2020_ratio = []
for i in elec_car_2018:
    elec_car_2018_ratio.append(i/elec_car[0][-1] *100 )
for i in elec_car_2019:
    elec_car_2019_ratio.append(i/elec_car[1][-1] *100 )
for i in elec_car_2020:
    elec_car_2020_ratio.append(i/elec_car[2][-1] *100 )

plt.figure(figsize=(10,10))
plt.title("2018 전국 전기차 비율")
plt.pie(elec_car_2018_ratio,labels= local, autopct ='%.1f%%',startangle=260,
counterclock=False, explode=explode, shadow =True, wedgeprops=wedgeprops)
plt.show()
print("="*70)
plt.figure(figsize=(10,10))
plt.title("2019 전국 전기차 비율")
plt.pie(elec_car_2019_ratio,labels= local, autopct ='%.1f%%',startangle=260,
counterclock=False, explode=explode, shadow =True, wedgeprops=wedgeprops)
plt.show()
print("="*70)
plt.figure(figsize=(10,10))
plt.title("2020 전국 전기차 비율")
plt.pie(elec_car_2020_ratio,labels= local, autopct ='%.1f%%',startangle=260,
counterclock=False, explode=explode, shadow =True, wedgeprops=wedgeprops)
plt.show()
print("="*70)

####################################################################################################################################
plt.figure(figsize=(25,10))
plt.title("2018 전국 전기차")
plt.bar(np.arange(len(local)), elec_car_2018, align='edge', edgecolor='lightgray', linewidth=5 ,color = colors )
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2019 전국 전기차")
plt.bar(np.arange(len(local)), elec_car_2019 , align='edge', edgecolor='lightgray',linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2020 전국 전기차")
plt.bar(np.arange(len(local)), elec_car_2020,align='edge', edgecolor='lightgray', linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

elec_char = electric3.values.tolist()
local = ['강원도', '경기도', '경상남도', '경상북도', '광주광역시', '대구광역시', '대전광역시', '부산광역시', '서울특별시', '세종특별자치시', '울산광역시', '인천광역시', '전라남도', '전라북도', '제주특별자치도', '충청남도', '충청북도']


elec_char_2016=[]
elec_char_2017=[]
elec_char_2018=[]
elec_char_2019=[]
elec_char_2020=[]

for i in elec_char[:-1]:
    elec_char_2016.append(i[1])
    elec_char_2017.append(i[2])
    elec_char_2018.append(i[3])
    elec_char_2019.append(i[4])
    elec_char_2020.append(i[5])

print(len(elec_char_2016))
plt.figure(figsize=(25,10))
plt.title("2016 전국 전기차 충전소")
plt.bar(np.arange(len(local)), elec_char_2016, align='edge', edgecolor='lightgray', linewidth=5 ,color = colors )
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2017 전국 전기차 충전소")
plt.bar(np.arange(len(local)), elec_char_2017 , align='edge', edgecolor='lightgray',linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2018 전국 전기차 충전소")
plt.bar(np.arange(len(local)), elec_char_2018,align='edge', edgecolor='lightgray', linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2019 전국 전기차 충전소")
plt.bar(np.arange(len(local)), elec_char_2019,align='edge', edgecolor='lightgray', linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

plt.figure(figsize=(25,10))
plt.title("2020 전국 전기차 충전소")
plt.bar(np.arange(len(local)), elec_char_2020,align='edge', edgecolor='lightgray', linewidth=5,color = colors)
plt.xticks(np.arange(len(local)), local)
plt.show()
print("="*70)

loca = []
for i in elec_char:
    loca.append(i[0])

print(loca)
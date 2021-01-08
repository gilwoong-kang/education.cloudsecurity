import csv,re,os


with open('./apt_data.csv','r',encoding='CP949') as file:
    apt_data = csv.reader(file)

    result = []

    for apt in apt_data:
        if apt[0] == '시군구' :
            continue
        
        if re.search('인천광역시',apt[0]):
            if float(apt[5]) >= 120.0 and int(re.sub(',','',apt[8])) <= 50000: 
                result.append(apt[4])

    for r in result:
        print('{},'.format(r))
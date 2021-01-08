import re

with open('./csv_assignment/input.txt','r') as file:
    with open('./csv_assignment/output.csv','w') as output:
        for data in file:
            list = re.findall('[가-힣0-9]+',data)
            for i in range(len(list)):
                if i != len(list)-1 :
                    output.write('{},'.format(list[i]))
                else :
                    output.write('{}'.format(list[i]))
            output.write('\n')
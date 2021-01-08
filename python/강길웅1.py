import numpy as np
import re

result = []
month = [0,0,0,0,0,0,0,0,0,0,0,0]

with open('./output.txt','w') as output:
    with open('./input.txt','r') as file:
        data = file.readline()
        for data in file:
            output.write('{}'.format(data.strip()))
            if data.startswith('#'):
                output.write('\n')
                continue
            data = data.split('\t')
            for d in range(1,len(data)):
                split = re.findall('[^,]',data[d])
                word = ''
                for j in split:
                    word += j
                value = int(word.strip())
                data[d] = value
                month[d-1] += value
            list = np.array(data[1:])
            avg = np.mean(list)
            sum = np.sum(list)
            output.write('\t{}\t{}\n'.format(sum,round(avg,2)))
            result.append([avg,sum])

        # 월별 총합값
        month.append(np.sum(month))
        month.append(round(month[12]/12,2))
        output.write('sum\t\t ')
        for i in range(len(month)):
            output.write('{}\t'.format(month[i]))
        output.write('\navg\t ')
        for i in range(len(month)-1):
            output.write('{}\t'.format(round(month[i]/11,2)))
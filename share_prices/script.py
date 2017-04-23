from random import randint


# Companies
company1 = 'IDFC'
company2 = 'CEAT'
company3 = 'GAIL'
company4 = 'Flipkart'
company5 = 'IndiGo'
company6 = 'Infosys'
company7 = 'Snapdeal'
company8 = 'Wipro'
company9 = 'MphasiS'
company10 = 'BankBazaar'

f = open('share_prices.csv', 'w+')
f.write('Year,Month,'+company1+','+company2+','+company3+','+company4+','+company5+','+company6+','+company7+','+company8+','+company9+','+company10+'\n')

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
i = 1990

while i<=2017:
    for index, month in enumerate(months):
        if i == 2017 and index == 3:
            break
        f.write(str(i) + ',' + month + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + ',' + str(randint(1, 999)) + '\n')
    i += 1
f.close()

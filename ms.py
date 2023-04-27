import webbrowser as wb




#9702/11/O/N/22
#Subject code/ Varient/ month/ year

while True:
    search = input()

    sub_code = search[0:4]

    varient = search[5:7]

    month = search[8]

    year = search[12:]

    subdict = {
        '9702' : 'Physics',
        '9701' : 'Chemistry',
        '9709' : 'Mathematics',
        '9618' : 'Computer Science (for first examination in 2021) '
        }
    subname = subdict[sub_code]
    vari = {
        'F' : 'm',
        'M' : 's',
        'O' : 'w'
    }
    v = vari[month]

    #https://papers.gceguide.com/A%20Levels/Physics%20(9702)/2022/9702_s22_ms_11.pdf
    #f'https://papers.gceguide.com/A%20Levels/{subjectname}%20({sub_code})/20{year}/{sub_code}_{v}{year}_ms_{varient}.pdf'
    a = (f'https://papers.gceguide.com/A%20Levels/{subname}%20({sub_code})/20{year}/{sub_code}_{v}{year}_ms_{varient}.pdf')
    wb.open(a)
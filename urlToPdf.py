import os
import time
import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept', 'text/plain, */*; q=0.01'),
        ('Accept-Language','zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7'),
        ('Cache-Control','no-cache'),
        ('Host','c1.com')
    ],
    'cookie': [
        ('gr_user_id',''),
        ('',''),
        ('JSESSIONID','')
    ],
    'outline-depth': 10,
}

urlBasePath = './crawlerConfluence/crawlerConfluence/spiders/urls'
files = os.listdir(urlBasePath)

for i in files:
    print(i)
    cc = os.path.join(os.path.abspath(urlBasePath), i)
    with open(cc, 'r', encoding='utf-8') as f:
        time.sleep(5)
        url = f.readline()
        pdfFileName = i + '.pdf'
        print(url)
        pdf = pdfkit.from_url(url, i + '.pdf' ,options=options)
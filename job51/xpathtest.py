import re




'''
text='\r\n\t\t\t\t民营公司    \t\t    \t\t\t\xa0\xa0|\xa0\xa0少于50人    \t\t    \t\t    \t\t\t\xa0\xa0|\xa0\xa0影视/媒体/艺术/文化传播,广告    \t\t\t\t\t'


pa = re.compile('\W(\w+)\W')

result=pa.findall(text)[0:]
print(result)

item={}
target_list=['无工作经验', '大专', '招8人', '10-19发布']
for i in target_list:
    if re.search(pattern="经验",string=i):
        item['Require_exp']=i

    if re.search(pattern='高中|中专|大专|本科|硕士|博士',string=i):
        item['Require_degree']=i

    if re.search(pattern='人',string=i):
        item['Require_number']=i

    if re.search(pattern='发布',string=i):
        item['Job_update']=i

    if re.search(pattern='语|话',string=i):
        item['Require_lan']=i

print(item)
'''
target=['\r\n\t\t\t\t\t\t\t\t','\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t', '\r\n\t\t\t\t\t\t\t\t', '双凤开发区辉山路\t\t\t\t\t\t\t']

for i in target:
    if re.search(pattern='(\w+)\W+',string=i):
        print(i)

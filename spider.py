from lxml import etree
import time
import pandas as pd
import requests

cookies = {
    'qcc_did': 'c5dbc819-7bf0-4e9b-ba5d-582d3c832b86',
    'UM_distinctid': '17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4',
    'acw_tc': '3ad7921216486413121376260e84f3bad3f3ebcb6be0093ca0e38fb00b',
    'QCCSESSID': '9661c5941243678b7bbfd1b7c5',
    'CNZZDATA1254842228': '1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648639087',
}

headers = {
    'authority': 'www.qcc.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.qcc.com/',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'qcc_did=c5dbc819-7bf0-4e9b-ba5d-582d3c832b86; UM_distinctid=17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4; acw_tc=3ad7921216486413121376260e84f3bad3f3ebcb6be0093ca0e38fb00b; QCCSESSID=9661c5941243678b7bbfd1b7c5; CNZZDATA1254842228=1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648639087',
}
proxies = { "http": None, "https": None}
cookie = {
    'qcc_did': 'c5dbc819-7bf0-4e9b-ba5d-582d3c832b86',
    'UM_distinctid': '17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4',
    'QCCSESSID': '9661c5941243678b7bbfd1b7c5',
    'acw_tc': '3ad837a616487735016983919e28cc34fe97435625d73fbe26753c8726',
    'CNZZDATA1254842228': '1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648766817',
}

header = {
    'authority': 'www.qcc.com',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://www.qcc.com/web/search?key=A%E8%82%A1',
    'accept-language': 'zh-CN,zh;q=0.9',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'qcc_did=c5dbc819-7bf0-4e9b-ba5d-582d3c832b86; UM_distinctid=17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4; QCCSESSID=9661c5941243678b7bbfd1b7c5; acw_tc=3ad837a616487735016983919e28cc34fe97435625d73fbe26753c8726; CNZZDATA1254842228=1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648766817',
}
cookies1 = {
    'qcc_did': 'c5dbc819-7bf0-4e9b-ba5d-582d3c832b86',
    'UM_distinctid': '17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4',
    'QCCSESSID': '9661c5941243678b7bbfd1b7c5',
    'acw_tc': '3ad8379616486464676367954ed17ad9142ba6670d2654c87d1646448e',
    'CNZZDATA1254842228': '1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648638644',
}


company_name = []
code = []
more = []
IPC_list = []
Data_list = []
UserName_list = []
Type_list = []
publicNum_list = []
i=0
for page in range(1,126):
    params = {
        'key': 'A\u80A1',
        'p': page,
        'pageSize': '40',
    }

    response = requests.get('https://www.qcc.com/web/search', headers=headers, params=params, cookies=cookies,proxies = proxies)
    html = response.text
# 数据解析
    tree = etree.HTML(html)
    li_list = tree.xpath('//div[@class="search-cell"]/table/tr/td[3]/div/div/span/a/span/text()')
    code_list = tree.xpath("//div[@class='tags']/span/span/span/span/text()")
    url_list = tree.xpath("//div[@class='search-cell']/table/tr/td[3]/div/div/span/a/@href")
    # code.extend(code_list)
    # company_name.extend(li_list)
    print("第", page, "页数据爬取完成")
    print(code_list)

    for url1 in url_list:
        url2 = str(url1).replace("firm","cassets")
        #print(url2)
        responses = requests.get(url2, headers=header, cookies=cookie)

        # print(responses)
        next_Html = responses.text
        trees=etree.HTML(next_Html)
        next_url_list = trees.xpath("//div[@class='app-ntable']/table/tr/td[10]/div/span/a/@href")
        # print(url1)
        # print(next_url_list)
        for next_url in next_url_list:

            next_url = 'https://www.qcc.com'+next_url
            headers1 = {
                'authority': 'www.qcc.com',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-user': '?1',
                'sec-fetch-dest': 'document',
                'referer': next_url,
                'accept-language': 'zh-CN,zh;q=0.9',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'qcc_did=c5dbc819-7bf0-4e9b-ba5d-582d3c832b86; UM_distinctid=17fc9ee69a9142-0a10b64a70c6ec-9771a3f-144000-17fc9ee69aaee4; QCCSESSID=9661c5941243678b7bbfd1b7c5; acw_tc=3ad8379616486464676367954ed17ad9142ba6670d2654c87d1646448e; CNZZDATA1254842228=1123474496-1648358287-https%253A%252F%252Fwww.baidu.com%252F%7C1648638644',
            }
            response1 = requests.get(next_url, headers=headers1, cookies=cookies1,proxies = proxies)
            html1 = response1.text
            tree1 = etree.HTML(html1)
            IPC = tree1.xpath('//div[@class="sub-part"]/table/tr[4]/td[2]/text()')
            Date = tree1.xpath('//div[@class="sub-part"]/table/tr[1]/td[4]/text()')
            User_name = tree1.xpath('//div[@class="sub-part"]/table/tr/td[2]/span/a/text()')
            public_Num = tree1.xpath('//div[@class="sub-part"]/table/tr[2]/td[2]/text()')
            Type = tree1.xpath('//div[@class="sub-part"]/table/tr[5]/td[2]/text()')
            print( li_list[i],IPC,Date,Type,public_Num,User_name,i)
            IPC_list.append(IPC)
            Data_list.append(Date)
            publicNum_list.append(public_Num)
            Type_list.append(Type)
            UserName_list.append(User_name)
            company_name.append(li_list[i])
            code.append(code_list[i])
            time.sleep(0)
            #print("111111")
        i = i + 1
    time.sleep(20)
    i = 0

company_name = pd.DataFrame(company_name)
code = pd.DataFrame(code)
IPC_list = pd.DataFrame(IPC_list)
Data_list = pd.DataFrame(Data_list)
publicNum_list = pd.DataFrame(publicNum_list)
Type_list = pd.DataFrame(Type_list)
UserName_list = pd.DataFrame(UserName_list)
company_name.to_excel("finish.xlsx",index=False)
code.to_excel("finish1.xlsx",index=False)
IPC_list.to_excel("finish2.xlsx",index=False)
Data_list.to_excel("finish3.xlsx",index=False)
publicNum_list.to_excel("finish4.xlsx",index=False)
Type_list.to_excel("finish5.xlsx",index=False)
UserName_list.to_excel("finish6.xlsx",index=False)





import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import html.parser
import urllib.request



def main():

    driver = webdriver.Chrome()
    driver.get('https://www.zhihu.com/question/40273344')
    print('------ start ------')
    print(driver.title, end='\n')

    time.sleep(5)
    driver.save_screenshot('40273344.png')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)

    result_res = driver.page_source
    print(result_res)
    result_soup = BeautifulSoup(result_res, 'lxml')
    result_bf = result_soup.prettify()

    with open("./output/rawfile/raw_result.txt", 'w', encoding="utf-8") as girls:
        girls.write(result_bf)
    girls.close()
    print('页面结构爬取完成')

    with open("./output/rawfile/noscript_meta.txt", 'wb') as noscript_meta:
        noscript_nodes = result_soup.find_all('noscript')  # 找到所有<noscript>node
        noscript_inner_all = ""
        for noscript in noscript_nodes:
            noscript_inner = noscript.get_text()  # 获取<noscript>node内部内容
            noscript_inner_all += noscript_inner + "\n"

        noscript_all = html.parser.unescape(noscript_inner_all).encode('utf-8')  # 将内部内容转码并存储
        noscript_meta.write(noscript_all)

    noscript_meta.close()
    print("爬取noscript标签成功!!!")

    img_soup = BeautifulSoup(noscript_all, 'html.parser')
    img_nodes = img_soup.find_all('img')
    with open("./output/rawfile/img_meta.txt", 'w') as img_meta:
        count = 0
        for img in img_nodes:
            if img.get('src') is not None:
                img_url = img.get('src')

                line = str(count) + "\t" + img_url + "\n"
                img_meta.write(line)
                urllib.request.urlretrieve(img_url, "./output/image/" + str(count) + ".jpg")  # 一个一个下载图片
                print('已下载第{}个图片，图片url = {}'.format(count+1, img_url))
                count += 1

    img_meta.close()
    print("图片下载成功")


if __name__ == '__main__':
    main()
    pass
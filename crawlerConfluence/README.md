
# Scrapy

> Scrapy Engine: 负责 Spider、Item Pipeline、Downloader、Scheduler 中间的通讯、信号、数据传递等  
> Scheduler: 接受 Engine 发送过来的 Request 请求，并按一定的方式进行整理排列、入队，当 Engine 需要时，交还给 Engine  
> Downloader: 负责下载 Engine 发送的 Requests 请求，并将其获取到的 Responses 交换给 Engine，并交给 Spider 来处理  
> Spider: 负责处理所有的 Response，从中分析提取数据，获取 Item 字段需要的数据，并将需要跟进的 URL 提交给引擎，再次进入 Scheduler  
> Item Pipeline: 处理 Spider 中获取到的 Item，并进行后期处理（详细分析、过滤、存储等）  

## 1.创建 scrapy 项目

```sh
$cd ~/python-tools/
$scrapy startproject crawlerConfluence
```

## 2.目录结构

```sh
├── crawlerConfluence
│   ├── __init__.py
│   ├── items.py // 目标文件
│   ├── middlewares.py
│   ├── pipelines.py // 管道文件
│   ├── settings.py // 设置文件
│   └── spiders // 存储爬虫代码目录
│       └── __init__.py
└── scrapy.cfg // 配置文件
```

## 3.创建爬虫

```sh
$cd ~/python-tools/crawlerConfluence/crawlerConfluence/spiders/
$scrapy genspider easemob "c1.com"
```

## 4.运行爬虫

```sh
$cd ~/python-tools/crawlerConfluence/crawlerConfluence/spiders/
$scrapy crawl easemob
```

## 5.使用全局默认的HEADER

```
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/plain, */*; q=0.01",
   "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
   "Cache-Control":"no-cache",
   "Host":"",
   "Cookie":""
}
```

## 6.控制请求频率

```
# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3
```

## 7.启用 PIPELINES

```
# Configure item pipelines
ITEM_PIPELINES = {
   "crawlerConfluence.pipelines.CrawlerconfluencePipeline": 300,
}
```

Twisted 作为核心引擎  osyncio   IO等待时间  单线程进阶版（不等时间）

步骤
1 爬虫拿到 start_urls,封装为Requsest请求对象   但不会真正的去请求
2 调度器队列  先进先出   yield Request(url,callback=self.parse)  会把请求对象放到调度器中
3 下载器从调度器中拿到请求对象，去请求，拿到响应
4 响应会封装成Response对象   -》发送服务器信息， 收回
5 响应对象会传递给Spider的parse方法
6 yield Item() 会把数据放到管道中
7 管道中处理数据
8 yield Request() 会把请求对象放到调度器中

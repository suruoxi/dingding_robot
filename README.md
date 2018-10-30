# dingding_rebot
钉钉机器人定时提醒喝水、休息等，可区分工作日和节假日

## 自动发消息

依赖于钉钉。微信有各种限制。

钉钉机器人文档: https://open-doc.dingtalk.com/docs/doc.htm?treeId=257&articleId=105735&docType=1    
给自己发送的办法： 拉一个群，然后把其他人移除，只剩自己. 得到webhook地址，放在url.txt中    
这个代码里是发送纯文本，还可以发送图片、卡片等消息.    

## 节假日判断

chinesecalendar这个库

## 定时调度

apscheduler, 类似cron

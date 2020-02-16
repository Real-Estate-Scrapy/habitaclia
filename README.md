# Habitaclia

curl http://scrapyd:6800/schedule.json \
-d project=habitaclia_1 \
-d _version=2019-12-31T18_04_11 \
-d spider=spider \
-d jobid=2019-12-31T18_04_32 \
-d setting=CLOSESPIDER_PAGECOUNT=10 \
-d setting=CLOSESPIDER_TIMEOUT=60 \
-d arg1=val1 \
-d page_url=https://www.habitaclia.com/comprar-casa-magnifica_en_pedralbes_pedralbes-barcelona-i4737001535271.htm


```
crawl spider -a page_url=https://www.habitaclia.com/viviendas-centre-terrassa.htm
```

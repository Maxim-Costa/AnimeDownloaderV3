#!/bin/bash
if [[ "$1" == "" ]]; then
  echo "     cusi By BladeMight, v1.0"
  echo "$0 <sibnet-url> <*commands-str>"
  echo "In command str you can use variables:"
  echo " \\\$du = direct url"
  echo " \\\$ti = title"
  echo " \\\$id = id"
  echo " \\\$au = accept url"
  echo "You must escape variables, so they can be processed in code!, Or you can use single quotes ''"
  echo "command str examples:"
  echo "  cusi <url> 'aria2c \"\$du\" -o \"\$ti\"'"
  echo "  cusi <url> 'ffmpeg -i \"\$du\"'"
  exit 0
fi
url="$1"
H1="Accept-Encoding: identity;q=1, *;q=0"
H2="Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5"
H3="User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36"
H4="chrome-proxy: frfr"
H5="Accept: */*"
H6="Connection: keep-alive"
H7="Range: bytes=0-"
H8="Referer: $url"
resp=$(curl -s -H "$H1" -H "$H2" -H "$H3" -H "$H4" -H "$H5" -H "$H6" -H "$H7" --compressed "$url" | iconv -f cp1251 -t utf-8 )
accepturl=$(echo "$resp" | grep -iP '\d+\.mp4' | sed -re 's/.*(\/v\/.*?mp4)", type.*/https:\/\/video.sibnet.ru\1/g')
id=$(echo "$resp" | grep -i DOCTYPE | sed -re 's/.*php\?videoid=([0-9]*).*/\1/g')
#echo "Video-Id: $id"
title=$(echo "$resp" | grep -iP 'videoname' | sed -re 's/.*?videoName.>(.*?)<\/h1>.*/\1/g')
#echo "Video-Title: $title"
#echo "Accept-URL: $accepturl"
directurl=$(curl -I "$accepturl" -s -H "$H1" -H "$H2" -H "$H3" -H "$H4" -H "$H5" -H "$H6" -H "$H7" -H "$H8" --compressed | awk 'BEGIN{IGNORECASE=1} match($0, /location: (.*)/, z) {printf "https:%s", z[1]}')
echo "$directurl"
if [[ "$2" != "" ]]; then
  echo "Eval mode."
  au="$accepturl"
  du="$directurl"
  ti=$(echo "$title" | sed -re 's/\\|\/|\*|:|\"|<|>|\?|\|//g') # safe title
  eval $2
fi

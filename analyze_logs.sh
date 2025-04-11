#!/bin/bash

sum_requests=$(wc -l < access.log)
echo "Общее количество запросов: $sum_requests" >> report.txt

unique_ip=$(awk '{print $1}' access.log | sort | uniq | wc -l)
echo "Количество уникальных IP-адресов: $unique_ip" >> report.txt

method_count=$(awk '{print $6}' access.log | cut -d\" -f2 | sort | uniq -c)
echo "Количество запросов по методам:" >> report.txt
echo "$method_count" | awk '{print $1 " " $2}' >> report.txt

popular_url=$(awk '{print $7}' access.log | sort | uniq -c | sort -nr | head -n 1)
count=$(echo $popular_url | awk '{print $1}')
url=$(echo $popular_url | awk '{print $2}')
echo "Самый популярный URL: $count $url" >> report.txt

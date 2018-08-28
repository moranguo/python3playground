#!/bin/bash

# Array pretending to be a Pythonic dictionary
machine_list=( "inin01:ip1"
"inin02:ip2"
"rein01:ip3"
"rein02:ip4" )
path='/home/ztrend/monitor_script'
file='count.txt'
local_file=$path'/'$file

total=0
output_zenoss=''
#output_s3_bucket=''
for host in "${machine_list[@]}" ; do
    host_name="${host%%:*}"
    host_ip="${host##*:}"
    ret=`ssh ${host_ip} '/bin/ls /var/spool/nebula/data/inmta/dead-mail | /usr/bin/wc -l'`
    count=$(($ret/2))
    total=$((total+$count))
    output_zenoss=$output_zenoss$host_name'='$count';'
    #output_s3_bucket=$output_s3_bucket$host_name':'$count"\n"
done

output='|total='$total';'$output_zenoss
output_s3='total='$total';'$output_zenoss
#output_s3='total:'$total"\n"$output_s3_bucket
#output_s3=${output_s3::${#output_s3}-2}
echo -n $output_s3 > $local_file

#shell script to access s3 bucket in eu-central-1 report below issue:
#The authorization mechanism you have provided is not supported. Please use AWS4-HMAC-SHA256
#change to use python up upload file to s3, need to install boto3 on instance
python $path"/upload_s3.py"

if [ $total -gt 0 ]
then
    echo "WARNING total $total dead mail found"$output
    exit 1
else
    echo "OK no dead mail found"$output
    exit 0
fi

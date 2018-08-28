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

S3KEY="xxx"
S3SECRET="xxx" # pass these in

function putS3
{
  path=$1
  file=$2
  aws_path=$3
  bucket='test-bucket'
  date=$(date +"%a, %d %b %Y %T %z")
  acl="x-amz-acl:public-read"
  content_type='application/x-compressed-tar'
  string="PUT\n\n$content_type\n$date\n$acl\n/$bucket$aws_path$file"
  signature=$(echo -en "${string}" | openssl sha1 -hmac "${S3SECRET}" -binary | base64)
  curl -X PUT -T "$path/$file" \
    -H "Host: $bucket.s3.amazonaws.com" \
    -H "Date: $date" \
    -H "Content-Type: $content_type" \
    -H "$acl" \
    -H "Authorization: AWS ${S3KEY}:$signature" \
    "https://$bucket.s3.amazonaws.com$aws_path$file"
}

putS3 $path $file "/"


if [ $total -gt 0 ]
then
    echo "WARNING total $total dead mail found"$output
    exit 1
else
    echo "OK no dead mail found"$output
    exit 0
fi

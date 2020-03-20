#!/bin/bash
cd  /var/www/mediawiki/bmeg-wiki
while :
do
	php maintenance/runJobs.php --memory-limit max --maxjobs 100 --wait
	sleep 1
done

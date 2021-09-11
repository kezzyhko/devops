# Monitoring


Table of contents:  
[Disclaimer](#disclaimer)  
[Report and screenshots](#report-and-screenshots)  
[Best practices](#best-practices)  


## Disclaimer

We were provided with example repo in the task: https://github.com/black-rosary/loki-nginx  
Part of config files in this folder was taken form the above mentioned repo.  


## Report and screenshots

Grafana works:  
![](report_screenshots/grafana/login.png)  
![](report_screenshots/grafana/welcome.png)  

Prometheus works:  
![](report_screenshots/prometheus.png)  

All data sources are present:  
![](report_screenshots/data-sources/list.png)  
![](report_screenshots/data-sources/loki.png)  
![](report_screenshots/data-sources/tested.png)  

And they are working:  
![](report_screenshots/logs/loki.png)  
![](report_screenshots/logs/prometheus.png)  

Dashboards are added as well:  
![](report_screenshots/dashboards/loki.png)  
![](report_screenshots/dashboards/prometheus.png)  


## Best practices

* Dynamic labels should not be used freequently
* Caching should be configured
* Dashboards should be logically separated
* Dashboards should be consistent
* When copying a dashboard, you should not copy tags

# Monitoring


## Mentions

Thanks to the following repo for example of config files:  
https://github.com/black-rosary/loki-nginx


## Screenshots of working system

Grafana works:  
![](report_screenshots/grafana-login.png)  
![](report_screenshots/grafana-welcome.png)  

All data sources are present:  
![](report_screenshots/data-sources-loki.png)
![](report_screenshots/data-sources-list.png) 

And everything is working:  
![](report_screenshots/logs-loki.png)
![](report_screenshots/logs-prometheus.png)


## Best practices

* Dynamic labels should not be used freequently
* Caching should be configured
* Dashboards should be logically separated
* Dashboards should be consistent
* When copying a dashboard, you should not copy tags

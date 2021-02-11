FROM docker.elastic.co/beats/metricbeat:7.7.0
COPY metricbeat.yml /etc/metricbeat/metricbeat.yml
USER root
RUN chown root:metricbeat /etc/metricbeat/metricbeat.yml
RUN chmod go-w /etc/metricbeat/metricbeat.yml
USER metricbeat
CMD ["-environment", "container"]
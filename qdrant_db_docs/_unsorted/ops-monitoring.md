---
title: Monitoring & Telemetry
source: https://qdrant.tech/documentation/ops-monitoring/
---

# Monitoring & Telemetry

These pages cover how to observe and measure a running Qdrant deployment using its built-in metrics endpoints and external monitoring tools.

## Monitoring & Telemetry

[Monitoring & Telemetry](https://qdrant.tech/documentation/ops-monitoring/monitoring/) ([local](./ops-monitoring/monitoring.md)) describes the Prometheus/OpenMetrics-compatible `/metrics` endpoint, the available metrics, and how to connect Qdrant to a Prometheus and Grafana monitoring stack.

## Managed Cloud Prometheus Monitoring

[Managed Cloud Prometheus Monitoring](https://qdrant.tech/documentation/ops-monitoring/managed-cloud-prometheus/) ([local](./ops-monitoring/managed-cloud-prometheus.md)) is a step-by-step tutorial for deploying Prometheus and Grafana in a Kubernetes cluster and configuring them to scrape metrics from a Qdrant Managed Cloud database.

## Self-Hosted Prometheus Monitoring

[Self-Hosted Prometheus Monitoring](https://qdrant.tech/documentation/ops-monitoring/hybrid-cloud-prometheus/) ([local](./ops-monitoring/hybrid-cloud-prometheus.md)) is a step-by-step tutorial for setting up Prometheus and Grafana monitoring for Qdrant running in a Hybrid Cloud or Private Cloud environment.

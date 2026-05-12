---
title: Optimization
source: https://qdrant.tech/documentation/ops-optimization/
---

# Optimization

These pages cover strategies and internal mechanisms for improving search performance, reducing memory usage, and managing how Qdrant organizes data on disk.

## Optimize Performance

[Optimize Performance](https://qdrant.tech/documentation/ops-optimization/optimize/) ([local](./ops-optimization/optimize.md)) walks through three main optimization scenarios — high-speed search, high-precision search, and low memory usage — and the configuration choices that achieve each one.

## Optimizer

[Optimizer](https://qdrant.tech/documentation/ops-optimization/optimizer/) ([local](./ops-optimization/optimizer.md)) explains how Qdrant’s background optimizer rebuilds segments to keep data structures efficient, including the vacuum, merge, and indexing stages and the thresholds that trigger them.

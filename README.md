## Stage 1: Python Foundations Through Useful Projects (Core Syntax & Logic)

- **Project 1.1: Courier Tiering & Routing Engine.** Multi-conditional logic to automatically assign shipping carriers based on package weight, destination, and SLA tier.

**STATUS**: Project 1.1 Complete. Moving to Project 1.2.
**COMPANY**: OmniMart Logistics (3PL/Fulfillment)
**SYSTEMS BUILT**: Courier Routing Engine v1.0
**KPIs TRACKED**: SLA Alignment %, Core Cost-per-Order Routing
**CURRENT readiness**: Python 12%, Analytics 5%, Portfolio 5%
**OBJECTIVES**: Functional programming, pricing tiers, mathematical logic.

- **Project 1.2: Dynamic Fulfillment Fee Calculator.** Custom functions to calculate variable warehouse picking/packing fees with volume-based tier discounts.

**STATUS**: Project 1.2 Complete. Moving to Project 1.3.
**COMPANY**: OmniMart Logistics (3PL/Fulfillment)
**SYSTEMS BUILT**: Courier Routing Engine v1.0, Dynamic Billing Engine v1.0
**KPIs TRACKED**: Revenue Integrity, Invoicing Error Margin, Variable Volume Margins
**CURRENT READINESS**: Python 18%, Analytics 12%, Portfolio 10%
**OBJECTIVES**: Transition into data collections, dictionary mappings, and loops.

- **Project 1.3: Warehouse Inventory Audit Reconciliation.** Loop and dictionary manipulation to compare physical counts against systemic inventory tables, identifying variances.
- **Project 1.4: Multi-Client Manifest Aggregator.** List and string processing to parse raw, poorly formatted shipping manifests from different external e-commerce clients.
- **Project 1.5: SLA Breach Alert System.** Structural exception handling and modular functions to scan operational timestamps and flag high-priority delivery delays.
- **Project 1.6: Fulfillment Center Access Control Logger.** File I/O operations to read, parse, and safely write security access logs, highlighting unauthorized off-hours entries.

---

## Stage 2: Data-Focused Python Projects (I/O, Quality, & Automation)

- **Project 2.1: Automated Shipping Manifest Validator.** Ingestion of raw CSV manifests with rigorous type checking, missing value isolation, and error log generation.
- **Project 2.2: Client Configuration Parser.** Utilizing JSON configurations to build a system that dynamically adapts processing rules based on individual client SLAs.
- **Project 2.3: Weekly Operations Summary Generator.** Aggregating raw transaction logs to calculate descriptive baseline statistics (mean, median, IQR) without external libraries.
- **Project 2.4: The Silent Corruption Detector.** Defensive script writing with a comprehensive test plan to flag corrupted timestamps and negative weight values in incoming streams.
- **Project 2.5: Legacy System Data Transformer.** Converting chaotic flat-file text reports from legacy warehouse systems into structured, normalized relational-ready CSV files.
- **Project 2.6: Automated PDF/Text Invoice Generator.** Compiling calculated operational metrics into clean, reproducible plain-text billing summaries for the finance team.

---

## Stage 3: Junior Data Analyst Projects (The Modern Analytics Stack)

- **Project 3.1: Order Ingestion & Vectorized Profiling.** Migrating legacy scripts to NumPy and Pandas for high-speed, vectorized tracking of daily fulfillment volume.
- **Project 3.2: Warehouse Capacity Bottleneck Analysis.** Utilizing advanced Pandas filtering, grouping, and merging to identify fulfillment centers exceeding 85% utilization.
- **Project 3.3: Operational KPI Dashboard Engines.** Translating raw data into structured visual performance profiles using Matplotlib and Seaborn (tracking On-Time Delivery % and Cost-per-Order).
- **Project 3.4: Customer Cohort Churn Identification.** Analyzing e-commerce client behavior over time to isolate accounts with declining order volumes using windowing concepts.
- **Project 3.5: Carrier Performance & SLA Drilldown.** Statistical profiling of transit times across different shipping partners to prove or disprove systemic delivery delays.
- **Project 3.6: Relational Database Blueprinting (SQL Readiness).** Transforming flat dataframes into structured schemas, enforcing primary/foreign keys via Python-driven SQLite databases.

---

## Stage 4: Portfolio-Worthy Data Analyst Projects (Storytelling & Stakeholder Impact)

- **Project 4.1: The Labor Optimization Crisis.** Comprehensive analysis combining warehouse shift logs, order volume, and labor costs to pinpoint operational inefficiencies. Includes an executive presentation.
- **Project 4.2: E-Commerce Client Profitability Audit.** End-to-end data pipeline evaluating margin leakage from high-volume clients abusing custom fulfillment exceptions.
- **Project 4.3: Interactive Supply Chain Health Explorer.** Creating an advanced, interactive multi-view visualization suite mapping nationwide delivery delays and bottlenecked hubs.
- **Project 4.4: Historical Trend & Seasonality Playbook.** Deep-dive time-series analysis isolating Q4 peak-season spikes to dictate seasonal hiring targets for operations.
- **Project 4.5: Executive Quarterly Business Review (QBR) Engine.** A completely automated, professional markdown-and-visualization pipeline that generates high-level stakeholder reports.
- **Project 4.6: The Legacy Codebase Refactoring Audit.** A capstone engineering project where you pull your early Stage 1 code, rewrite it using professional modular design patterns, add unit tests, and write a comprehensive production README.

---

## Stage 5: Beginner Data Science Projects (Machine Learning & Predictive Modeling)

- **Project 5.1: Fulfillment Failure Predictor (Classification).** Feature engineering on historical metadata to predict the likelihood of an order missing its delivery SLA before it leaves the hub.
- **Project 5.2: Daily Order Volume Forecasting (Time Series / Regression).** Implementing statistical and basic predictive modeling to forecast incoming daily parcel volumes for labor scheduling.
- **Project 5.3: Warehouse Storage Space Optimization (Clustering).** Segmenting inventory SKUs based on velocity (turnover rate) and physical size to optimize pick-path layout designs.
- **Project 5.4: Delivery Route Anomaly & Fraud Detection.** Isolating anomalous driver transit durations and atypical fuel charges using statistical distance and outlier models.
- **Project 5.5: AB Testing Framework for Fulfillment Layouts.** Designing, executing, and statistically evaluating a split-test comparing two different warehouse picking methodologies.
- **Project 5.6: The Production Model Handover.** Packaging your top-performing predictive model into an operational python script with comprehensive logging, metrics evaluation, and a monitoring architecture.

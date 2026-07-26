# Elastic SOC Dashboard

## Overview

This dashboard is designed to monitor security events and assist SOC analysts during investigations.

## Dashboard Objectives

- Monitor security alerts
- Identify suspicious activities
- Analyze endpoint events
- Support incident investigation

## Visualizations

### 1. Alert Severity Distribution

Purpose:
- Display alerts by severity level.
- Help analysts prioritize critical incidents.

Data:
- event.severity

---

### 2. Top Alert Sources

Purpose:
- Identify systems generating the most alerts.

Data:
- host.name
- agent.name

---

### 3. Process Execution Monitoring

Purpose:
- Investigate suspicious processes.

Data:
- process.name
- process.command_line

---

### 4. Network Activity Monitoring

Purpose:
- Analyze suspicious connections.

Data:
- source.ip
- destination.ip
- destination.port

---

## Investigation Workflow

1. Review alert severity.
2. Identify affected host.
3. Analyze related logs.
4. Check process execution.
5. Investigate network indicators.
6. Document findings.

## Tools

- Elastic Security
- Kibana
- Sysmon
- Windows Event Logs

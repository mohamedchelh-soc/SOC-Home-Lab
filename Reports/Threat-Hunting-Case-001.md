# Threat Hunting Case - Suspicious PowerShell Activity

## 1. Objective

Identify suspicious PowerShell activity that may indicate malicious execution on Windows endpoints.

## 2. Hypothesis

An attacker may use PowerShell to execute encoded commands, download payloads, or perform unauthorized actions.

## 3. Data Sources

- Windows Event Logs
- Sysmon Logs
- Elastic Security Events

## 4. Hunting Queries

Investigated:

- PowerShell execution events
- Encoded command usage
- Suspicious command patterns
- Network connections from PowerShell processes

## 5. Investigation Steps

1. Search PowerShell execution events.
2. Review command-line arguments.
3. Identify suspicious parent processes.
4. Check related network activity.
5. Validate indicators.

## 6. Findings

No confirmed malicious activity found during the investigation.

## 7. Recommendations

- Monitor PowerShell activity.
- Enable enhanced logging.
- Create detection rules for suspicious commands.
- Review privileged user activity.

## 8. Tools Used

- Elastic Security
- Kibana
- Sysmon
- MITRE ATT&CK Framework

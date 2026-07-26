# MITRE ATT&CK Mapping

## Overview

This document maps the SOC Home Lab activities to MITRE ATT&CK techniques.

## Techniques

| Technique | ID | Description |
|---|---|---|
| PowerShell | T1059.001 | Command and Scripting Interpreter: PowerShell |
| Command Execution | T1059 | Command and Scripting Interpreter |
| Network Service Scanning | T1046 | Network discovery using scanning tools |
| File and Directory Discovery | T1083 | Discover files and directories |
| Process Discovery | T1057 | Identify running processes |

## Detection Coverage

The lab demonstrates detection and investigation of:

- Suspicious PowerShell execution
- Abnormal command execution
- Network reconnaissance activity
- Endpoint investigation

## Tools Used

- Elastic Security
- Sysmon
- Windows Event Logs
- MITRE ATT&CK Framework

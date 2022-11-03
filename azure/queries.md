# azure monitor queries

```
let startTimestamp = ago(24h);
KubePodInventory
| where TimeGenerated > startTimestamp
| project ContainerID, PodName=Name, Namespace
| where PodName contains "api" and Namespace startswith "dev"
| distinct ContainerID, PodName
| join
(
    ContainerLog
    | where TimeGenerated > startTimestamp
)
on ContainerID
| project TimeGenerated, PodName, LogEntry, LogEntrySource
| summarize by TimeGenerated, LogEntry
| order by TimeGenerated desc
```
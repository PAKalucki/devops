# log insight usefull queries

# lambda duration
```
filter @type = "REPORT"
| fields @requestId, @billedDuration
| sort by @billedDuration desc
```

# lambda cold starts
```
filter @type = "REPORT" |
parse @message /Init Duration: (?<init>\S+)/ |
stats count() as total, count(init) as coldStarts, median(init) as avgInitDuration, max(init) as maxInitDuration, avg(@maxMemoryUsed)/1000/1000 as memoryused
```

# lambda memory
```
filter @type = "REPORT"
| stats max(@memorySize / 1000 / 1000) as provisonedMemoryMB,
  min(@maxMemoryUsed / 1000 / 1024) as smallestMemoryRequestMB,
  avg(@maxMemoryUsed / 1024 / 1024) as avgMemoryUsedMB,
  max(@maxMemoryUsed / 1024 / 1024) as maxMemoryUsedMB,
  provisonedMemoryMB - maxMemoryUsedMB as overProvisionedMB
```
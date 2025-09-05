# SNMP component for ESPHome

This is an external ESPHome component that enables support for SNMP protocol. The protocol is widely used in network management and network monitoring.

**Original Documentation:** https://aquaticus.info/snmp.html

**Integration tests:** https://github.com/aquaticus/esphome_snmp_tests

Tested with ESPHome version 2025.8.1


# New features

## Installation:
```yaml
# Retrieve SNMP component from github
external_components:
  - source: github://mmiller1br/esphome-snmp
```

## Config Example
```yaml
# Enable SNMP component
snmp:
  contact: YOUR-NAME
  location: YOUR-LOCATION
  read_community: "READ-ONLY"
  write_community: "READ-WRITE"
  temperature: my_temp_sensor
  humidity: my_humid_sensor
```

## Configuration Variables

- **contact** (Optional, string): Value for sysContact (1.3.6.1.2.1.1.4) OID. Defaults to an empty string.
- **location** (Optional, string): Value for sysLocation (1.3.6.1.2.1.1.6) OID. Defaults to an empty string.
- **read_community** (Optional, string): name of the READ ONLY community. Defaults to "public".
- **write_community** (Optional, string): name of the READ WRITE community. Defaults to "private".
- **temperature** (Optional, string): ID of a sensor with temperature information. Values will be publiched as INTEGER, for example 20.5 is equal to 215.
- **humidity** (Optional, string): ID of a sensor with humidity information. Values will be publiched as INTEGER, for example 67.8 is equal to 678.


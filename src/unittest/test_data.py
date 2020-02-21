key1 = "issueSummary"
key2 = "XY&^$#*@!1234%^&"

data = {
  "id": "AWcvsjx864kVeDHDi2gB",
  "instanceId": "E-NETWORK-EVENT-AWcvsjx864kVeDHDi2gB-1542693469197",
  "category": "Warn",
  "status": "NEW",
  "timestamp": 1542693469197,
  "severity": "P1",
  "domain": "Availability",
  "source": "DNAC",
  "priority": "P1",
  "type": "Network",
  "title": "Device unreachable",
  "description": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
  "actualServiceId": "10.10.20.82",
  "assignedTo": "",
  "enrichmentInfo": {
    "issueDetails": {
      "issue": [
        {
          "issueId": "AWcvsjx864kVeDHDi2gB",
          "issueSource": "Cisco DNA",
          "issueCategory": "Availability",
          "issueName": "snmp_device_down",
          "issueDescription": "This network device leaf2.abc.inc is unreachable from controller. The device role is ACCESS.",
          "issueEntity": "network_device",
          "issueEntityValue": "10.10.20.82",
          "issueSeverity": "HIGH",
          "issuePriority": "",
          "issueSummary": "Network Device 10.10.20.82 Is Unreachable From Controller",
          "issueTimestamp": 1542693469197,
          "suggestedActions": [
            {
              "message": "From the controller, verify whether the last hop is reachable.",
              "steps": []
            },
            {
              "message": "Verify that the physical port(s) on the network device associated with the network device discovery(IP) is UP.",
              "steps": []
            },
            {
              "message": "Verify access to the device.",
              "steps": []
            }
          ],
          "impactedHosts": [
            {
              "hostName": "DUT",
              "hostOs": "Windows",
              "ssid": "Unknown",
              "connectedInterface": "Unknown",
              "failedAttempts": 3,
              "location": {
                "siteId": "SanJose",
                "siteType": "BUILDING",
                "area": "Global",
                "building": "ABC",
                "apsImpacted": []
              },
              "timestamp": 1542693469197
            }
          ]
        }
      ]
    },
    "connectedDevice": [
      {
        "deviceDetails": {
          "family": "Switches and Hubs",
          "type": "Cisco Catalyst 9300 Switch",
          "errorCode": "SNMP-TIMEOUT",
          "macAddress": "50:60:ab:cd:70:80",
          "role": "ACCESS",
          "apManagerInterfaceIp": "",
          "associatedWlcIp": "",
          "bootDateTime": "2020-01-01 00:00:01",
          "collectionStatus": "Partial Collection Failure",
          "interfaceCount": "66",
          "lineCardCount": "1",
          "lineCardId": "022daaff-2a4a-4eb6-9050-91aab668fdf2",
          "managementIpAddress": "10.10.20.21",
          "memorySize": "888963920",
          "platformId": "C9300-48U",
          "reachabilityFailureReason": "Collection Failure",
          "reachabilityStatus": "Unreachable",
          "snmpContact": "",
          "snmpLocation": "",
          "series": "Cisco Catalyst 9300 Series Switches",
          "inventoryStatusDetail": "<status><general code=\"SNMP_TIMEOUT\"/></status>",
          "collectionInterval": "Global Default",
          "serialNumber": "FCW1234L0UZ",
          "softwareVersion": "16.6.3",
          "roleSource": "AUTO",
          "hostname": "leaf2.abc.inc",
          "upTime": "01:08:43.96",
          "lastUpdateTime": 1542693255158,
          "errorDescription": "SNMP timeouts are occurring with this device. Either the SNMP credentials are not correctly provided to controller or the device is responding slow and snmp timeout is low. If its a timeout issue, controller will attempt to progressively adjust the timeout in subsequent collection cycles to get device to managed state. User can also run discovery again only for this device using the discovery feature after adjusting the timeout and snmp credentials as required. Or user can update the timeout and snmp credentials as required using update credentials.",
          "tagCount": "0",
          "lastUpdated": "2018-11-20 05:54:15",
          "instanceUuid": "a7633ae5-d3c9-4aea-837d-c3ad5b19c802",
          "id": "a7633ae5-d3c9-4aea-837d-c3ad5b19c802",
          "neighborTopology": [
            {
              "errorCode": 5000,
              "message": "An internal has error occurred while processing this request.",
              "detail": "An internal has error occurred while processing this request."
            }
          ],
          "cisco360view": "https://10.10.20.22/dna/assurance/home#networkDevice/a7633ae5-d3c9-4aea-837d-c3ad5b19c802"
        }
      }
    ]
  }
}

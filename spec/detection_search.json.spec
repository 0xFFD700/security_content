{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "title": "Detection Search Manifest",
  "description": "The fields that make up the manifest of a version 1 detection search",
  "type": "object",
  "properties": {
    "asset_type": {
      "description": "Designates the type of asset being investigated",
      "type": "string"
    },
    "channel": {
      "description": "A grouping function that designates where this search came from. For example, searches and stories in Enterprise Security Updates are in the ESCU channel",
      "type": "string"
    },
    "confidence": {
      "description": "Confidence that detected behavior is malicious",
      "type": "string"
    },
    "correlation_rule": {
      "type": "object",
      "description": "Various fields to enhance usability in Enterprise Security",
      "properties": {
        "notable": {
          "type": "object",
          "description": "Various fields associated with creating a notable event",
          "properties": {
            "rule_description": {
              "description": "Description of the notable event that will display in Incident Review",
              "type": "string"
            },
            "rule_title": {
              "description": "Title of the notable event that will display in Incident Review",
              "type": "string"
            },
            "nes_fields": {
              "description": "A list of suggested fields to be used for notable-event suppression",
              "type": "string"
            }
          },
          "additionalProperties": false,
          "required": [
            "rule_description",
            "rule_title",
            "nes_fields"
          ]
        },
        "risk": {
          "type": "object",
          "description": "Fields associated with assigning risk to objects",
          "properties": {
            "risk_object": {
              "description": "TThe field to which you are assigning risk",
              "type": "string"
            },
            "risk_object_type": {
              "description": "The type of object to which you’re assigning risk",
              "type": "array",
              "items": {
                "type": "string",
                "enum": [
                  "system",
                  "user",
                  "other"
                ]
              },
              "minItems": 0,
              "maxItems": 1,
              "uniqueItems": true
            },
            "risk_score": {
              "description": "Score assigned to risk_object",
              "type": "integer"
            }
          },
          "additionalProperties": false,
          "required": [
            "risk_score",
            "risk_object",
            "risk_object_type"
          ]
        },
        "suppress": {
          "type": "object",
          "description": "Fields associated with suppressing the creation of multiple alerts",
          "properties": {
            "suppress_fields": {
              "description": "The fields to base the suppression on",
              "type": "string"
            },
            "suppress_period": {
              "description": "The length of time the suppression should be in effect",
              "type": "string"
            }
          },
          "additionalProperties": false,
          "required": [
            "suppress_fields",
            "suppress_period"
          ]
        }
      },
      "additionalProperties": false
    },
    "creation_date": {
      "description": "The date the story manifest was created",
      "type": "string"
    },
    "phantom_playbooks": {
      "description": "Array of recommended playbooks",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "phantom_server": {
            "type": "string",
            "description": "IP address and username of the phantom server. Currently, we will ship this value as automation (hostname) and we encourage the users to modify those values according to their environment. Eg: automation (hostname)"
          },
          "playbook_name": {
            "type": "string",
            "description": "Name of the playbook. This name should be the same as the name on phantom community repository on github with underscores and appended with community/<playbook_name>. The playbooks are hosted on https://github.com/phantomcyber/playbooks. Eg: community/simple_network_enrichment"
          },
          "playbook_display_name": {
            "type": "string",
            "description": "Display Name of the playbook. Capitalize each letter and remove underscores from playbook_name field. Eg: Simple Network Enrichment"
          },
          "playbook_url": {
            "type": "string",
            "description": "Url of the playbook on Phantom website."
          },
          "sensitivity": {
            "type": "string",
            "description": "TLP colors (White, Green, Amber or Red)"
          },
          "severity": {
            "type": "string",
            "description": "Severity in phantom (High, Medium, Low)"
          }
        },
        "additionalProperties": false,
        "required": [
          "phantom_server",
          "playbook_name",
          "sensitivity",
          "severity",
          "playbook_url",
          "playbook_display_name"
        ]
      }
    },
    "data_metadata": {
      "type": "object",
      "description": "Information about the date being ingested",
      "properties": {
        "data_models": {
          "description": "A list of data models, if any, used by this search",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "data_source": {
          "description": "A high-level description of the type of data needed for this search to complete",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "data_sourcetypes": {
          "description": "The list of sourcetypes, if any, used by this search",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "providing_technologies": {
          "description": "A list of technologies that provide this data",
          "type": "array",
          "items": {
            "enum": [
              "Apache",
              "AWS",
              "Bro",
              "Microsoft Windows",
              "Linux",
              "macOS",
              "Netbackup",
              "Splunk Enterprise",
              "Splunk Enterprise Security",
              "Splunk Stream",
              "Active Directory",
              "Bluecoat",
              "Carbon Black Response",
              "Carbon Black Protect",
              "CrowdStrike Falcon",
              "Microsoft Exchange",
              "Nessus",
              "Palo Alto Firewall",
              "Qualys",
              "Sysmon",
              "Tanium",
              "Ziften",
              "OSquery"
            ]
          },
          "minItems": 0,
          "uniqueItems": true
        }
      },
      "additionalProperties": false,
      "required": [
        "data_source",
        "providing_technologies"
      ]
    },
    "eli5": {
      "description": "Explain it like I’m 5 - A detail description of the SPL of the search, written in a style that can be understood by a future Splunk expert",
      "type": "string"
    },
    "how_to_implement": {
      "description": "A discussion on how to implement this search, from what needs to be ingested, config files modified, and suggested per site modifications",
      "type": "string"
    },
    "known_false_positives": {
      "description": "Scenarios in which detected behavior is benig, coupled with suggestions on how to verify the behavior",
      "type": "string"
    },
    "maintainers": {
      "description": "An array of the current maintainers of the Analytic Story.",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "company": {
            "type": "string",
            "description": "Company associated with the person maintaining this search"
          },
          "email": {
            "type": "string",
            "description": "Email address of the person maintaining this search"
          },
          "name": {
            "type": "string",
            "description": "Name of the person maintaining this search"
          }
        },
        "additionalProperties": false,
        "required": [
          "name",
          "email",
          "company"
        ]
      }
    },
    "mappings": {
      "type": "object",
      "description": "Mappings to various industry standards and frameworks",
      "properties": {
        "cis20": {
          "description": "A list of critical security controls this search helps you implement",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "kill_chain_phases": {
          "description": "A list of kill-chain phases to which the search applies",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "mitre_attack": {
          "description": "A list of the techniques and tactics identified by the search",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        },
        "nist": {
          "description": "A list of the NIST controls the search helps you implement",
          "type": "array",
          "items": {
            "type": "string"
          },
          "minItems": 0,
          "uniqueItems": true
        }
      },
      "additionalProperties": false
    },
    "modification_date": {
      "description": "The date of the most recent modification to the search",
      "type": "string"
    },
    "original_authors": {
      "description": "A list of the original authors of the search",
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "company": {
            "type": "string",
            "description": "Company associated with the person who originally authored the search"
          },
          "email": {
            "type": "string",
            "description": "Email address of the person who originally authored the search"
          },
          "name": {
            "type": "string",
            "description": "Name of the person who originally authored the search"
          }
        },
        "additionalProperties": false,
        "required": [
          "name",
          "email",
          "company"
        ]
      }
    },
    "references": {
      "description": "A list of URLs that give more information about the search",
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 0,
      "uniqueItems": true
    },
    "scheduling": {
      "type": "object",
      "description": "Various fields to assist in scheduling the search",
      "properties": {
        "cron_schedule": {
          "description": "Schedule of the search in cron format",
          "type": "string"
        },
        "earliest_time": {
          "description": "The earliest time the search should run in Splunk format",
          "type": "string"
        },
        "latest_time": {
          "description": "The latest time tes search should run against in Splunk format",
          "type": "string"
        }
      },
      "additionalProperties": false
    },
    "search": {
      "description": "The search (in SPL) executed within core Splunk",
      "type": "string"
    },
    "search_description": {
      "description": "A description of what the search is designed to detect",
      "type": "string"
    },
    "search_id": {
      "description": "The unique identifier for the search",
      "type": "string"
    },
    "search_name": {
      "description": "The name of the search",
      "type": "string"
    },
    "search_type": {
      "description": "The type of the search",
      "enum": [
        "detection",
        "investigative",
        "contextual",
        "support"
      ]
    },
    "security_domain": {
      "description": "The high-level security area to which the search belongs",
      "enum": [
        "access",
        "endpoint",
        "network",
        "threat"
      ]
    },
    "spec_version": {
      "description": "The version of the detection search specification this manifest follows",
      "type": "integer"
    },
    "status": {
      "description": "The current status of the search - development, experimental, production",
      "enum": [
        "development",
        "experimental",
        "production"
      ]
    },
    "team_notes": {
      "description": "Notes for the team about the search",
      "type": "string"
    },
    "version": {
      "description": "The version of the search",
      "type": "string"
    }
  },
  "additionalProperties": false,
  "required": [
    "channel",
    "confidence",
    "creation_date",
    "data_metadata",
    "eli5",
    "how_to_implement",
    "known_false_positives",
    "maintainers",
    "modification_date",
    "original_authors",
    "search",
    "search_description",
    "search_id",
    "search_type",
    "security_domain",
    "scheduling",
    "version"
  ]
}

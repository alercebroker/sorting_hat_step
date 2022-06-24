EXTRA_FIELDS = {
    "type": "map",
    "values": [
      "null",
      "int",
      "float",
      "string",
      "bytes",
      {
        "type": "map", "values": ["string", "float", "null", "int"],
      }
    ],
    "default": {}
}

SCHEMA = {
  "type": "record",
  "doc": "Multi stream alert of any telescope/survey",
  "name": "alerce.alert",
  "fields": [
    {
      "name": "oid",
      "type": "string"
    },
    {
      "name": "tid",
      "type": "string"
    },
    {
      "name": "pid",
      "type": "long"
    },
    {
      "name": "candid",
      "type": ["long", "string"]
    },
    {
      "name": "mjd",
      "type": "double"
    },
    {
      "name": "fid",
      "type": "int"
    },
    {
      "name": "ra",
      "type": "double"
    },
    {
      "name": "dec",
      "type": "double"
    },
    {
      "name": "rb",
      "type": ["null", "float"]
    },
    {
      "name": "rbversion",
      "type": ["null", "string"]
    },
    {
      "name": "mag",
      "type": "float"
    },
    {
      "name": "e_mag",
      "type": "float"
    },
    {
      "name": "rfid",
      "type": ["null", "int"]
    },
    {
      "name": "isdiffpos",
      "type": "int"
    },
    {
      "name": "e_ra",
      "type": "float"
    },
    {
      "name": "e_dec",
      "type": "float"
    },
    {
      "name": "extra_fields",
      "type": EXTRA_FIELDS,
    },
    {
      "name": "aid",
      "type": "string"
    },
    {
      "name": "elasticcPublishTimestamp",
      "type": {"type": "long", "logicalType": "timestamp-millis"},
    },
    {
      "name": "brokerIngestTimestamp",
      "type": {"type": "long", "logicalType": "timestamp-millis"},
    },
  ]
}

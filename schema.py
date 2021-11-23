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
      "type": "long"
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
      "type": ["float", "null"]
    },
    {
      "name": "rbversion",
      "type": "string"
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
      "type": "int"
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
      "type": {
        "type": "map",
        "values": ["null", "int", "float", "string"],
      }
    },
    {
      "name": "aid",
      "type": "long"
    },
  ]
}

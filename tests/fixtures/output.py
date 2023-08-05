"""Expected results constants."""

RIGHT_PARSING = {"host": "hexlet.io",
                 "timeout": 50,
                 "proxy": "123.234.53.22",
                 "follow": False
                 }

RIGHT_SIMPLE = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
'''

RIGHT_STYLISH = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
'''   # noqa: W291

RIGHT_PLAIN = '''Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]
'''

RIGHT_JSON = '''[
  {
    "type": "nested",
    "key": "common",
    "nested": [
      {
        "type": "added",
        "key": "follow",
        "second_value": false
      },
      {
        "type": "unchanged",
        "key": "setting1",
        "first_value": "Value 1"
      },
      {
        "type": "deleted",
        "key": "setting2",
        "first_value": 200
      },
      {
        "type": "changed",
        "key": "setting3",
        "first_value": true,
        "second_value": null
      },
      {
        "type": "added",
        "key": "setting4",
        "second_value": "blah blah"
      },
      {
        "type": "added",
        "key": "setting5",
        "second_value": {
          "key5": "value5"
        }
      },
      {
        "type": "nested",
        "key": "setting6",
        "nested": [
          {
            "type": "nested",
            "key": "doge",
            "nested": [
              {
                "type": "changed",
                "key": "wow",
                "first_value": "",
                "second_value": "so much"
              }
            ]
          },
          {
            "type": "unchanged",
            "key": "key",
            "first_value": "value"
          },
          {
            "type": "added",
            "key": "ops",
            "second_value": "vops"
          }
        ]
      }
    ]
  },
  {
    "type": "nested",
    "key": "group1",
    "nested": [
      {
        "type": "changed",
        "key": "baz",
        "first_value": "bas",
        "second_value": "bars"
      },
      {
        "type": "unchanged",
        "key": "foo",
        "first_value": "bar"
      },
      {
        "type": "changed",
        "key": "nest",
        "first_value": {
          "key": "value"
        },
        "second_value": "str"
      }
    ]
  },
  {
    "type": "deleted",
    "key": "group2",
    "first_value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  {
    "type": "added",
    "key": "group3",
    "second_value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
]'''

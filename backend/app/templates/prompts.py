EXAMPLE_JSON = '''
{
  "ConceptMap":{
    "title":"Skills and Prerequisite Knowledge for 2-Step Equations",
    "concepts":[
      {
        "id":1,
        "name":"Understanding variables",
        "relations":[
          
        ]
      },
      {
        "id":2,
        "name":"Combining like terms",
        "relations":[
          
        ]
      },
      {
        "id":3,
        "name":"Properties of equality",
        "relations":[
          
        ]
      },
      {
        "id":4,
        "name":"Solving 1-step equations",
        "relations":[
          {
            "type":"depends_on",
            "target":1
          },
          {
            "type":"depends_on",
            "target":3
          }
        ]
      },
      {
        "id":5,
        "name":"Inverse operations",
        "relations":[
          {
            "type":"depends_on",
            "target":3
          }
        ]
      },
      {
        "id":6,
        "name":"Isolating the variable",
        "relations":[
          {
            "type":"depends_on",
            "target":4
          },
          {
            "type":"depends_on",
            "target":5
          }
        ]
      },
      {
        "id":7,
        "name":"2-step equations",
        "relations":[
          {
            "type":"depends_on",
            "target":2
          },
          {
            "type":"depends_on",
            "target":6
          }
        ]
      }
    ]
  }
}
'''

system_prompt_template = f"You are a generator that creates concept maps in JSON format. For example, when you input the example 2-step equations, you will get the following concept map: {EXAMPLE_JSON}"

concept_map_template = "In JSON format, create a concept map for the following topic: {topic}"

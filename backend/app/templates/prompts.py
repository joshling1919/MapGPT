EXAMPLE_JSON = '''
{
  "initialNodes": [
    { id: "1", data: { label: "Understanding variables" } },
    { id: "2", data: { label: "Combining like terms" } },
    { id: "3", data: { label: "Properties of equality" } },
    { id: "4", data: { label: "Solving 1-step equations" } },
    { id: "5", data: { label: "Inverse operations" } },
    { id: "6", data: { label: "Isolating the variable" } },
    { id: "7", data: { label: "2-step equations" } },
  ],
  "initialEdges": [
    { id: "4-1", source: "4", target: "1" },
    { id: "4-3", source: "4", target: "3" },
    { id: "5-3", source: "5", target: "3" },
    { id: "6-4", source: "6", target: "4" },
    { id: "6-5", source: "6", target: "5" },
    { id: "7-2", source: "7", target: "2" },
    { id: "7-6", source: "7", target: "6" },
  ];
}
'''

system_prompt_template = f"""You are a generator that creates concept maps graphs. 
For example, when you are given the topic, "2-step equations", you will generate the 
following graph in JavaScript: {EXAMPLE_JSON} in this exact format. You do not need to
generate anything other than the graph's nodes and edges in JSON"""

concept_map_template = "Create a concept map for the following topic: {topic}. DO NOT include anything other than the output JSON in your response. For example, you do not need to provide explanations before or after the JSON."

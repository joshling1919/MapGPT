import dagre from "dagre";
import { useState } from "react";
import ReactFlow, {
  Background,
  Controls,
  Edge,
  Node,
  Position,
} from "reactflow";
import { generateConceptMap } from "../../api/conceptMap";
import { initialEdges, initialNodes } from "../../data";

const dagreGraph = new dagre.graphlib.Graph();
dagreGraph.setDefaultEdgeLabel(() => ({}));

const nodeWidth = 172;
const nodeHeight = 36;

interface LayoutedElements {
  nodes: Node[];
  edges: Edge[];
}

const getLayoutedElements = (
  nodes: Node[],
  edges: Edge[],
  direction: "TB" | "LR" = "TB"
): LayoutedElements => {
  const isHorizontal = direction === "LR";
  dagreGraph.setGraph({ rankdir: direction });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: nodeWidth, height: nodeHeight });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  nodes.forEach((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    node.targetPosition = isHorizontal
      ? ("left" as Position)
      : ("top" as Position);
    node.sourcePosition = isHorizontal
      ? ("right" as Position)
      : ("bottom" as Position);

    node.position = {
      x: nodeWithPosition.x - nodeWidth / 2,
      y: nodeWithPosition.y - nodeHeight / 2,
    };
  });

  return { nodes, edges };
};

const { nodes: layoutedNodes, edges: layoutedEdges } = getLayoutedElements(
  initialNodes as Node[],
  initialEdges
);

const ConceptMap = () => {
  const [nodes, setNodes] = useState<Node[]>([]);
  const [edges, setEdges] = useState<Edge[]>([]);
  const [topic, setTopic] = useState<string>("");

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    generateConceptMap(topic).then((res) => {
      generateConceptMap(topic).then((res) => {
        console.log("res.concept_map", res.concept_map);
        const parsed = JSON.parse(res.concept_map);
        console.log("parsed", parsed);
        if (parsed) {
          const responseNodes = parsed.initialNodes;
          const responseEdges = parsed.initialEdges;

          const { nodes: newLayoutedNodes, edges: newLayoutedEdges } =
            getLayoutedElements(responseNodes, responseEdges);

          setNodes(newLayoutedNodes);
          setEdges(newLayoutedEdges);
        } else {
          console.error("Could not parse nodes and edges from the response.");
        }
      });
    });
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setTopic(e.target.value);
  };

  return (
    <section>
      <form onSubmit={handleSubmit}>
        <input value={topic} onChange={handleInputChange} />
      </form>
      <div className="flow-container">
        <ReactFlow nodes={nodes} edges={edges} fitView>
          <Background />
          <Controls />
        </ReactFlow>
      </div>
    </section>
  );
};

export default ConceptMap;

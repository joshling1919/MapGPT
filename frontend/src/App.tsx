import ReactFlow, { Background, Controls, Node } from "reactflow";
import "reactflow/dist/style.css";
import "./App.css";

const nodes: Node[] = [
  {
    id: "1", // required
    position: { x: 0, y: 0 }, // required
    data: { label: "Node 1" }, // required
  },
];
function App() {
  return (
    <div className="App">
      <div className="flow-container">
        <ReactFlow nodes={nodes}>
          <Background />
          <Controls />
        </ReactFlow>
      </div>
    </div>
  );
}

export default App;

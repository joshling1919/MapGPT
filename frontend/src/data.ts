// export const initialNodes = [
//   { id: "1", data: { label: "Understanding variables" } },
//   { id: "2", data: { label: "Combining like terms" } },
//   { id: "3", data: { label: "Properties of equality" } },
//   { id: "4", data: { label: "Solving 1-step equations" } },
//   { id: "5", data: { label: "Inverse operations" } },
//   { id: "6", data: { label: "Isolating the variable" } },
//   { id: "7", data: { label: "2-step equations" } },
// ];

// export const initialEdges = [
//   { id: "4-1", source: "4", target: "1" },
//   { id: "4-3", source: "4", target: "3" },
//   { id: "5-3", source: "5", target: "3" },
//   { id: "6-4", source: "6", target: "4" },
//   { id: "6-5", source: "6", target: "5" },
//   { id: "7-2", source: "7", target: "2" },
//   { id: "7-6", source: "7", target: "6" },
// ];

export const initialNodes = [
  { id: "1", data: { label: "Measures of Error" } },
  { id: "2", data: { label: "Mean Squared Error" } },
  { id: "3", data: { label: "Actual Values" } },
  { id: "4", data: { label: "Predicted Values" } },
  { id: "5", data: { label: "Squared Residuals" } },
];

export const initialEdges = [
  { id: "2-1", source: "2", target: "1" },
  { id: "2-3", source: "2", target: "3" },
  { id: "2-4", source: "2", target: "4" },
  { id: "5-3", source: "5", target: "3" },
  { id: "5-4", source: "5", target: "4" },
];

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
  { id: "1", data: { label: "Tanjiro Kamado" } },
  { id: "2", data: { label: "Nezuko Kamado" } },
  { id: "3", data: { label: "Zenitsu Agatsuma" } },
  { id: "4", data: { label: "Inosuke Hashibira" } },
  { id: "5", data: { label: "Giyu Tomioka" } },
  { id: "6", data: { label: "Shinobu Kocho" } },
  { id: "7", data: { label: "Kanao Tsuyuri" } },
];

export const initialEdges = [
  { id: "1-2", source: "1", target: "2" }, // Tanjiro is Nezuko's brother
  { id: "1-3", source: "1", target: "3" }, // Tanjiro is friends with Zenitsu
  { id: "1-4", source: "1", target: "4" }, // Tanjiro is friends with Inosuke
  { id: "1-5", source: "1", target: "5" }, // Tanjiro is mentored by Giyu
  { id: "1-6", source: "1", target: "6" }, // Tanjiro is connected to Shinobu
  { id: "2-6", source: "2", target: "6" }, // Nezuko is connected to Shinobu
  { id: "3-4", source: "3", target: "4" }, // Zenitsu is friends with Inosuke
  { id: "5-6", source: "5", target: "6" }, // Giyu is connected to Shinobu
  { id: "6-7", source: "6", target: "7" }, // Shinobu is Kanao's mentor
];

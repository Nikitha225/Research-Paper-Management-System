import Card from "../UI/Card";
import DocumentListLayout from "../UI/DocumenstListLayout";
function DocumentsPage() {
  const DOCUMENTS = [
    {
      id: "641d1308565936c8cbad5ff1",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d130b565936c8cbad5ff3",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d1311565936c8cbad5ff5",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d1313565936c8cbad5ff7",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d131a565936c8cbad5ff9",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d131c565936c8cbad5ffb",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d1322565936c8cbad5ffd",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d1324565936c8cbad5fff",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d132c565936c8cbad6001",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d132e565936c8cbad6003",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d1334565936c8cbad6005",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641d1336565936c8cbad6007",
      fileName: "multi_agent.json",
      title:
        "This paper introduces a multi-agent approach to adjust trafﬁc lights based on trafﬁc situation in order to reduce average delay",
      pages: 7,
    },
    {
      id: "641d15017ee82d7ba212733b",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
    {
      id: "641e0649b391f9ecbfbf8e73",
      fileName: "NetSquid.json",
      title: "NetSquid, a NETwork Simulator for QUantum",
      pages: 15,
    },
  ];

  return (
    <>
      <h1>Documents Page</h1>
      <ul>
        {DOCUMENTS.map((document) => (
          <li key={document.id}>
            <Card>
              {/* <p to={document.id}>{document.title}</p> */}
              <DocumentListLayout
                filename={document.fileName}
                title={document.title}
                pages={document.pages}
              />
            </Card>
          </li>
        ))}
      </ul>
    </>
  );
}

export default DocumentsPage;

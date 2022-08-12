const nodes = document.body;

function enterInput(node) {
  const fields = ["id", "name", "autocomplete"];

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    console.log(field);
    if (node[field]) {
      switch (true) {
        case node[field].includes("first") && node[field].includes("name"):
          node.value = "First";
          break;
        case node[field].includes("email"):
          node.value = "email@gmail.com";
          break;
        case node[field].includes("last") && node[field].includes("name"):
          node.value = "Name";
          break;
        case node[field].includes("full") && node[field].includes("name"):
          node.value = "First Name";
          break;
        case node[field].includes("name") && !node[field].includes("middle"):
          node.value = "First Name";
          break;
        case node[field].includes("country"):
          node.value = "My Country";
          break;
        case node[field].includes("city"):
          node.value = "My City";
          break;
        case node[field].includes("zip") || node[field].includes("postal"):
          node.value = 12345;
          break;
        case node[field].includes("phone") || node[field].includes("tel"):
          node.value = 1234567890;
          break;
        case node[field].includes("address"):
          node.value = "1234 Some House Drive";
          break;
        case node[field].includes("about"):
          node.value = "This is the about me section.";
          break;
        default:
          break;
      }
    }
  }
}

function findFields(node) {
  if (node.hasChildNodes()) {
    node.childNodes.forEach(findFields);
  } else {
    enterInput(node);
  }
}

findFields(nodes);

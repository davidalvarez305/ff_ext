const nodes = document.body;

function matchesField(fieldName, key) {
  return fieldName.toLowerCase().includes(key.toLowerCase());
}

function customFields(node) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    console.log(label);
    switch (true) {
      case matchesField(label, "linkedin profile"):
        node.value = "LinkedIn";
        break;
      case matchesField(label, "github"):
        node.value = "Github";
        break;
      case matchesField(label, "salary") || matchesField(label, "compensation"):
        node.value = "Open";
        break;
      case matchesField(label, "how did you hear about this job"):
        node.value = "LinkedIn";
        break;
      case matchesField(label, "state"):
        node.value = "Florida";
        break;
      case matchesField(label, "gender"):
        node.value = "Male";
        break;
      case matchesField(label, "hispanic"):
        node.value = "Yes";
        break;
      case matchesField(label, "veteran"):
        node.value = "I am not a protected veteran";
        break;
      case matchesField(label, "authorized to work in the united states"):
        node.value = "Yes";
        break;
      default:
        node.value = "";
    }
  }
}

function resolveName(node, field) {
  let name = "";
  let fieldName = "";

  if (!node["labels"]) {
    fieldName = node[field];
  } else {
    fieldName = node["labels"][0].innerText;
  }

  switch (true) {
    case matchesField(fieldName, "first"):
      name = "First Name";
      break;
    case matchesField(fieldName, "last"):
      name = "Last Name";
      break;
    case matchesField(fieldName, "full"):
      name = "Full Name";
      break;
    case matchesField(fieldName, "middle"):
      name = "Middle Name";
      break;
    default:
      name = "Full Name";
  }

  return name;
}

function findSiblings(node) {
  node.nextSibling;
}

function enterInput(node) {
  const fields = ["id", "name", "autocomplete", "className"];

  if (node["nodeName"] === "SELECT") {
    console.log("Select node: ", node);
  }

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "name"):
          node.value = resolveName(node, field);
          break;
        case matchesField(node[field], "email"):
          node.value = "email@gmail.com";
          break;
        case matchesField(node[field], "password"):
          node.value = "password";
          break;
        case matchesField(node[field], "country"):
          node.value = "United States";
          break;
        case matchesField(node[field], "city"):
          node.value = "My City";
          break;
        case matchesField(node[field], "zip") ||
          matchesField(node[field], "postal"):
          node.value = 12345;
          break;
        case matchesField(node[field], "phone") ||
          matchesField(node[field], "tel"):
          node.value = 1234567890;
          break;
        case matchesField(node[field], "address"):
          node.value = "1234 Some House Drive";
          break;
        case matchesField(node[field], "about"):
          node.value = "This is the about me section.";
          break;
        case matchesField(node[field], "linkedin"):
          node.value = "https://www.linkedin.com/";
          break;
        case matchesField(node[field], "additional"):
          node.value = "Additional information field.";
          break;
        default:
          customFields(node);
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

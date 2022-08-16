const nodes = document.body;

function matchesField(fieldName, key) {
  return fieldName.toLowerCase().includes(key.toLowerCase());
}

function resolveName(node, label) {
  switch (true) {
    case matchesField(label, "first"):
      node.value = "First Name";
      break;
    case matchesField(label, "last"):
      node.value = "Last Name";
      break;
    case matchesField(label, "full"):
      node.value = "Full Name";
      break;
    case matchesField(label, "middle"):
      node.value = "Middle Name";
      break;
    default:
      node.value = "Full Name";
  }
}

function resolveCheckbox(node) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;

    switch (true) {
      case matchesField(label, "latino"):
        node.checked = true;
        break;
      case matchesField(label, "male") && !matchesField(label, "female"):
        node.checked = true;
        break;
    }
  }
}

function enterInput(node) {
  if (node["type"] === "checkbox") {
    resolveCheckbox(node);
  }
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    switch (true) {
      case matchesField(label, "name"):
        resolveName(node, label);
        break;
      case matchesField(label, "email"):
        node.value = "email@gmail.com";
        break;
      case matchesField(label, "password"):
        node.value = "password";
        break;
      case matchesField(label, "phone") || matchesField(label, "tel"):
        node.value = 1234567890;
        break;
      case matchesField(label, "contact") && matchesField(label, "type"):
        node.value = "Mobile";
        break;
      case matchesField(label, "address") || matchesField(label, "residence"):
        node.value = "1234 Some House Drive";
        break;
      case matchesField(label, "current location"):
        node.value = "Miami Lakes, FL, USA";
        break;
      case matchesField(label, "country"):
        node.value = "United States";
        break;
      case matchesField(label, "city"):
        node.value = "My City";
        break;
      case matchesField(label, "zip") || matchesField(label, "postal"):
        node.value = 12345;
        break;
      case matchesField(label, "state"):
        node.value = "Florida";
        break;
      case matchesField(label, "location"):
        node.value = "Miami Lakes, FL";
        break;
      case matchesField(label, "linkedin") || matchesField(label, "profile"):
        node.value = "LinkedIn";
        break;
      case matchesField(label, "github") || matchesField(label, "website"):
        node.value = "Github";
        break;
      case matchesField(label, "salary") || matchesField(label, "compensation"):
        node.value = "Open";
        break;
      case matchesField(label, "how did you hear about this job"):
        node.value = "LinkedIn";
        break;
      case matchesField(label, "how did you hear about us"):
        node.value = "Social Network";
        break;
      case matchesField(label, "have you previously worked for") ||
        matchesField(label, "are you currently an employee"):
        node.value = "No";
        break;
      case matchesField(label, "gender"):
        node.value = "Male";
        break;
      case matchesField(label, "hispanic") || matchesField(label, "race"):
        node.value = "Yes";
        break;
      case matchesField(label, "veteran"):
        node.value = "I am not a protected veteran";
        break;
      case matchesField(label, "disability"):
        node.value =
          "No, I don't have a disability, or a history/record of having a disability";
        break;
      case matchesField(label, "authorized to work in the united states"):
        node.value = "Yes";
        break;
      case matchesField(label, "immigration sponsorship for employment visa"):
        node.value = "Yes";
        break;
      case matchesField(label, "legally authorized to work in the country"):
        node.value = "Yes";
        break;
      default:
        node.value = "";
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

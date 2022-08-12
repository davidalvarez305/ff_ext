const nodes = document.body;

function matchesField(fieldName, key) {
  return fieldName.toLowerCase().includes(key);
}

function customFields(node) {
  if (node.id.includes("job_application_answers_attributes_0_text_value")) {
    node.value = "https://linkedin.com/";
  }
  if (node.id.includes("job_application_answers_attributes_1_text_value")) {
    node.value = "https://github.com/";
  }
  if (node.id.includes("job_application_answers_attributes_2_text_value")) {
    node.value = "LinkedIn";
  }
}

function selectFields(node) {
  console.log(node);
  node.value = "Florida Atlantic University";
}

function enterInput(node) {
  const fields = ["id", "name", "autocomplete"];

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "first") &&
          matchesField(node[field], "name"):
          node.value = "First";
          break;
        case matchesField(node[field], "email"):
          node.value = "email@gmail.com";
          break;
        case matchesField(node[field], "password"):
          node.value = "password";
          break;
        case matchesField(node[field], "last") &&
          matchesField(node[field], "name"):
          node.value = "Name";
          break;
        case matchesField(node[field], "full") &&
          matchesField(node[field], "name"):
          node.value = "First Name";
          break;
        case matchesField(node[field], "name") &&
          !matchesField(node[field], "middle"):
          node.value = "First Name";
          break;
        case matchesField(node[field], "country"):
          node.value = "My Country";
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
        case matchesField(node[field], "select2-drop-mask"):
          selectFields(node);
          break;
        default:
          if (field === "id") {
            customFields(node);
          }
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

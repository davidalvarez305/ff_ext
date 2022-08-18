import { User } from "./utils";

function matchesField(fieldName: string, key: string) {
  return fieldName.toLowerCase().includes(key.toLowerCase());
}

function resolveName(node: any, user: User) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    switch (true) {
      case matchesField(label, "first"):
        node.value = user.firstName;
        break;
      case matchesField(label, "last"):
        node.value = user.lastName;
        break;
      case matchesField(label, "full"):
        node.value = user.firstName + user.lastName;
        break;
      case matchesField(label, "middle"):
        node.value = user.middleName;
        break;
      default:
        node.value = user.firstName + user.lastName;
    }
  }
}

function resolveCheckbox(node: any, user: User) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;

    switch (true) {
      case matchesField(label, "latino"):
        node.checked = user.ethnicity === "latino";
        break;
      case matchesField(label, "male") && !matchesField(label, "female"):
        node.checked = user.sex === "male";
        break;
    }
  }
}

function searchByLabel(node: any, user: User) {
  if (node["type"] === "checkbox") {
    resolveCheckbox(node, user);
  }
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    switch (true) {
      case matchesField(label, "name"):
        resolveName(node, user);
        break;
      case matchesField(label, "email"):
        node.value = user.email;
        break;
      case matchesField(label, "password"):
        node.value = user.password;
        break;
      case matchesField(label, "phone") || matchesField(label, "tel"):
        node.value = user.phoneNumber;
        break;
      case matchesField(label, "contact") && matchesField(label, "type"):
        node.value = user.contactType;
        break;
      case matchesField(label, "address") || matchesField(label, "residence"):
        node.value = user.addressLineOne;
        break;
      case matchesField(label, "current location"):
        node.value = `${user.city}, ${user.state}, ${user.country}`;
        break;
      case matchesField(label, "country"):
        node.value = user.country;
        break;
      case matchesField(label, "city"):
        node.value = user.city;
        break;
      case matchesField(label, "zip") || matchesField(label, "postal"):
        node.value = user.zip;
        break;
      case matchesField(label, "state"):
        node.value = user.state;
        break;
      case matchesField(label, "location"):
        node.value = `${user.city}, ${user.state}`;
        break;
      case matchesField(label, "linkedin") || matchesField(label, "profile"):
        node.value = user.linkedin;
        break;
      case matchesField(label, "github") ||
        matchesField(label, "website") ||
        matchesField(label, "portfolio"):
        node.value = user.portfolio;
        break;
      case matchesField(label, "salary") || matchesField(label, "compensation"):
        node.value = user.salary;
        break;
      case matchesField(label, "how did you hear about this job"):
        node.value = user.faqOne ? user.faqOne : "";
        break;
      case matchesField(label, "how did you hear about us"):
        node.value = user.faqOne ? user.faqOne : "";
        break;
      case matchesField(label, "have you previously worked for") ||
        matchesField(label, "are you currently an employee"):
        node.value = user.faqTwo ? user.faqTwo : "";
        break;
      case matchesField(label, "gender"):
        node.value = user.gender;
        break;
      case matchesField(label, "hispanic") || matchesField(label, "race"):
        node.value = user.race;
        break;
      case matchesField(label, "veteran"):
        node.value = user.veteranStatus;
        break;
      case matchesField(label, "disability"):
        node.value = user.disabilityStatus;
        break;
      case matchesField(label, "authorized to work in the united states"):
        node.value = user.faqFour ? user.faqFour : "";
        break;
      case matchesField(label, "immigration sponsorship for employment visa"):
        node.value = user.faqFive ? user.faqFive : "";
        break;
      case matchesField(label, "legally authorized to work in the country"):
        node.value = user.faqFour ? user.faqFour : "";
        break;
      default:
        node.value = "";
    }
  }
}

function enterInput(node: any, user: User) {
  const fields = ["id", "name", "autocomplete", "className"];

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "name"):
          resolveName(node, user);
          break;
        case matchesField(node[field], "email"):
          node.value = user.email;
          break;
        case matchesField(node[field], "password"):
          node.value = user.password;
          break;
        case matchesField(node[field], "country"):
          node.value = user.country;
          break;
        case matchesField(node[field], "city"):
          node.value = user.city;
          break;
        default:
          searchByLabel(node, user);
          break;
      }
    }
  }
}

function findFields(node: any, user: User) {
  if (node.hasChildNodes()) {
    node.childNodes.forEach(findFields);
  } else {
    enterInput(node, user);
  }
}

export function fillFields(user: User) {
  findFields(document.body, user);
}

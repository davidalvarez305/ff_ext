const nodes = document.body;

function matchesField(fieldName, key) {
  return fieldName.toLowerCase().includes(key.toLowerCase());
}

function resolveName(node) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
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

function searchByLabel(node) {
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

function enterInput(node) {
  const fields = ["id", "name", "autocomplete", "className"];

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "name"):
          resolveName(node);
          break;
        case matchesField(node[field], "email"):
          node.value = "email@gmail.com";
          break;
        case matchesField(node[field], "password"):
          node.value = "password";
          break;
        case matchesField(node[field], "country"):
          node.value = "My Country";
          node.value = "United States";
          break;
        case matchesField(node[field], "city"):
          node.value = "My City";
        default:
          searchByLabel(node);
          break;
      }
    }
  }
}

function findFields(node) {
  if (node.hasChildNodes()) {
    node.childNodes.forEach(findFields);
  } else {
    console.log("find fields...");
    enterInput(node);
  }
}

function main() {
  console.log("Starting....");

  let user = {
    NmkQZWeW9_ojadERwK74HXYj43Lw: 0.3039316821878978,
    PZiFauEC6H: 0.04273172815465165,
    "2m7cMrwRPoxpa8LvmpAaJ": 0.7010494474513925,
    D: 0.4552683870622114,
    HQhIxPxO8tsdocRuGJpnhB7k2PjD: 0.18360190519964337,
    rVwM8: 0.8681098855694265,
    "3Vf5HGYDOmUli3": 0.527829742115212,
    fQ4ryGL2cxhJeRd: 0.10353706566292953,
    D_DQqODu_: 0.1272988336424956,
    "8UY0a7": 0.17057184875868092,
    "8i1uVtPwzl0KRA8iYZ4uKcPKF": 0.9554370948377217,
    TTi: 0.038665872114993616,
    YofUj9RrK7foQrl: 0.5835241172217945,
    sb3SzEB_: 0.17136910050721899,
    "801FopHCCML4ozrfmjak": 0.10999126507324442,
    D8: 0.05981337403919851,
    oL8ZZvrAG: 0.36816486041399255,
    hfXxJ0sNp42y2HYEDXLBYgZ6mV: 0.13977757384990708,
    "2xx4AJrQswA5TIcXr": 0.8610074761855161,
    "68RNcKQmgnh_qTG": 0.5234909406332302,
    wJsV8BRo1cT2MtXDuh: 0.4497261910215308,
    "6yFr4E81bvXK": 0.5996413679577888,
    Px2bjBvFSBu: 0.017922504534248707,
    yazK1KQbmUhE4Ul1rZX5hf0yulX_JK: 0.7105144243046027,
    cXmdnvmP: 0.028121925940253756,
    R_fDjw9yBejk3: 0.699514797889162,
    z: 0.34347612922580006,
    "2kTX6Q2tzbCo3": 0.678962211994213,
  };

  browser.storage.local
    .get("user")
    .then((res) => {
      console.log("res: ", res);
    })
    .catch(console.error);
  findFields(nodes);
}

main();

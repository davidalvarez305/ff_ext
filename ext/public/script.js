const entries = [
  {
    input: "email",
    prop: "email",
  },
  {
    input: "password",
    prop: "password",
  },
  {
    input: "phone",
    prop: "phoneNumber",
  },
  {
    input: "tel",
    prop: "phoneNumber",
  },
  {
    input: "contact",
    prop: "contactType",
  },
  {
    input: "type",
    prop: "contactType",
  },
  {
    input: "address",
    prop: "addressLineOne",
  },
  {
    input: "residence",
    prop: "addressLineOne",
  },
  {
    input: "country",
    prop: "country",
  },
  {
    input: "city",
    prop: "city",
  },
  {
    input: "zip",
    prop: "zip",
  },
  {
    input: "postal",
    prop: "zip",
  },
  {
    input: "state",
    prop: "state",
  },
  {
    input: "linkedin",
    prop: "linkedin",
  },
  {
    input: "profile",
    prop: "linkedin",
  },
  {
    input: "github",
    prop: "portfolio",
  },
  {
    input: "website",
    prop: "portfolio",
  },
  {
    input: "portfolio",
    prop: "portfolio",
  },
  {
    input: "salary",
    prop: "salary",
  },
  {
    input: "compensation",
    prop: "salary",
  },
  {
    input: "how did you hear about this job",
    prop: "applicationReferral",
  },
  {
    input: "how did you hear about us",
    prop: "applicationReferral",
  },
  {
    input: "current company",
    prop: "currentCompany",
  },
  {
    input: "current (or most recent) company",
    prop: "currentCompany",
  },
  {
    input: "gender",
    prop: "gender",
  },
  {
    input: "hispanic",
    prop: "isHispanic",
  },
  {
    input: "race",
    prop: "race",
  },
  {
    input: "veteran",
    prop: "veteranStatus",
  },
  {
    input: "disability",
    prop: "disabilityStatus",
  },
  {
    input: "authorized to work in the united states",
    prop: "workAuthorization",
  },
  {
    input: "legally authorized to work in the country",
    prop: "workAuthorization",
  },
  {
    input: "authorized to work",
    prop: "workAuthorization",
  },
  {
    input: "permanent work authorization",
    prop: "workAuthorization",
  },
  {
    input: "immigration sponsorship for employment visa",
    prop: "immigrationSponsorship",
  },
  {
    input: "require visa sponsorship",
    prop: "immigrationSponsorship",
  },
  {
    input: "require sponsorship for employment visa",
    prop: "immigrationSponsorship",
  },
  {
    input: "work visa",
    prop: "immigrationSponsorship",
  },
];

const stateAbbreviations = {
  Alabama: "AL",
  Alaska: "AK",
  Arizona: "AZ",
  Arkansas: "AR",
  California: "CA",
  Colorado: "CO",
  Connecticut: "CT",
  Delaware: "DE",
  "District of Columbia": "DC",
  Florida: "FL",
  Georgia: "GA",
  Hawaii: "HI",
  Idaho: "ID",
  Illinois: "IL",
  Indiana: "IN",
  Iowa: "IA",
  Kansas: "KS",
  Kentucky: "KY",
  Louisiana: "LA",
  Maine: "ME",
  Maryland: "MD",
  Massachusetts: "MA",
  Michigan: "MI",
  Minnesota: "MN",
  Mississippi: "MS",
  Missouri: "MO",
  Montana: "MT",
  Nebraska: "NE",
  Nevada: "NV",
  "New Hampshire": "NH",
  "New Jersey": "NJ",
  "New Mexico": "NM",
  "New York": "NY",
  "North Carolina": "NC",
  "North Dakota": "ND",
  Ohio: "OH",
  Oklahoma: "OK",
  Oregon: "OR",
  Pennsylvania: "PA",
  "Rhode Island": "RI",
  "South Carolina": "SC",
  "South Dakota": "SD",
  Tennessee: "TN",
  Texas: "TX",
  Utah: "UT",
  Vermont: "VT",
  Virginia: "VA",
  Washington: "WA",
  "West Virginia": "WV",
  Wisconsin: "WI",
  Wyoming: "WY",
};

function matchesField(fieldName, key) {
  return String(fieldName).toLowerCase().includes(String(key).toLowerCase());
}

function resolveName(node, user) {
  const fields = ["id", "name", "autocomplete", "className"];

  fields.forEach((field) => {
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "first"):
          node.value = user.firstName;
          break;
        case matchesField(node[field], "last"):
          node.value = user.lastName;
          break;
        case matchesField(node[field], "full"):
          node.value = user.firstName + " " + user.lastName;
          break;
        case matchesField(node[field], "middle"):
          node.value = user.middleName;
          break;
        default:
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
                node.value = user.firstName + " " + user.lastName;
                break;
              case matchesField(label, "middle"):
                node.value = user.middleName;
                break;
              default:
                node.value = user.firstName + " " + user.lastName;
            }
          }
      }
    }
  });
}

function resolveCheckbox(node, user) {
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

function resolveRadioButtons(node, user) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    for (let i = 0; i < entries.length; i++) {
      switch (true) {
        case matchesField(label, "unrestricted right to work"):
          if (node.value === user.workAuthorization) {
            node.checked = true;
          }
          break;
        case matchesField(label, "need sponsorship"):
          if (node.value === user.immigrationSponsorship) {
            node.checked = true;
          }
          break;
        default:
          if (matchesField(node.value, user[entries[i].prop])) {
            node.checked = true;
          }
      }
    }
  }
}

function searchByLabel(node, user) {
  if (node["type"] === "checkbox") {
    resolveCheckbox(node, user);
  }
  if (node["type"] === "radio") {
    resolveRadioButtons(node, user);
  }
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    for (let i = 0; i < entries.length; i++) {
      switch (true) {
        case matchesField(label, "name"):
          resolveName(node, user);
          break;
        case matchesField(label, "current location"):
          node.value = `${user.city}, ${user.state}, ${user.country}`;
          break;
        case matchesField(label, "location"):
          node.value = `${user.city}, ${user.state}`;
          break;
        case matchesField(label, "state"):
          node.value = user.state;
          if (node.value === "") {
            node.value = stateAbbreviations[user.state];
          }
          break;
        case matchesField(label, entries[i].input):
          node.value = user[entries[i].prop];
          break;
      }
    }
  }
}

function enterInput(node, user) {
  const fields = ["id", "name", "autocomplete", "className"];

  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      for (let n = 0; n < entries.length; n++) {
        switch (true) {
          case matchesField(node[field], "name"):
            resolveName(node, user);
            break;
          case matchesField(node[field], "location"):
            node.value = `${user.city}, ${user.state}`;
            break;
          case matchesField(node[field], entries[n].input):
            node.value = user[entries[n].prop];
            break;
        }
      }
    }
  }
  searchByLabel(node, user);
}

function findFields(node, user) {
  if (node.hasChildNodes()) {
    node.childNodes.forEach((n) => {
      findFields(n, user);
    });
  } else {
    enterInput(node, user);
  }
}

browser.storage.local
  .get("user")
  .then((data) => {
    if (data.user) {
      findFields(document.body, data.user);
    }
  })
  .catch((err) => {
    console.error(err);
  });

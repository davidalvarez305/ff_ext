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

const fields = ["id", "name", "className"];

let results = [];

function getField(node, val) {
  let data = {};
  fields.some((field) => {
    const check = node.hasAttribute(field);
    if (check) {
      data["field"] = field;
      data["name"] = node[field];
      data["data"] = val;
    }
    return check;
  });
  return data;
}

function matchesField(fieldName, key) {
  return String(fieldName).toLowerCase().includes(String(key).toLowerCase());
}

function resolveName(node, user) {
  let data = {};
  fields.some((field) => {
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "first"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.firstName;
          results.push(data);
          break;
        case matchesField(node[field], "last"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.lastName;
          results.push(data);
          break;
        case matchesField(node[field], "full"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.firstName + " " + user.lastName;
          results.push(data);
          break;
        case matchesField(node[field], "middle"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.middleName;
          results.push(data);
          break;
        default:
          if (node["labels"] && node["labels"][0]) {
            const label = node["labels"][0].innerText;
            switch (true) {
              case matchesField(label, "first"):
                data = getField(node, user.firstName);
                results.push(data);
                break;
              case matchesField(label, "last"):
                data = getField(node, user.lastName);
                results.push(data);
                break;
              case matchesField(label, "full"):
                data = getField(node, user.firstName + " " + user.lastName);
                results.push(data);
                break;
              case matchesField(label, "middle"):
                data = getField(node, user.middleName);
                results.push(data);
                break;
              default:
                data = getField(node, user.firstName + " " + user.lastName);
                results.push(data);
                break;
            }
          }
      }
    }
    return data.hasOwnProperty("data");
  });
}

function resolveCheckbox(node, user) {
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    let data = {};
    switch (true) {
      case matchesField(label, "latino"):
        data = getField(node, true);
        results.push(data);
        break;
      case matchesField(label, "male") && !matchesField(label, "female"):
        data = getField(node, true);
        results.push(data);
        break;
    }
  }
}

function resolveRadioButtons(node, user) {
  let data = {};
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    entries.some((entry) => {
      switch (true) {
        case matchesField(label, "unrestricted right to work"):
          data = getField(node, true);
          results.push(data);
          break;
        case matchesField(label, "need sponsorship"):
          data = getField(node, true);
          results.push(data);
          break;
        default:
          data = getField(node, true);
          results.push(data);
          break;
      }
      return data.hasOwnProperty("data");
    });
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
    let data = {};
    entries.some((entry) => {
      switch (true) {
        case matchesField(label, "name"):
          resolveName(node, user);
          break;
        case matchesField(label, "current location"):
          data = getField(node, `${user.city}, ${user.state}, ${user.country}`);
          results.push(data);
          break;
        case matchesField(label, "location"):
          data = getField(node, `${user.city}, ${user.state}`);
          results.push(data);
          break;
        case matchesField(label, "state"):
          data = getField(node, stateAbbreviations[user.state]);
          results.push(data);
          break;
        case matchesField(label, entry.input):
          data = getField(node, user[entry.prop]);
          results.push(data);
          break;
      }
      return data.hasOwnProperty("data");
    });
  }
}

function enterInput(node, user) {
  let data = {};
  fields.some((field) => {
    if (node[field]) {
      for (let n = 0; n < entries.length; n++) {
        switch (true) {
          case matchesField(node[field], "name"):
            resolveName(node, user);
            break;
          case matchesField(node[field], "location"):
            data = getField(node, `${user.city}, ${user.state}`);
            results.push(data);
            break;
          case matchesField(node[field], entries[n].input):
            data = getField(node, user[entries[n].prop]);
            results.push(data);
            break;
        }
      }
      return data.hasOwnProperty("data");
    }
  });
  if (!data.hasOwnProperty("data")) {
    searchByLabel(node, user);
  }
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
      if (results.length > 0) {
        fetch("http://localhost:5000/", {
          method: "POST",
          body: JSON.stringify({ data: results }),
        })
          .then(async (data) => {
            const response = await data.json();
            alert(response.data);
          })
          .catch((err) => {
            console.log(err);
            alert(err);
          });
      }
    }
  })
  .catch((err) => {
    console.error(err);
  });

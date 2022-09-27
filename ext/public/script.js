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
  {
    input: "area of interest",
    prop: "areaOfInterest",
  },
  {
    input: "Security Clearance",
    prop: "securityClearance",
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

const fields = ["id", "name", "className", "autocomplete"];

let results = [];

function getField(node, val) {
  let data = {};
  fields.some((field) => {
    const check = node.hasAttribute(field);
    if (check) {
      data["field"] = field;
      data["name"] = node[field];
      data["data"] = val;
      data["type"] = node["nodeName"];
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
  for (let i = 0; i < fields.length; i++) {
    const field = fields[i];
    if (node[field]) {
      switch (true) {
        case matchesField(node[field], "first"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.firstName;
          data["type"] = node["nodeName"];
          break;
        case matchesField(node[field], "last"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.lastName;
          data["type"] = node["nodeName"];
          break;
        case matchesField(node[field], "full"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.firstName + " " + user.lastName;
          data["type"] = node["nodeName"];
          break;
        case matchesField(node[field], "middle"):
          data["field"] = field;
          data["name"] = node[field];
          data["data"] = user.middleName;
          data["type"] = node["nodeName"];
          break;
        default:
          if (node["labels"] && node["labels"][0]) {
            const label = node["labels"][0].innerText;
            switch (true) {
              case matchesField(label, "email") ||
                matchesField(label, "e-mail"):
                data = getField(node, user.email);
                break;
              case matchesField(label, "first"):
                data = getField(node, user.firstName);
                break;
              case matchesField(label, "last"):
                data = getField(node, user.lastName);
                break;
              case matchesField(label, "full"):
                data = getField(node, user.firstName + " " + user.lastName);
                break;
              case matchesField(label, "middle"):
                data = getField(node, user.middleName);
                break;
              default:
                break;
            }
          }
      }
      if (data.hasOwnProperty("data")) {
        break;
      }
    }
  }
  return data;
}

function resolveCheckbox(node, user) {
  let data = {};
  if (node["labels"] && node["labels"][0]) {
    const label = node["labels"][0].innerText;
    switch (true) {
      case matchesField(label, "latino"):
        data = getField(node, true);
        break;
      case matchesField(label, "male") && !matchesField(label, "female"):
        data = getField(node, true);
        break;
    }
  }
  return data;
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
  return data;
}

function resolveField(node, user) {
  let data = {};
  fields.some((field) => {
    if (node[field]) {
      for (let n = 0; n < entries.length; n++) {
        if (matchesField(node[field], "name")) {
          data = resolveName(node, user);
          break;
        }
        if (matchesField(node[field], "location")) {
          data = getField(node, `${user.city}, ${user.state}`);
          break;
        }
        if (matchesField(node[field], entries[n].input)) {
          data = getField(node, user[entries[n].prop]);
          break;
        }
      }
      return data.hasOwnProperty("data");
    }
  });
  return data;
}

function isEmpty(obj) {
  return Object.keys(obj).length === 0;
}

function findFields(nodes, user) {
  nodes.forEach((node) => {
    let data = {};

    if (node.type === "file") {
      data = getField(node, "resume");
    } else if (node.type === "button") {
      if (node.outerHTML.includes("resume")) {
        data = getField(node, "resume");
      } else if (node.outerHTML.includes("cover")) {
        data = getField(node, "cover");
      } else {
        data = getField(node, "resume");
      }
    } else if (node["type"] === "checkbox") {
      data = resolveCheckbox(node, user);
    } else if (node["type"] === "radio") {
      data = resolveRadioButtons(node, user);
    } else {
      data = resolveField(node, user);
    }

    if (!isEmpty(data)) {
      results.push(data);
    }
  });
}

browser.storage.local
  .get("user")
  .then((data) => {
    if (data.user) {
      let nodes = [];
      ["select", "input", "checkbox", "radio", "button"].forEach((nodeType) => {
        const nodeList = document.querySelectorAll(nodeType);
        nodes = [...nodes, ...nodeList];
      });
      findFields(nodes, data.user);
      if (results.length > 2) {
        console.log(results);
        fetch("http://localhost:5000/", {
          method: "POST",
          body: JSON.stringify({
            data: {
              url: window.location.href,
              results: results,
              user: data.user,
            },
          }),
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

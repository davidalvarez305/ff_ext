export const fields = [
  {
    label: "First Name",
    name: "firstName",
  },
  {
    label: "Last Name",
    name: "lastName",
  },
  {
    label: "Email",
    name: "email",
    type: "email",
  },
  {
    label: "Phone Number",
    name: "phoneNumber",
    type: "tel",
  },
  {
    label: "Middle Name",
    name: "middleName",
  },
  {
    label: "Race",
    name: "race",
  },
  {
    label: "Gender",
    name: "gender",
  },
  {
    label: "Preferred Contact Type",
    name: "preferredContactType",
  },
  {
    label: "Password",
    name: "password",
    type: "password",
  },
  {
    label: "Address Line 1",
    name: "addressLineOne",
  },
  {
    label: "Address Line 2",
    name: "addressLineTwo",
  },
  {
    label: "City",
    name: "city",
  },
  {
    label: "State",
    name: "state",
  },
  {
    label: "Country",
    name: "country",
  },
  {
    label: "Zip",
    name: "zip",
    type: "number",
  },
  {
    label: "LinkedIn",
    name: "linkedin",
  },
  {
    label: "Facebook",
    name: "facebook",
  },
  {
    label: "Twitter",
    name: "twitter",
  },
  {
    label: "Portfolio",
    name: "portfolio",
  },
  {
    label: "Website",
    name: "website",
  },
  {
    label: "Salary",
    name: "salary",
  },
  {
    label: "How did you hear about us?",
    name: "applicationReferral",
  },
  {
    label: "Current Company",
    name: "currentCompany",
  },
  {
    label: "Do you have a disability?",
    name: "disabilityStatus",
  },
  {
    label: "What's your veteran status?",
    name: "veteranStatus",
  },
  {
    label: "Are you authorized to work in the United States?",
    name: "workAuthorization",
  },
  {
    label: "Will you need immigration sponsorship for employment visa?",
    name: "immigrationSponsorship",
  },
];

export type User = {
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: number;
  middleName: string;
  isHispanic: string;
  password: string;
  contactType: string;
  addressLineOne: string;
  addressLineTwo: string;
  city: string;
  state: string;
  country: string;
  zip: number;
  linkedin: string;
  facebook: string;
  twitter: string;
  portfolio: string;
  website: string;
  salary: string;
  applicationReferral: string;
  currentCompany: string;
  workAuthorization: string;
  immigrationSponsorship: string;
  gender: string;
  race: string;
  veteranStatus: string;
  disabilityStatus: string;
};

export const emptyUser = {
  firstName: "",
  lastName: "",
  email: "",
  phoneNumber: 0,
  middleName: "",
  isHispanic: "",
  race: "",
  gender: "",
  password: "",
  contactType: "",
  addressLineOne: "",
  addressLineTwo: "",
  city: "",
  state: "",
  country: "",
  zip: 0,
  linkedin: "",
  facebook: "",
  twitter: "",
  portfolio: "",
  website: "",
  salary: "",
  applicationReferral: "",
  currentCompany: "",
  workAuthorization: "",
  immigrationSponsorship: "",
  veteranStatus: "",
  disabilityStatus: "",
};

export const capitalizeFirstLetter = (str: string) => {
  return str.charAt(0).toUpperCase() + str.slice(1);
};

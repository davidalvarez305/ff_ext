import React from "react";
import { Form, Formik } from "formik";
import { SimpleInputField } from "./SimpleInputField";
import { COUNTRY_LIST, fields, STATE_ABBREVIATIONS, User } from "./utils";
import { Button, Flex } from "@chakra-ui/react";
import SelectComponent from "./SelectComponent";

interface Props {
  user: User;
  setShowSetup: (value: React.SetStateAction<boolean>) => void;
}

export const Setup: React.FC<Props> = ({ user, setShowSetup }) => {
  function handleSubmit(user: User) {
    user.isHispanic = user.race === "Hispanic or Latino" ? "Yes" : "No";
    user.fullName = user.firstName + " " + user.lastName;
    browser.storage.local.set({
      user,
    });
    setShowSetup(false);
  }

  return (
    <Formik initialValues={user} onSubmit={handleSubmit}>
      <Form>
        <Flex
          justify={"center"}
          align={"center"}
          direction={"column"}
          textAlign={"left"}
          gap={1}
        >
          {fields.map((field) => {
            switch (field.name) {
              case "race":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "Hispanic or Latino",
                      "White (Not Hispanic or Latino)",
                      "Black or African America (Not Hispanic or Latino)",
                      "Native Hawaiian or Other Pacific Islander (Not Hispanic or Latino)",
                      "Asian (Not Hispanic or Latino)",
                      "American Indian or Alaska Native (Not Hispanic or Latino)",
                      "Two or More Races (Not Hispanic or Latino)",
                    ]}
                    {...field}
                  />
                );
              case "areaOfInterest":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "Cloud",
                      "Consulting",
                      "Data Analytics",
                      "Design & UX",
                      "Enterprise Operations",
                      "Infrastructure & Technology",
                      "Project Management",
                      "Research",
                      "Sales",
                      "Security",
                      "Software Engineering",
                    ]}
                    {...field}
                  />
                );
              case "securityClearance":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No"]}
                    {...field}
                  />
                );
              case "workAuthorization" || "immigrationSponsorship":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No"]}
                    {...field}
                  />
                );
              case "state":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={Object.keys(STATE_ABBREVIATIONS)}
                    {...field}
                  />
                );
              case "country":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={COUNTRY_LIST}
                    {...field}
                  />
                );
              case "veteranStatus":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "I identify as one or more of the classifications of a protected veteran",
                      "I am not a protected veteran",
                      "I don't wish to answer",
                    ]}
                    {...field}
                  />
                );
              case "disabilityStatus":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No", "I don't wish to answer"]}
                    {...field}
                  />
                );
              case "gender":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Male", "Female", "Decline To Self Identify"]}
                    {...field}
                  />
                );
              case "degree":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "High School Diploma",
                      "Associate's Degree",
                      "Bachelor's Degree",
                      "Master's Degree",
                      "Master of Business Administration (M.B.A)",
                      "Juris Doctor (J.D.)",
                      "Doctor of Medicine (M.D.)",
                      "Doctor of Philosophy (Ph.D.)",
                      "Engineer's Degree",
                      "Other",
                    ]}
                    {...field}
                  />
                );
              case "relocationWillingness":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No"]}
                    {...field}
                  />
                );
              case "isReferral":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No"]}
                    {...field}
                  />
                );
              default:
                return <SimpleInputField {...field} />;
            }
          })}
          <Button
            sx={{ my: 1 }}
            variant={"outline"}
            type={"submit"}
            colorScheme={"green"}
          >
            Save
          </Button>
        </Flex>
      </Form>
    </Formik>
  );
};

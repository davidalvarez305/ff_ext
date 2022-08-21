import React from "react";
import { Form, Formik } from "formik";
import { SimpleInputField } from "./SimpleInputField";
import { fields, User } from "./utils";
import { Button, Flex } from "@chakra-ui/react";
import SelectComponent from "./SelectComponent";

interface Props {
  user: User;
}

export const Setup: React.FC<Props> = ({ user }) => {
  function handleSubmit(user: User) {
    browser.storage.local.set({
      user,
    });
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
              case "workAuthorization":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No"]}
                    {...field}
                  />
                );
              case "isHispanic":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={["Yes", "No", "Decline To Self Identify"]}
                    {...field}
                  />
                );
              case "veteranStatus":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "I am not a protected veteran",
                      "I identify as one or more of the classifications of a protected veteran",
                      "I don't wish to answer",
                    ]}
                    {...field}
                  />
                );
              case "disabilityStatus":
                return (
                  <SelectComponent
                    defaultValue={user[field.name]}
                    options={[
                      "Yes, I have a disability, or have a history/record of having a disability",
                      "No, I don't have a disability, or a history/record of having a disability",
                      "I don't wish to answer",
                    ]}
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

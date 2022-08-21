import React from "react";
import { Form, Formik } from "formik";
import { SimpleInputField } from "./SimpleInputField";
import { fields, User } from "./utils";
import { Button, Flex } from "@chakra-ui/react";
import SelectComponent from "./SelectField";

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
                return <SelectComponent options={["yes", "no"]} {...field} />;
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

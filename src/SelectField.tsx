import {
  FormControl,
  FormLabel,
  Box,
  FormErrorMessage,
} from "@chakra-ui/react";
import { useState } from "react";
import CreatableSelect from "react-select/creatable";
import { capitalizeFirstLetter } from "./utils";
import { useField, useFormikContext } from "formik";

type SelectType = { value: string; label: string };

interface Props {
  options: Array<any>;
  name: string;
  label: string;
}

const SelectComponent: React.FC<Props> = ({ options, name, label }) => {
  const { setFieldValue } = useFormikContext();

  const [field, meta] = useField(name);

  const [selectedValue, setSelectedValue] = useState<null | SelectType>({
    value: "",
    label: "",
  });

  return (
    <Box
      sx={{
        ml: 2,
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        width: 250,
      }}
    >
      <FormControl>
        <FormLabel
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
          }}
          htmlFor={field.name}
        >
          {label}
        </FormLabel>
        <CreatableSelect
          name={field.name}
          placeholder={""}
          value={selectedValue}
          onChange={(e) => {
            setSelectedValue(e);
            setFieldValue(field.name, e?.value);
          }}
          options={options.map((op) => {
            return {
              value: op,
              label: capitalizeFirstLetter(op),
            };
          })}
        />
        {meta.error && meta.touched && (
          <FormErrorMessage>{meta.error}</FormErrorMessage>
        )}
      </FormControl>
    </Box>
  );
};

export default SelectComponent;

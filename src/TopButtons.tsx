import { Box, Button } from "@chakra-ui/react";
import React from "react";

interface Props {
  rightButtonClick: () => void;
  leftButtonClick: () => void;
}

export const TopButtons: React.FC<Props> = ({
  rightButtonClick,
  leftButtonClick,
}) => {
  return (
    <Box
      sx={{
        display: "flex",
        justifyContent: "center",
        alignItems: "top",
        width: "100%",
        gap: 5,
        my: 2,
      }}
    >
      <Button
        variant={"outline"}
        colorScheme={"blue"}
        width={75}
        onClick={leftButtonClick}
      >
        Fill
      </Button>
      <Button
        variant={"outline"}
        colorScheme={"blue"}
        width={75}
        onClick={rightButtonClick}
      >
        Setup
      </Button>
    </Box>
  );
};

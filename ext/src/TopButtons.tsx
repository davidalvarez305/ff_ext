import { Box, Button } from "@chakra-ui/react";
import React from "react";

interface Props {
  rightButtonClick?: () => void;
  leftButtonClick?: () => void;
  leftButton?: string;
  rightButton?: string;
}

export const TopButtons: React.FC<Props> = ({
  rightButtonClick,
  leftButtonClick,
  leftButton,
  rightButton,
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
      {leftButtonClick && leftButton && (
        <Button
          variant={"outline"}
          colorScheme={"green"}
          width={75}
          onClick={leftButtonClick}
        >
          {leftButton}
        </Button>
      )}
      {rightButton && rightButtonClick && (
        <Button
          variant={"outline"}
          colorScheme={"red"}
          width={75}
          onClick={rightButtonClick}
        >
          {rightButton}
        </Button>
      )}
    </Box>
  );
};

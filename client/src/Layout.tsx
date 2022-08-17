import { Box, ChakraProvider, theme } from "@chakra-ui/react";
import React from "react";

interface Props {
  children: React.ReactNode;
}

export const Layout: React.FC<Props> = ({ children }) => {
  return (
    <ChakraProvider theme={theme}>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          height: "50vh",
          width: "25vw",
          borderWidth: 3,
          borderRadius: 25,
        }}
      >
        {children}
      </Box>
    </ChakraProvider>
  );
};

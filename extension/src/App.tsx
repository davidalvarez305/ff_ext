import { Box } from "@chakra-ui/react";
import { useEffect, useState } from "react";
import { fillFields } from "./fillFields";
import { Layout } from "./Layout";
import { Setup } from "./Setup";
import { TopButtons } from "./TopButtons";
import { emptyUser, User } from "./utils";

export const App = () => {
  const [showSetup, setShowSetup] = useState(false);
  const [user, setUser] = useState<User>(emptyUser);

  useEffect(() => {
    browser.storage.local
      .get("user")
      .then((data: { user?: User }) => {
        if (data.user) {
          setUser(data.user);
        }
      })
      .catch((err: Error) => {
        console.error(err);
      });
  }, []);

  const styles = {
    margin: 2,
  };

  if (showSetup) {
    return (
      <Layout>
        <Box sx={styles}>
          <TopButtons
            leftButtonClick={() => fillFields(user)}
            rightButtonClick={() => setShowSetup((prev) => !prev)}
          />
          <Box sx={{ overflow: "scroll", height: "100vh" }}>
            <Setup user={user} />
          </Box>
        </Box>
      </Layout>
    );
  }

  return (
    <Layout>
      <TopButtons
        leftButtonClick={() => fillFields(user)}
        rightButtonClick={() => setShowSetup((prev) => !prev)}
      />
      <Box sx={{ height: "100vh" }}>Yo</Box>
    </Layout>
  );
};

import { Box, Button } from "@chakra-ui/react";
import { Form, Formik } from "formik";
import { useEffect, useState } from "react";
import { Layout } from "./Layout";
import { Setup } from "./Setup";
import { SimpleInputField } from "./SimpleInputField";
import { TopButtons } from "./TopButtons";
import { emptyUser, User } from "./utils";

export const App = () => {
  const [showSetup, setShowSetup] = useState(false);
  const [user, setUser] = useState<User>(emptyUser);

  function handleRequest() {
    browser.storage.local.get("user").then((data: { user?: User }) => {
      if (data.user) {
        fetch("http://localhost:5000/", {
          method: "POST",
          body: JSON.stringify({
            data: {
              url: window.location.href,
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
    });
  }

  function handleLinkedIn(values: { keywords: "" }) {
    browser.storage.local.get("user").then((data: { user?: User }) => {
      if (data.user) {
        fetch("http://localhost:5000/", {
          method: "POST",
          body: JSON.stringify({
            data: {
              url: "https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin",
              user: data.user,
              keywords: values.keywords,
            },
          }),
        })
          .then(async (data) => {
            const response = await data.json();
            alert(response.data);
          })
          .catch((err) => {
            alert(err);
          });
      }
    });
  }

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
            rightButtonClick={() => setShowSetup((prev) => !prev)}
            rightButton={"Home"}
          />
          <Box sx={{ overflow: "scroll", height: "100vh" }}>
            <Setup user={user} setShowSetup={setShowSetup} />
          </Box>
        </Box>
      </Layout>
    );
  }

  return (
    <Layout>
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          height: "100vh",
          width: "100%",
        }}
      >
        <TopButtons
          rightButton={"Setup"}
          leftButton={"Request"}
          leftButtonClick={() => handleRequest()}
          rightButtonClick={() => setShowSetup((prev) => !prev)}
        />
        <Box sx={{ my: 20 }}>
          <Formik initialValues={{ keywords: "" }} onSubmit={handleLinkedIn}>
            <Form>
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  flexDirection: "column",
                  gap: 5,
                }}
              >
                <SimpleInputField
                  name={"keywords"}
                  label={"Linkedin Job Search"}
                />
                ;
                <Button
                  variant={"outline"}
                  colorScheme={"blue"}
                  type={"submit"}
                  width={75}
                />
              </Box>
            </Form>
          </Formik>
        </Box>
      </Box>
    </Layout>
  );
};

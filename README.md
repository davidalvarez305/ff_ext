In order to reproduce this application, follow these steps:

Step #1: Download the source code.

```
git clone https://github.com/davidalvarez305/ff_ext
```

Step #2: Download dependencies.

```
cd ff_ext && yarn
```

Step #3: Build the application.

```
yarn start
```

Step #4: Upload "dist" folder to firefox in debug mode.

```
about:debugging#/runtime/this-firefox
```

```
Step #1: Click on "Load Temporary Add-on"

Step #2: Navigate to "dist" folder & click Open.
```

Step #5: Use.

```
Step #1: Click on "Setup" and enter your information. This is saved in your browser, there are no requests made to any server to save your information.

Step #2: Navigate to any website that requires form input.

Step #3: Click "Fill".
```

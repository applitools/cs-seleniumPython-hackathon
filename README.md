# applitools-seleniumPython-hackathon

## Pre-Requisites
1.  Install Python [here](https://www.python.org/downloads/)
2.  Install ChromeDriver from [here](https://chromedriver.chromium.org/downloads) if you are running on mac, you can also install it using the brew, simply run `brew install chromedriver`
3.  Register to Applitools and [create an account](https://auth.applitools.com/users/register)
4.  Ensure you have your Applitools API Key!

## Hackathon Overview
Imagine you wrote tests for the [1st Version of the App (V1)](https://demo.applitools.com/hackathon.html)

Then [Next Version (V2)](https://demo.applitools.com/hackathonV2.html) came along later and has changes. (including bugs) Some of these bugs are functional bugs and some of are visual bugs. 

**The Challenge**

Write an automated test for both versions which leverages Applitools. Run both a traditional test (provided) and the new test you wrote. Compare the results.

**Instructions**

1.  Review Traditional Script (provided) TraditionalSuite has been provided to you, as we assume you have already written these scripts before. Analyze them, make sure they are ok, and feel free to add any additional coverage/lines of code you see fit.
2.  Run the test suite against both Version 1 and Version 2. You are going to find a lot of failures in Version 2. (changes have been made, including bugs)
3.  Review the scripts again, and review how many assertions and locators required to cover all the elements in the page.
4.  Open the VisualAISuiteSolution and set your ApiKey in string 'eyes.api_key = "api_key"' (or comment the string and set APPLITOOLS_API_KEY environment variable), or write to the terminal: `export APPLIOOLS_API_KEY=<APPLITOOLS_API_KEY>`
5.  Modified the different tests in VisualAISuite to include visual assertion to achieve the same coverage as with the TraditionalSuite.
6.  Run the same test again and see all the differences between the screenshots of the 1st version and the 2nd version of the app.

Note: When you run the tests against V2, you’ll see differences in screenshots because the app is actually different. You should see exactly what those differences are (highlighted in pink) in Applitools dashboard.

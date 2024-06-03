# Subscribe News Letter
  Build on Playwright + pytest

## Instructions
1. Install python based on the OS [link](https://www.python.org/downloads/)

2. Activate the virtual environment `venv\Scripts\Activate.ps1` by running the command in windows

3. Install all dependencies `pip3 install -r requirements.txt`

4. Add the website address in the file `files\data.csv`

5. Install the browser dependencies `playwright install-deps chromium` and `playwright install`

6. Execute this command in cmd for browser headless mode `pytest -v -s --browser-channel chromium` and if you want to see the live execution `pytest -v -s --browser-channel chromium --headed`

7. If you like to execute scritps in parallel  add the number of process `pytest -v -s --browser-channel chromium --numprocesses 4`



## Input parameters
1. In the root of this project the `.env` of below details
    ```
    input_filename=data.csv
    output_filename=output.csv
    email_Address=test123@gmail.com
    ```


2. Update the input files in the folder `files` section
3. You can find the test's results in files folder
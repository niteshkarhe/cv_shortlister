# speech_to_text
This is a python flask API project

# Pre-requisite
1. Install Python 3.11.4
2. Open CMD and run command `python --version`. It should be 3.11.4 
3. If it is not 3.11.4 then add below path to User Environment variable
   C:\Users\nites\AppData\Local\Programs\Python\Python311\Scripts\
   C:\Users\nites\AppData\Local\Programs\Python\Python311
   **Note**: Above paths may change based on your system
4. Make sure you have node.js installed, if not then install it and run command in another CMD: `npm install @openapitools/openapi-generator-cli -g` 
5. clone repository

# Step to run project
1. After cloning the project, run command in CMD inside speech_to_text project folder:  `pip install virtualenv`
2. Run command `python -m virtualenv -python python311 env`. This will create **env** folder inside **speech_to_text** folder
3. Go to folder: env\Scripts and run command in CMD at this location: `activate`. You should see **(env)** written in the CMD at the start of the path. This has activated the virtual environment
4. Be in the same CMD and go back to the folder speech_to_text and run command - `pip install -r requirements.txt`
5. Now from the same CMD, run below command by changing your project location:
   openapi-generator-cli generate -t E:\NK\PythonProject\speech_to_text\codegen\template -i E:\NK\PythonProject\speech_to_text\src\codegen_server\openapi_server\openapi\openapi.yaml -g python-flask -o E:\NK\PythonProject\speech_to_text\src\codegen_server --generate-alias-as-model

   **Note**: Please note that the project location till speech_to_text folder needs to change based on your system
6. Change the content of speech_to_text/src/codegen_server/openapi_server/__main__.py:

#!/usr/bin/env python3<br/>
import os<br/>
from openapi_server.run import application<br/>

def main():<br/>
   port = os.getenv("PORT") or 5000<br/>
   application.run(port=port)<br/>

if __name__ == '__main__':<br/>
   main()<br/>

   **Note**: If you see "br", then remove those from the python code

7. Run command from same CMD when **(env)** is present at the project path: `SET PYTHONPATH=E:\NK\PythonProject\speech_to_text\src\codegen_server`
   **Note**: Please note that the relevant project path may change according to your system
8. From the same CMD, go to the path: speech_to_text/src/codegen_server/openapi_server and run command: `python __main__.py`

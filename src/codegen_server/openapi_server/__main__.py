#!/usr/bin/env python3
import os
from openapi_server.run import application

def main():
    port = os.getenv("PORT") or 8080
    application.run(port=port)

if __name__ == '__main__':
    main()
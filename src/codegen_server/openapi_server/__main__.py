#!/usr/bin/env python3

import os

from openapi_server.run import application

def main():
    port = os.getenv("PORT") or 5000
    application.run(port=port, debug=True)

if __name__ == '__main__':
    main()
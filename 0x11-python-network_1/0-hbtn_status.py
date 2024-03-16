#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import urlib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as re:
        content = re.read()
        print("Body response : ")
        print(f"\t- type : {type(content)}")
        print(f"\t- content: {content}")
        print(f"\t- utf8 content : {content.decode('utf-8')}")

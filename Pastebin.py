import socket 
import requests
import base64
    

def main():

    nama_host = socket.gethostname()
    host64 = nama_host.encode('utf-8')
    encode64 = base64.b64encode(host64)
    url = "http://pastebin.com/api/api_post.php"
    upload = requests.post(url, encode64)
    print(f"Host name is : {nama_host}")


if __name__ == "__main__":
    main()
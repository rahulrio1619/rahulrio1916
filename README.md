# EX01 Developing a Simple Webserver
## Date:24/07/2024

## AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Serving the HTML pages.

### Step 5:
Testing the webserver.

## PROGRAM:
from http.server import HTTPServer,BaseHTTPRequestHandler

content='''<html>
<head>
<title> My Web Server</title>
</head>
<body>
    <center><table border="10" cellpadding="30">
        <caption><h3>MY SYSTEM CONFIGURATION</caption></h3>
        <tr bgcolor="yellow" style="color:black;">
          <th bgcolor="antiquewhite">S.no</th><th>Item</th><th>value</th>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
          <th bgcolor="yellow" style="color:black;"> 1</td><th>OS Name</th><th>Microsoft Windows 10 Pro</th>
        </tr>
        <tr bgcolor="antiquewhite" style="color:black;">
            <th bgcolor="yellow" style="color:black;">2</th><th>system manufacturer</th><th>HP</th>
          </tr>
          <tr bgcolor="antiquewhite" style="color:black;">
            <th bgcolor="yellow" style="color:black;">3</th><th>system model</th><th>elite book 840 g3</th>
          </tr>
          <tr bgcolor="antiquewhite" style="color:black;">
            <th bgcolor="yellow" style="color:black;">4</th><th>Ram</th><th>8 GB DDR4</th>
          </tr>
          <tr bgcolor="antiquewhite" style="color:black;">
            <th bgcolor="yellow" style="color:black;">5</th><th>Processor</th><th>intel i5 6th gen</th>
          </tr>
          <tr bgcolor="antiquewhite" style="color:black;">
            <th bgcolor="yellow" style="color:black;">6</th><th>SSD</th><th>256 GB</th>
          </tr>
        </center>

</body>
</html>'''


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()  



## OUTPUT:
![alt text](<Screenshot (25).png>)


## RESULT:
The program for implementing simple webserver is executed successfully.

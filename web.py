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
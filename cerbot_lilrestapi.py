import subprocess
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleAPI(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/soc":
            soc = self.get_dbus_value("com.victronenergy.battery.ttyS6", "/Soc")
            self.respond({"soc": soc})
        elif self.path == "/solar":
            voltage = self.get_dbus_value("com.victronenergy.solarcharger.ttyS5", "/Dc/0/Voltage")
            current = self.get_dbus_value("com.victronenergy.solarcharger.ttyS5", "/Dc/0/Current")
            if voltage is not None and current is not None:
                power = voltage * current
                self.respond({"solar_power": power})
            else:
                self.respond({"error": "Could not retrieve solar voltage/current"})
        else:
            self.send_error(404, "Not Found")

    def get_dbus_value(self, service, path):
        try:
            output = subprocess.check_output(["dbus", "-y", service, path, "GetValue"], text=True)
            return float(output.split("=")[-1].strip())
        except Exception as e:
            return None

    def respond(self, data):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

server_address = ('', 8080)
httpd = HTTPServer(server_address, SimpleAPI)
print("Starting server on port 8080...")
httpd.serve_forever()

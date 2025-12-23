from http.server import BaseHTTPRequestHandler, HTTPServer
# http.server یک کتابخانه داخل پایتون
#HttpServer خود سرور رو میسازه
#BaseHTTPRequestHandler برای مدیریت درخواست‌ها استفاده میشه
class SimpleGETHandler(BaseHTTPRequestHandler):
    #این کلاس ازBaseHTTPHandler ارث بری می کند
    #هر وقت درخواستی اومد این کلاس تصمیم می گیرد چه اتفاقی بیفتد
    def do_GET(self):
        #این متد برای مدیریت درخواست‌های GET استفاده میشه
        print(f"Received GET request for path: {self.path}")

        self.send_response(200)  # ارسال پاسخ با کد وضعیت 200 (موفقیت)
        self.send_header('Content-type', 'text/html')  # تنظیم هدر پاسخ
        self.end_headers()  # پایان هدرها
        response_content = f"<html><body><h1>Hello! You accessed: {self.path}</h1></body></html>"

        self.wfile.write(response_content.encode('utf-8'))
    # سایر متدها را رد می‌کنیم
    def do_POST(self):
        self.send_error(405, "Method Not Allowed")

    def do_PUT(self):
        self.send_error(405, "Method Not Allowed")

    def do_DELETE(self):
        self.send_error(405, "Method Not Allowed")

host = 'localhost'
port = 8080

with HTTPServer((host, port), SimpleGETHandler) as server:
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()


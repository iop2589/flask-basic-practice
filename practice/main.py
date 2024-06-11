from flask import Flask

app = Flask(__name__)

@app.get("/hello")
def hello():
  return "<h1>Hello</h1>"

if __name__ == "__main__":
  host_addr = "127.0.0.1"
  port_num = "8080"
  app.run(host=host_addr,port=port_num)
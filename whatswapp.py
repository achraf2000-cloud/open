import request


data = {"first_name":"Richard", "second_name":"Stallman"}
r = requests.post("http://linuxfr.org", data = data)

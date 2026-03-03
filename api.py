import requests

proxies = {
    "http": "http://proxy.spo.ifsp.edu.br:3128",
    "https": "http://proxy.spo.ifsp.edu.br:3128"
}


try:
    r = requests.get("https://swapi.dev/api/people/1", proxies=proxies)
    print(r.status_code)
except requests.exceptions.ProxyError as e:
    print(f"Proxy error {e}")

print(r.url)
print(r.text)

data = r.json()

print(type(data))
print(data["name"])
print(data.keys())

planet = data["homeworld"]


try:
    p = requests.get(data["homeworld"], proxies=proxies)
    print(p.status_code)
except requests.exceptions.ProxyError as e:
    print(f"Proxy error {e}")

print(p.url)
print(p.text)



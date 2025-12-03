import requests


url_template = "https://wttr.in/{}?nTquQ&lang=ru"

article_id = [
	"Лондон", 
	"Шереметьево", 
	"Череповец"
]

for art in article_id:
    url = f"https://wttr.in/{art}?lang=ru&m&n&Q&T"
    response = requests.get(url, headers={"User-Agent": "curl"})
    print(f"\n{art}")
    print(response.text)
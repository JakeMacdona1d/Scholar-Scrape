import requests
import webbrowser


headers = { # To appear not as a bot
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
}

params = {
    "where": "web"        # theres's also a "nexearch" param that will produce different results
}


def save_naver_organic_results():
    html = requests.get("https://scholar.google.com/citations?view_op=view_citation&hl=en&user=ggHXV-4AAAAJ&citation_for_view=ggHXV-4AAAAJ:7PzlFSSx8tAC", params=params, headers=headers).text

    # replacing every space to underline (_) so bruce lee will become bruce_lee 
    # query = params['query'].replace(" ", "_")

    with open(f"naver_organic_results.html", mode="w", encoding="utf-8") as file:
        file.write(html)
save_naver_organic_results()

webbrowser.open('naver_organic_results.html') 

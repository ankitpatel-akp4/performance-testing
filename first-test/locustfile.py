from locust import task, run_single_user
from locust import FastHttpUser


class en_wikipedia_org(FastHttpUser):
    host = "https://en.wikipedia.org"
    default_headers = {
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Linux"',
    }

    @task
    def t(self):
        with self.client.request(
            "GET",
            "/wiki/HAR_(file_format)",
            headers={
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "accept-language": "en-US,en-IN;q=0.9,en;q=0.8",
                "cache-control": "max-age=0",
                "referer": "https://github.com/SvenskaSpel/har2locust",
                "sec-fetch-dest": "document",
                "sec-fetch-mode": "navigate",
                "sec-fetch-site": "cross-site",
                "sec-fetch-user": "?1",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass
        with self.client.request(
            "GET",
            "/static/favicon/wikipedia.ico",
            headers={
                "Referer": "https://en.wikipedia.org/wiki/HAR_(file_format)",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            },
            catch_response=True,
        ) as resp:
            pass


if __name__ == "__main__":
    run_single_user(en_wikipedia_org)

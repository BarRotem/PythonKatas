import requests
import time


def request_retry(url, retry_limit=3):
    """
    The function performs a GET request to the given url, while implementing a linear retry logic, sleeping 3 seconds between every try.
    Failed request is defined by status code >= 500.
    The function stops after retry_limit retries (if retry_limit=3, there should be 4 attempts in total. The first one, and 3 more retries).

    :param url: a valid url
    :param retry_limit: int
    :return: Return the resulting response as text.
    """
    retry_counts = 0
    response = requests.get(url)

    while response.status_code >= 500 and retry_counts <= retry_limit:
        # Request failed, linearly retry
        print(f"Unable to issue GET request to : {response.url}, retry count : {retry_counts}")
        time.sleep(3)
        response = requests.get(url)
        retry_counts += 1
    if response.status_code == 200:
        return f"Response status code for {response.url} is : {response.status_code}\nResponse text is : {response.text}\n"
    else:
        return f"Status code for requested url : {response.url} is not 200 (OK). Received : {response.status_code}\n"


if __name__ == '__main__':
    print(request_retry('https://google.com'))
    #print(request_retry('https://sdfsgewcwe4rc34rxwrfxw3r3xrxr.com'))
    print(request_retry('https://httpbin.org/status/500'))


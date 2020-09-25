import re
import json
import os
import threading
import time
import requests
from requests.exceptions import RequestException


# for i in range(len(problemset)):

def parse_stat_status_pairs(stat_status_pairs):
    print("")
    print("")
    print("parse_stat_status_pairs")
    print(type(stat_status_pairs[0]), len(stat_status_pairs[0]))
    print(stat_status_pairs[0])
    question__title_slug = stat_status_pairs[0]["stat"]["question__title_slug"]
    construct_url(question__title_slug)
    # if title == "robot-room-cleaner":
    #     continue
    # time.sleep(0.1)
    # t = threading.Thread(target=construct_url, args=(question__title_slug,))
    # t.start()

    # for i in range(len(stat_status_pairs)):
    #     title = stat_status_pairs[i]["stat"]["question__title_slug"]
    #     if title == "robot-room-cleaner":
    #         continue
    #     # construct_url(title)
    #     time.sleep(0.1)
    #     t = threading.Thread(target=construct_url, args=(title,))
    #     t.start()


def construct_url(question__title_slug):
    url = "https://leetcode.com/problems/" + question__title_slug + "/description/"
    print(url + "\n")
    get_topic_content(url, question__title_slug)


def save_problem(title, content):
    # content = bytes(content,encoding = 'utf8')
    filename = title + ".html"
    with open(filename, 'w+', encoding="utf-8")as f:
        f.write(content)


def get_topic_content(topic_url, title):
    response = requests.get(topic_url)
    set_cookie = response.headers["Set-Cookie"]
    print("setCookie:", set_cookie)
    try:
        pattern = re.compile("csrftoken=(.*?);.*?", re.S)
        csrftoken = re.search(pattern, set_cookie)
        print("csrftoken:", csrftoken.group())
        url = "https://leetcode.com/graphql"
        data = {"operationName": "getQuestionDetail",
                "variables": {"titleSlug": title},
                "query": "query getQuestionDetail($titleSlug: String!) {\n  isCurrentUserAuthenticated\n  question(titleSlug: $titleSlug) {\n    questionId\n    questionFrontendId\n    questionTitle\n    translatedTitle\n    questionTitleSlug\n    content\n    translatedContent\n    difficulty\n    stats\n    allowDiscuss\n    contributors\n    similarQuestions\n    mysqlSchemas\n    randomQuestionUrl\n    sessionId\n    categoryTitle\n    submitUrl\n    interpretUrl\n    codeDefinition\n    sampleTestCase\n    enableTestMode\n    metaData\n    enableRunCode\n    enableSubmit\n    judgerAvailable\n    infoVerified\n    envInfo\n    urlManager\n    article\n    questionDetailUrl\n    libraryUrl\n    companyTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    companyTagStats\n    topicTags {\n      name\n      slug\n      translatedName\n      __typename\n    }\n    __typename\n  }\n  interviewed {\n    interviewedUrl\n    companies {\n      id\n      name\n      slug\n      __typename\n    }\n    timeOptions {\n      id\n      name\n      __typename\n    }\n    stageOptions {\n      id\n      name\n      __typename\n    }\n    __typename\n  }\n  subscribeUrl\n  isPremium\n  loginUrl\n}\n"
                }
        headers = {
            'x-csrftoken': csrftoken.group(1),
            'referer': topic_url,
            'content-type': 'application/json',
            'origin': 'https://leetcode.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        cookies = {'__cfduid': 'd9ce37537c705e759f6bea15fffc9c58b1525271602',
                   '_ga': 'GA1.2.5783653.1525271604',
                   '_gid': 'GA1.2.344320119.1533189808',
                   'csrftoken': csrftoken.group(1),
                   ' _gat': '1'}
        # payload表单为json格式

        dumpJsonData = json.dumps(data)
        response = requests.post(url, data=dumpJsonData, headers=headers, cookies=cookies)
        dictInfo = json.loads(response.text)
        content = dictInfo["data"]["question"]["content"]
    except Exception as e:
        print(e)
        print("错误：" + topic_url)


'''
    for string in soup.stripped_strings:
        print(string)
'''


def topic_content():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    if response.status_code == 200:
        stat_status_pairs = json.loads(response.text)['stat_status_pairs']
        # print(len(stat_status_pairs), stat_status_pairs)
    else:
        return None
    parse_stat_status_pairs(stat_status_pairs)


def topics():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    set_cookie = response.headers["Set-Cookie"]
    print("setCookie:", set_cookie)
    pattern = re.compile("csrftoken=(.*?);.*?", re.S)
    csrf_token = re.search(pattern, set_cookie).group(1)
    print("csrftoken:", csrf_token)
    url = "https://leetcode.com/graphql"
    params = {"operationName": "managementFieldPermissions",
              "query": "query managementFieldPermissions {\n  fieldPermissionInfos(namespaces: [NOJ]) {\n    "
                       "fieldName\n    permissionCodes\n    __typename\n  }\n}\n",
              "variables": {}
              }
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-length': '229',
        'content-type': 'application/json',
        'cookie': '''__auc=ee7edfd31746c1a19227745bfea; gr_user_id=f4c5615a-ac79-494c-b504-5b041f21f0e7; 
        grwng_uid=b7a19ff0-9745-48e2-84b3-0b6a3a27a0c0; a2873925c34ecbd2_gr_last_sent_cs1=leon-6u; csrftoken={}; 
        LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjE2MjI1NCIsIl9hdXRoX3VzZXJf
        YmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWFmYWNmMzkwNzV
        lYmMxYjlhODgzZGU1NGQzOThkMzdlNDA4MzA4MzQxYTczM2ExZWQzNzg5OTNiZmY0ZWEzMiIsImlkIjoyMTYyMjU0LCJlbWFpbCI6IiIsInVzZX
        JuYW1lIjoibGVvbi02dSIsInVzZXJfc2x1ZyI6Imxlb24tNnUiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpe
        XVuLWxjLXVwbG9hZC9kZWZhdWx0X2F2YXRhci5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTU5OTgwMTEzMi40NDI4
        NTMyfQ.q5pZpS-5vhH-RqIb0kXnCQjitkZ64LJ5ICEDZzSAIYY; _ga=GA1.2.2015793502.1600309199; 
        Hm_lvt_fa218a3ff7179639febdb15e372f411c=1599541640,1599711492,1599711547,1601000358; 
        a2873925c34ecbd2_gr_session_id=9ae583bd-e73b-4a9e-bbdc-0d601d320091; 
        a2873925c34ecbd2_gr_last_sent_sid_with_cs1=9ae583bd-e73b-4a9e-bbdc-0d601d320091; 
        a2873925c34ecbd2_gr_session_id_9ae583bd-e73b-4a9e-bbdc-0d601d320091=true; a2873925c34ecbd2_gr_cs1=leon-6u; 
        Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1601002401'''.format(csrf_token),
        'origin': 'https://leetcode.com',
        'referer': url,
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36',
        'x-csrftoken': csrf_token
    }
    topic_res = requests.post(url, headers=headers, data=params)
    print("")
    print("")
    print(topic_res.status_code)
    print("")
    print(topic_res.text)


"""
__auc=ee7edfd31746c1a19227745bfea; 
gr_user_id=f4c5615a-ac79-494c-b504-5b041f21f0e7; 
grwng_uid=b7a19ff0-9745-48e2-84b3-0b6a3a27a0c0; 
a2873925c34ecbd2_gr_last_sent_cs1=leon-6u; 
csrftoken=btnfnQakB0R1hRrFudSrvHSnGIAt1Crl0JDjhb0f3xIuxHJymr0cnFYtjhvJBuLz; 
LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMjE2MjI1NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWFmYWNmMzkwNzVlYmMxYjlhODgzZGU1NGQzOThkMzdlNDA4MzA4MzQxYTczM2ExZWQzNzg5OTNiZmY0ZWEzMiIsImlkIjoyMTYyMjU0LCJlbWFpbCI6IiIsInVzZXJuYW1lIjoibGVvbi02dSIsInVzZXJfc2x1ZyI6Imxlb24tNnUiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC9kZWZhdWx0X2F2YXRhci5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwiX3RpbWVzdGFtcCI6MTU5OTgwMTEzMi40NDI4NTMyfQ.q5pZpS-5vhH-RqIb0kXnCQjitkZ64LJ5ICEDZzSAIYY; 
_ga=GA1.2.2015793502.1600309199; 
Hm_lvt_fa218a3ff7179639febdb15e372f411c=1599541640,1599711492,1599711547,1601000358; 
a2873925c34ecbd2_gr_session_id=9ae583bd-e73b-4a9e-bbdc-0d601d320091; 
a2873925c34ecbd2_gr_last_sent_sid_with_cs1=9ae583bd-e73b-4a9e-bbdc-0d601d320091; 
a2873925c34ecbd2_gr_session_id_9ae583bd-e73b-4a9e-bbdc-0d601d320091=true; 
a2873925c34ecbd2_gr_cs1=leon-6u; 
Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1601002401
"""


if __name__ == '__main__':
    topics()

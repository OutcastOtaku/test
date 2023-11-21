import base64
from github import Github
from pprint import pprint

def print_repo(repo):

    print("Full name:", repo.full_name)

    print("Description:", repo.description)

    print("Date created:", repo.created_at)

    print("Date of last push:", repo.pushed_at)

    print("Home page:", repo.homepage)

    print("Language:", repo.language)

    print("Number of forks:", repo.forks)

    print("Number of stars:", repo.stargazers_count)
    print("-"*50)

    print("Contents:")
    try:
        for content in repo.get_contents(""):
            print(content)
        print("Liscense:", base64.b64decode(repo.get_license().content.encode()).decode())
    except:
        pass

username = "OutcastOtaku"

g = Github()

user = g.get_user(username)

for repo in user.get_repos():
    print_repo(repo)
    print("="*100)

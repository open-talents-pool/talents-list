import json
import argparse
from datetime import datetime
import requests

argparser = argparse.ArgumentParser()
argparser.add_argument('--github-handle', required=True)
argparser.add_argument('--name', required=True)
argparser.add_argument('--email-address', required=False)
argparser.add_argument('--contact-link', required=True)
argparser.add_argument('--primary-role-title', required=True)
argparser.add_argument('--country-of-residence', required=True)
argparser.add_argument('--city-of-residence', required=False)
argparser.add_argument('--technical-skills', required=True)
argparser.add_argument('--communication-languages', required=True)
argparser.add_argument('--willing-to-relocate', required=True)
argparser.add_argument('--willing-for-remote-work', required=True)

args = argparser.parse_args()

def get_user_oldest_repository_date(username):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {
        "Accept": "application/vnd.github.v3+json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        repos = response.json()
        if repos:
            earliest_repo = min(repos, key=lambda repo: repo['created_at'])
            join_date = earliest_repo['created_at']
            return join_date
        else:
            return "Doesn’t have any public repositories ."
    else:
        return f"Error: {response.status_code}"
    

data = {
    'github_handle': args.github_handle,
    'name': args.name,  
    'email_address': args.email_address,
    'contact_link': args.contact_link,  
    'primary_role_title': args.primary_role_title,
    'country_of_residence': args.country_of_residence,
    'city_of_residence':args.city_of_residence,
    'technical_skills': [skill.strip() for skill in str(args.technical_skills).split(',')],
    'communication_languages': [language.strip() for language in str(args.communication_languages).split(',')],
    'willing_to_relocate': str(args.willing_to_relocate).lower() == 'true',
    'willing_for_remote_work': str(args.willing_for_remote_work).lower() == 'true',
    'oldest_repository_date': get_user_oldest_repository_date(args.github_handle),
    'updated_at': datetime.now().isoformat()
}

file = args.github_handle + '.json'

with open(file, 'w') as f:
    json.dump(data, f, indent=2)

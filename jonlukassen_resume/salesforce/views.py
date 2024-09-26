import requests
from bs4 import BeautifulSoup
from django.shortcuts import render

def trailhead_profile(request):
    url = 'https://trailblazer.me/id/jlukassen'  # Replace with your Trailhead ID
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example: Scrape badge or rank data (adjust according to page structure)
        # Find all badges (this is just an example, you may need to inspect the page to get the correct tags)
        badges = soup.find_all('div', class_='badge-class')  # Adjust to actual class names

        # Extract badges or other progress info
        badge_list = [badge.text.strip() for badge in badges]

        return render(request, 'salesforce/trailhead_profile.html', {'badges': badge_list})
    else:
        return render(request, 'salesforce/trailhead_profile.html', {'error': 'Failed to retrieve Trailhead data.'})

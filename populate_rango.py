import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyITTeamProject.settings')

import django

django.setup()
from rango.models import City, Scenery
from django.contrib.auth.models import User


def populate():
    london = [
        {'title': 'London Eye',
         'url': 'https://www.visitbritain.com/us/en/london-eye',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/LondonEye.jpg'},
        {'title': 'London Dungeon',
         'url': 'https://www.visitbritain.com/us/en/london-dungeon',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/LondonDungeon.jpg'},
        {'title': 'Londons West End',
         'url': 'https://www.visitbritain.com/us/en/londons-west-end',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/LondonsWestEnd.jpg'}]

    manchester = [
        {'title': 'Manchester United Stadium Tour',
         'url': 'https://www.visitbritainshop.com/usa/manchester-united-museum-and-tour/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=manchester_united_museum_and_tour',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/ManchesterUnitedTour.jpg'},
        {'title': 'Manchester City Stadium Tour',
         'url': 'https://www.visitbritainshop.com/usa/manchester-city-football-club-stadium-tour/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=manchester_city_football_club_stadium_tour',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/ManchesterCityTour.jpg'},
        {'title': 'BritRail England Rail Pass',
         'url': 'https://www.visitbritainshop.com/usa/britrail-england-pass/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=britrail_england_pass',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/EnglandRailPass.jpg'},
        {'title': 'National Trust Touring Pass',
         'url': 'https://www.visitbritainshop.com/usa/national-trust-touring-pass/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=national_trust_touring_pass',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/LondonEye.jpg'},
        {'title': 'MP3 Walking Tour-Manchester',
         'url': 'https://www.visitbritainshop.com/usa/mp3-walking-tour-manchester/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=mp3_walking_tour_manchester',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/LondonEye.jpg'}]

    glasgow = [
        {'title': 'Glasgow University',
         'url': 'https://www.gla.ac.uk/',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/UniversityOfGlasgow.png'},
        {'title': 'Glasgow School of Art',
         'url': 'https://www.visitbritain.com/us/en/glasgow-school-art',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/GlasgowSchoolOfArt.jpg'},
        {'title': 'Kelvingrove Art Gallery and Museum',
         'url': 'https://www.visitbritain.com/us/en/kelvingrove-art-gallery-and-museum',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/KelvingroveMuseum.jpg'},
        {'title': 'Riverside Museum',
         'url': 'https://www.visitbritain.com/us/en/riverside-museum',
         'intro': 'Scenery introduction',
         'picture': 'user_scenery_images/RiversideMuseum.jpg'}]

    cats = {'London': {'cities': london, 'views': 128, 'likes': 64,
                       'intro': 'Discover 4 UNESCO World Heritage Sites (including the Tower of London), relax in 8 lush Royal Parks and explore free museums and galleries such as the British Museum.'},
            'Manchester': {'cities': manchester, 'views': 64, 'likes': 32,
                           'intro': 'cityIntro'},
            'Glasgow': {'cities': glasgow, 'views': 32, 'likes': 16,
                        'intro': 'cityIntro'}}

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'], intro=cat_data['intro'])
        for p in cat_data['cities']:
            add_page(c, p['title'], p['url'], p['picture'], p['intro'])

    for c in City.objects.all():
        for p in Scenery.objects.filter(city=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, picture, intro='sceneryIntroduction', views=0):
    p = Scenery.objects.get_or_create(city=cat, title=title)[0]
    p.url = url
    p.picture = picture
    p.intro = intro
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0, intro='cityIntroduction'):
    c = City.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.intro = intro
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()

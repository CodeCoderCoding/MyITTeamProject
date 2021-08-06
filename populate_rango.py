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
         'intro': 'The enormous London Eye is difficult to miss. It towers above Westminster and the Houses of Parliament giving you a fantastic bird’s eye view over all of London. The ride takes 30 minutes, and carries you up to a height of 135 metres - taller than a football field is long',
         'picture': 'user_scenery_images/LondonEye.jpg'},
        {'title': 'London Dungeon',
         'url': 'https://www.visitbritain.com/us/en/london-dungeon',
         'intro': 'Dare you brave the dank and dangerous London Dungeon? Your first thrill of the day will be the vertical free-fall ride that takes you down to the dungeons. Once underground youll experience the darker side of the city through the ages from Jack the Ripper to the plague. Just 19 interactive shows covers over 1,000 years of history, all while keeping you on the edge of your seat! Brave guests will love the opportunity to try and Escape Execution - the new escape room - but good luck, you only get 60 minutes before the Executioner returns!',
         'picture': 'user_scenery_images/LondonDungeon.jpg'},
        {'title': 'Londons West End',
         'url': 'https://www.visitbritain.com/us/en/londons-west-end',
         'intro': 'The West End, also known as Theatreland, covers a large area of central London and is home to more than 40 historic and modern theatres showing the worlds best smash-hit shows, plays and glitzy musicals, where you can see everything from The Mousetrap to The Lion King. Many theatres also offer backstage tours for a unique glimpse into life behind the curtains. A night out in a London West End theatre is not to be missed!',
         'picture': 'user_scenery_images/LondonsWestEnd.jpg'}]

    manchester = [
        {'title': 'Manchester United Stadium Tour',
         'url': 'https://www.visitbritainshop.com/usa/manchester-united-museum-and-tour/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=manchester_united_museum_and_tour',
         'intro': 'Tour the celebrated Old Trafford – home of one of the worlds most popular football clubs ',
         'picture': 'user_scenery_images/ManchesterUnitedTour.jpg'},
        {'title': 'Manchester City Stadium Tour',
         'url': 'https://www.visitbritainshop.com/usa/manchester-city-football-club-stadium-tour/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=manchester_city_football_club_stadium_tour',
         'intro': 'Explore City’s dressing room, press room, players’ tunnel and more on a tour of the Etihad ',
         'picture': 'user_scenery_images/ManchesterCityTour.jpg'},
        {'title': 'BritRail England Rail Pass',
         'url': 'https://www.visitbritainshop.com/usa/britrail-england-pass/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=britrail_england_pass',
         'intro': 'A pass for unlimited travel on rail services in England. ',
         'picture': 'user_scenery_images/EnglandRailPass.jpg'},
        {'title': 'National Trust Touring Pass',
         'url': 'https://www.visitbritainshop.com/usa/national-trust-touring-pass/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=national_trust_touring_pass',
         'intro': 'Discover the heritage houses of Britain on a National Trust touring pass, available at VisitBritain. ',
         'picture': 'user_scenery_images/LondonEye.jpg'},
        {'title': 'MP3 Walking Tour-Manchester',
         'url': 'https://www.visitbritainshop.com/usa/mp3-walking-tour-manchester/?utm_medium=referral&utm_source=visitbritain.com&utm_campaign=widget&utm_content=mp3_walking_tour_manchester',
         'intro': 'Encounter Manchesters famous landmarks on this informative and revealing audio tour ',
         'picture': 'user_scenery_images/LondonEye.jpg'}]

    glasgow = [
        {'title': 'Glasgow University',
         'url': 'https://www.gla.ac.uk/',
         'intro': 'The University of Glasgow (abbreviated as Glas. in post-nominals; Scottish Gaelic: Oilthigh Ghlaschu[5]) is a public research university in Glasgow, Scotland. Founded by '
                  'papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotlands four ancient universities. Along with the universities of Edinburgh, '
                  'Aberdeen, and St Andrews, the university was part of the Scottish Enlightenment during the 18th century. ',
         'picture': 'user_scenery_images/UniversityOfGlasgow.png'},
        {'title': 'Glasgow School of Art',
         'url': 'https://www.visitbritain.com/us/en/glasgow-school-art',
         'intro': 'The architect Charles Rennie Mackintosh’s masterpiece, the Glasgow School of Art, is a remarkable building, noted for its art nouveau ironwork, curling organic forms and '
                  'unusual furniture. To see inside, you’ll need to join a tour, so as not to disturb the students who work here.',
         'picture': 'user_scenery_images/GlasgowSchoolOfArt.jpg'},
        {'title': 'Kelvingrove Art Gallery and Museum',
         'url': 'https://www.visitbritain.com/us/en/kelvingrove-art-gallery-and-museum',
         'intro': 'With 8,000 objects in 22 galleries, Kelvingrove is one of Britains largest free museums. Explore its wealth '
                  'of art and historical objects, from arms and armour to paintings of all eras and movements, and even a natural history section.',
         'picture': 'user_scenery_images/KelvingroveMuseum.jpg'},
        {'title': 'Riverside Museum',
         'url': 'https://www.visitbritain.com/us/en/riverside-museum',
         'intro': 'Scotlands museum of transport and travel, the Riverside Museum takes you on a fascinating journey through the story of vehicles, '
                  'from horse-drawn carriages to early, automobiles, locomotives and some of Scotlands earliest buses and trams.',
         'picture': 'user_scenery_images/RiversideMuseum.jpg'}]

    edinburgh = [
        {'title': 'Edinburgh University',
         'url': 'https://www.gla.ac.uk/',
         'intro': 'The University of Glasgow (abbreviated as Glas. in post-nominals; Scottish Gaelic: Oilthigh Ghlaschu[5]) is a public research university in Glasgow, Scotland. Founded by '
                  'papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotlands four ancient universities. Along with the universities of Edinburgh, '
                  'Aberdeen, and St Andrews, the university was part of the Scottish Enlightenment during the 18th century. ',
         'picture': 'user_scenery_images/UniversityOfGlasgow.png'},
        {'title': 'Glasgow School of Art',
         'url': 'https://www.visitbritain.com/us/en/glasgow-school-art',
         'intro': 'The architect Charles Rennie Mackintosh’s masterpiece, the Glasgow School of Art, is a remarkable building, noted for its art nouveau ironwork, curling organic forms and '
                  'unusual furniture. To see inside, you’ll need to join a tour, so as not to disturb the students who work here.',
         'picture': 'user_scenery_images/GlasgowSchoolOfArt.jpg'},
        {'title': 'Kelvingrove Art Gallery and Museum',
         'url': 'https://www.visitbritain.com/us/en/kelvingrove-art-gallery-and-museum',
         'intro': 'With 8,000 objects in 22 galleries, Kelvingrove is one of Britains largest free museums. Explore its wealth '
                  'of art and historical objects, from arms and armour to paintings of all eras and movements, and even a natural history section.',
         'picture': 'user_scenery_images/KelvingroveMuseum.jpg'},
        {'title': 'Riverside Museum',
         'url': 'https://www.visitbritain.com/us/en/riverside-museum',
         'intro': 'Scotlands museum of transport and travel, the Riverside Museum takes you on a fascinating journey through the story of vehicles, '
                  'from horse-drawn carriages to early, automobiles, locomotives and some of Scotlands earliest buses and trams.',
         'picture': 'user_scenery_images/RiversideMuseum.jpg'}]

    cambridge = [
        {'title': 'Cambridge University',
         'url': 'https://www.gla.ac.uk/',
         'intro': 'The University of Glasgow (abbreviated as Glas. in post-nominals; Scottish Gaelic: Oilthigh Ghlaschu[5]) is a public research university in Glasgow, Scotland. Founded by '
                  'papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotlands four ancient universities. Along with the universities of Edinburgh, '
                  'Aberdeen, and St Andrews, the university was part of the Scottish Enlightenment during the 18th century. ',
         'picture': 'user_scenery_images/UniversityOfGlasgow.png'},
        {'title': 'Glasgow School of Art',
         'url': 'https://www.visitbritain.com/us/en/glasgow-school-art',
         'intro': 'The architect Charles Rennie Mackintosh’s masterpiece, the Glasgow School of Art, is a remarkable building, noted for its art nouveau ironwork, curling organic forms and '
                  'unusual furniture. To see inside, you’ll need to join a tour, so as not to disturb the students who work here.',
         'picture': 'user_scenery_images/GlasgowSchoolOfArt.jpg'},
        {'title': 'Kelvingrove Art Gallery and Museum',
         'url': 'https://www.visitbritain.com/us/en/kelvingrove-art-gallery-and-museum',
         'intro': 'With 8,000 objects in 22 galleries, Kelvingrove is one of Britains largest free museums. Explore its wealth '
                  'of art and historical objects, from arms and armour to paintings of all eras and movements, and even a natural history section.',
         'picture': 'user_scenery_images/KelvingroveMuseum.jpg'},
        {'title': 'Riverside Museum',
         'url': 'https://www.visitbritain.com/us/en/riverside-museum',
         'intro': 'Scotlands museum of transport and travel, the Riverside Museum takes you on a fascinating journey through the story of vehicles, '
                  'from horse-drawn carriages to early, automobiles, locomotives and some of Scotlands earliest buses and trams.',
         'picture': 'user_scenery_images/RiversideMuseum.jpg'}]

    oxford = [
        {'title': 'Oxford University',
         'url': 'https://www.gla.ac.uk/',
         'intro': 'The University of Glasgow (abbreviated as Glas. in post-nominals; Scottish Gaelic: Oilthigh Ghlaschu[5]) is a public research university in Glasgow, Scotland. Founded by '
                  'papal bull in 1451, it is the fourth-oldest university in the English-speaking world and one of Scotlands four ancient universities. Along with the universities of Edinburgh, '
                  'Aberdeen, and St Andrews, the university was part of the Scottish Enlightenment during the 18th century. ',
         'picture': 'user_scenery_images/UniversityOfGlasgow.png'},
        {'title': 'Glasgow School of Art',
         'url': 'https://www.visitbritain.com/us/en/glasgow-school-art',
         'intro': 'The architect Charles Rennie Mackintosh’s masterpiece, the Glasgow School of Art, is a remarkable building, noted for its art nouveau ironwork, curling organic forms and '
                  'unusual furniture. To see inside, you’ll need to join a tour, so as not to disturb the students who work here.',
         'picture': 'user_scenery_images/GlasgowSchoolOfArt.jpg'},
        {'title': 'Kelvingrove Art Gallery and Museum',
         'url': 'https://www.visitbritain.com/us/en/kelvingrove-art-gallery-and-museum',
         'intro': 'With 8,000 objects in 22 galleries, Kelvingrove is one of Britains largest free museums. Explore its wealth '
                  'of art and historical objects, from arms and armour to paintings of all eras and movements, and even a natural history section.',
         'picture': 'user_scenery_images/KelvingroveMuseum.jpg'},
        {'title': 'Riverside Museum',
         'url': 'https://www.visitbritain.com/us/en/riverside-museum',
         'intro': 'Scotlands museum of transport and travel, the Riverside Museum takes you on a fascinating journey through the story of vehicles, '
                  'from horse-drawn carriages to early, automobiles, locomotives and some of Scotlands earliest buses and trams.',
         'picture': 'user_scenery_images/RiversideMuseum.jpg'}]

    cats = {'London': {'cities': london, 'views': 128, 'likes': 64,
                       'intro': 'Discover 4 UNESCO World Heritage Sites (including the Tower of London), relax in 8 lush Royal Parks and explore free museums and galleries such as the British Museum. '
                                'London shopping offers everything from flea markets and vintage shops to luxury department stores like Selfridges and Harrods. '
                                'Londoners love to eat. Tuck in to tasty street food or savour haute cuisine at one of the London’s Michelin star restaurants. '
                                'Did you know? There are more than 230 professional theatres in London. Head to the Globe theatre, to see Shakespeare’s plays performed as they would have been in Tudor times.'},
            'Manchester': {'cities': manchester, 'views': 64, 'likes': 32,
                           'intro': 'Home to two of Englands most popular football teams – Manchester United and Manchester City – dont miss the chance to get '
                                    'closer to the history and the legends of these iconic clubs with a stadium tour. Experience the atmosphere of Canal Street - one of Britain’s most famous gay villages. '
                                    'Did you know? On Curry Mile, youll have the pick of more than 70 restaurants serving South Asian and Middle Eastern cuisines. '
                                    'Art lover? Head straight to The Lowry. This unique gallery is home to the worlds largest collection of works by LS Lowry, one of the best loved British artists of the 20th century.'},
            'Glasgow': {'cities': glasgow, 'views': 32, 'likes': 16,
                        'intro': 'Its history stretches back to the Stone Age, but this city is thoroughly modern and no stranger to a good time. '
                                 'Glasgow is a top spot for a city break if you’re keen on contemporary culture. Its home to over 20 museums and '
                                 'art galleries, including the award-winning Burrell Collection, the huge Kelvingrove Museum and Art Gallery and '
                                 'the Riverside Museum, a radical space designed by Zaha Hadid for the city’s transport heritage. '
                                 'The city is also the home of both the Scottish Opera and the Scottish Ballet.'},
            'Edinburgh': {'cities': edinburgh, 'views': 32, 'likes': 16,
                        'intro': 'Its history stretches back to the Stone Age, but this city is thoroughly modern and no stranger to a good time. '
                                 'Glasgow is a top spot for a city break if you’re keen on contemporary culture. Its home to over 20 museums and '
                                 'art galleries, including the award-winning Burrell Collection, the huge Kelvingrove Museum and Art Gallery and '
                                 'the Riverside Museum, a radical space designed by Zaha Hadid for the city’s transport heritage. '
                                 'The city is also the home of both the Scottish Opera and the Scottish Ballet.'},
            'Cambridge': {'cities': cambridge, 'views': 32, 'likes': 16,
                        'intro': 'Its history stretches back to the Stone Age, but this city is thoroughly modern and no stranger to a good time. '
                                 'Glasgow is a top spot for a city break if you’re keen on contemporary culture. Its home to over 20 museums and '
                                 'art galleries, including the award-winning Burrell Collection, the huge Kelvingrove Museum and Art Gallery and '
                                 'the Riverside Museum, a radical space designed by Zaha Hadid for the city’s transport heritage. '
                                 'The city is also the home of both the Scottish Opera and the Scottish Ballet.'},
            'Oxford': {'cities': oxford, 'views': 32, 'likes': 16,
                        'intro': 'Its history stretches back to the Stone Age, but this city is thoroughly modern and no stranger to a good time. '
                                 'Glasgow is a top spot for a city break if you’re keen on contemporary culture. Its home to over 20 museums and '
                                 'art galleries, including the award-winning Burrell Collection, the huge Kelvingrove Museum and Art Gallery and '
                                 'the Riverside Museum, a radical space designed by Zaha Hadid for the city’s transport heritage. '
                                 'The city is also the home of both the Scottish Opera and the Scottish Ballet.'}, }

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

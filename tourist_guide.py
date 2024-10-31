from datetime import datetime
import geocoder
import wikipedia
import requests
from bs4 import BeautifulSoup
import googlemaps
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import folium
import osmnx as ox
import networkx as nx
from datetime import timedelta

def get_tourist_places(location, country, limit=8):
    tourist_places = set()
    
    try:
        # First try direct Wikipedia page for the location
        try:
            wiki_page = wikipedia.page(f"{location}")
            content = wiki_page.content.lower()
            
            # Look for tourism/attractions section
            tourism_keywords = ['tourism', 'tourist attractions', 'places of interest', 'landmarks']
            for keyword in tourism_keywords:
                if keyword in content:
                    section_start = content.find(keyword)
                    relevant_content = content[section_start:section_start + 2000]
                    lines = relevant_content.split('\n')
                    
                    for line in lines:
                        # Look for specific types of attractions
                        if any(place_type in line.lower() for place_type in 
                              ['beach', 'park', 'museum', 'temple', 'mosque', 'palace', 'fort', 
                               'garden', 'monument', 'square', 'market', 'tower']):
                            words = line.split()
                            for i in range(len(words)-2):
                                potential_place = ' '.join(words[i:i+4])
                                if len(potential_place.split()) >= 2:
                                    tourist_places.add(potential_place.title())
        except:
            pass

        # If not enough places found, try TripAdvisor
        if len(tourist_places) < 3:
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                search_url = f"https://www.google.com/search?q=top+tourist+attractions+in+{location}+{country}+site:tripadvisor.com"
                response = requests.get(search_url, headers=headers)
                soup = BeautifulSoup(response.text, 'html.parser')
                
                for result in soup.find_all(['h3', 'div']):
                    text = result.get_text()
                    if any(place_type in text.lower() for place_type in 
                          ['beach', 'park', 'museum', 'temple', 'mosque', 'palace', 'fort', 
                           'garden', 'monument', 'square', 'market', 'tower']):
                        tourist_places.add(text.strip().title())
            except:
                pass

        # Clean up the places
        cleaned_places = set()
        unwanted = ['the', 'a', 'an', 'is', 'was', 'review', 'reviews', 'tripadvisor', 
                   'hotel', 'restaurant', 'things', 'to', 'do', 'in', 'top']
        
        for place in tourist_places:
            words = [w for w in place.split() if w.lower() not in unwanted]
            cleaned = ' '.join(words).strip()
            if len(cleaned.split()) >= 2 and not any(char.isdigit() for char in cleaned):
                cleaned_places.add(cleaned)

        return sorted(list(cleaned_places))[:limit] if len(cleaned_places) >= 3 else []
                
    except Exception as e:
        return []

def get_place_details(place_name, location, country):
    try:
        details = {
            'description': '',
            'visiting_hours': None,
            'best_time': None,
            'tips': None,
            'highlights': []
        }

        # Create search queries
        search_queries = [
            f"{place_name} {location}",
            f"{place_name} {country}",
            f"{place_name} tourist attraction",
            f"{place_name}"
        ]

        # Try each search query
        for query in search_queries:
            try:
                wiki_results = wikipedia.search(query)
                
                for result in wiki_results[:3]:
                    try:
                        page = wikipedia.page(result, auto_suggest=False)
                        summary = wikipedia.summary(result, sentences=5)
                        
                        if place_name.lower() in summary.lower():
                            details['description'] = summary
                            content = page.content.lower()
                            
                            # Get visiting hours
                            hour_keywords = ['opening hour', 'visiting hour', 'timing', 'open from', 'visiting time']
                            for keyword in hour_keywords:
                                if keyword in content:
                                    start = content.find(keyword)
                                    hours = content[start:start+150].split('\n')[0]
                                    if len(hours) > 20:
                                        details['visiting_hours'] = hours.capitalize()
                                        break
                            
                            if details['description']:
                                break
                                
                    except wikipedia.exceptions.DisambiguationError:
                        continue
                    except:
                        continue
                
                if details['description']:
                    break
                    
            except:
                continue

        # If no description found
        if not details['description']:
            details['description'] = f"Sorry, couldn't find detailed information about {place_name}."

        return details
        
    except Exception as e:
        return {'description': f"Sorry, couldn't find detailed information about {place_name}."}

def get_distance_details(origin_lat, origin_lng, place_name, location, country):
    try:
        geolocator = Nominatim(user_agent="my_tourist_app")
        
        # Try geocoding with different queries
        for query in [f"{place_name}, {location}, {country}", f"{place_name}, {country}"]:
            try:
                destination = geolocator.geocode(query)
                if destination:
                    break
            except:
                continue
        
        if destination:
            # Calculate distance
            origin = (origin_lat, origin_lng)
            dest = (destination.latitude, destination.longitude)
            distance = geodesic(origin, dest).kilometers
            
            # Create map
            center_point = [(origin_lat + destination.latitude)/2, 
                          (origin_lng + destination.longitude)/2]
            m = folium.Map(location=center_point, zoom_start=11)
            
            # Add markers and route
            folium.Marker(origin, popup='Your Location', 
                         icon=folium.Icon(color='red', icon='info-sign')).add_to(m)
            folium.Marker([destination.latitude, destination.longitude], 
                         popup=place_name, 
                         icon=folium.Icon(color='green', icon='info-sign')).add_to(m)
            folium.PolyLine(locations=[origin, [destination.latitude, destination.longitude]], 
                           weight=3, color='blue', opacity=0.8).add_to(m)
            
            map_file = "route_map.html"
            m.save(map_file)
            
            # Calculate routes for different transport modes
            routes = []
            transport_modes = {
                'car': {'speed': 35},
                'bus': {'speed': 25},
                'taxi': {'speed': 30}
            }
            
            for mode, info in transport_modes.items():
                duration_hours = distance / info['speed']
                duration = timedelta(hours=duration_hours)
                
                routes.append({
                    'mode': mode.upper(),
                    'distance': f"{distance:.2f} km",
                    'duration': f"{int(duration.total_seconds() // 3600)}h {int((duration.total_seconds() % 3600) // 60)}min"
                })
            
            return {
                'status': 'success',
                'routes': routes,
                'map_file': map_file
            }
        
        return {
            'status': 'error',
            'message': f"Couldn't find route to {place_name}"
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': str(e)
        }

def print_message():
    try:
        current_time = datetime.now().strftime("%H:%M:%S")
        g = geocoder.ip('me')
        
        if not g.ok:
            print(f"Current time is: {current_time}")
            print("Could not fetch location details")
            return
            
        location = g.city
        country = g.country
        address = g.address
        current_lat = g.lat
        current_lng = g.lng
        
        print(f"Current time is: {current_time}")
        print(f"Your location: {location}, {country}")
        print(f"Full address: {address}")
        
        try:
            wiki_summary = wikipedia.summary(f"{location}, {country}", sentences=3)
            print("\nAbout your location:")
            print(wiki_summary)
            
            tourist_places = get_tourist_places(location, country)
            if tourist_places:
                print("\nPopular Tourist Attractions:")
                for i, place in enumerate(tourist_places, 1):
                    print(f"{i}. {place}")
                
                while True:
                    print("\nEnter the number of the place you want to know more about (or 0 to exit):")
                    try:
                        choice = int(input())
                        if choice == 0:
                            break
                        if 0 < choice <= len(tourist_places):
                            selected_place = tourist_places[choice-1]
                            print(f"\nDetails about {selected_place}:")
                            
                            details = get_place_details(selected_place, location, country)
                            print("\nDescription:")
                            print(details['description'])
                            
                            if details.get('visiting_hours'):
                                print("\nVisiting Hours:")
                                print(details['visiting_hours'])
                            
                            print("\nRoute Information:")
                            distance_details = get_distance_details(
                                current_lat, current_lng, selected_place, location, country
                            )
                            
                            if distance_details['status'] == 'success':
                                for route in distance_details['routes']:
                                    print(f"\n{route['mode']}:")
                                    print(f"Distance: {route['distance']}")
                                    print(f"Estimated Time: {route['duration']}")
                            else:
                                print(f"Route Information: {distance_details['message']}")
                                
                            print("\nWould you like to see another place? (y/n)")
                            if input().lower() != 'y':
                                break
                        else:
                            print("Invalid choice. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                        
        except Exception as e:
            print("\nCouldn't fetch information about this location.")
            
    except Exception as e:
        print(f"Current time is: {current_time}")
        print("Could not fetch location details")

if __name__ == "__main__":
    print_message()
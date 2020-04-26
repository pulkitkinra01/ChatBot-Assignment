from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"6729d1e80f05377cf88f974a4a148fb0"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		
		# Changing logic to fetch range of max 100 records
		start=0
		count=1
		d=[]

		while( len(d)<100 and len(d)<count ):
			res = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20, start)
			res = json.loads(res)
			d.extend(res['restaurants'])
			start = res['results_shown']
			count = res['results_found']

		# print(results)
		# d = json.loads(results)

		# Filter records for price range
		# d = [data for data in d if data['restaurant']['price_range']==2]

		if len(d) == 0:
			response= "no returants found"
		else:
			response=""
			for restaurant in d:
				res_name =  restaurant['restaurant']['name']
				res_loc  =  restaurant['restaurant']['location']['address']
				res_rating = str(restaurant['restaurant']['user_rating']['aggregate_rating'])
				response = response + "Found "+ res_name + " in "+ res_loc +" has been rated as "+ res_rating + "(out of 5)\n" 

		# if d['results_found'] == 0:
		# 	response= "no returants found"
		# else:
		# 	for restaurant in d['restaurants']:
		# 		res_name =  restaurant['restaurant']['name']
		# 		res_loc  =  restaurant['restaurant']['location']['address']
		# 		res_rating =str(restaurant['restaurant']['user_rating']['aggregate_rating'])
		# 		response=response+ "Found "+ res_name + " in "+ res_loc +" has been rated as "+ res_rating + "(out of 5)\n" 
		
		dispatcher.utter_message("-----\n"+response)
		return [SlotSet('location',loc)]


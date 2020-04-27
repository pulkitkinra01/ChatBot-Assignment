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
		# if(loc==" "):
		# 	dispatcher.utter_message(template="utter_wrong_location")
		# 	return None
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		price_dict = {'Low':1,'Mid':2,'High':3}
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		
		# Changing logic to fetch range of max 100 records
		start=0
		count=1
		d=[]

		while( len(d)<20 and len(d)<count ):
			res = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5, start)
			res = json.loads(res)
			d.extend(res['restaurants'])
			start = start + res['results_shown']
			count = res['results_found']

		# print(results)
		# d = json.loads(results)

		# Filter records for price range
		d = [data for data in d if data['restaurant']['price_range']== price_dict.get(price, 2)]

		if len(d) == 0:
			response= "no returants found"
		else:
			response=""
			d = sorted(d, key = lambda i: i['restaurant']['user_rating']['aggregate_rating'], reverse=True)
			for restaurant in d[:5]:
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

class ActionSendEmail( Action ):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		response = "Email Sent"
		return response
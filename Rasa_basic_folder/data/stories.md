## New Story

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Goa"}
    - slot{"location":"Goa"}
    - slot{"location":"Goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_price
* price_range{"price":"mid"}
    - slot{"price":"mid"}
    - slot{"location":"Goa"}
    - slot{"cuisine":"chinese"}
    - action_search_restaurants
    - slot{"location":"Goa"}
    - utter_email_confirmation
* get_email{"email":"ahbcdj@dkj.com"}
	- slot{"email":"ahbcdj@dkj.com"}
    - slot{"location":"Goa"}
    - slot{"cuisine":"chinese"}
    - action_send_email
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"kolkata"}
    - slot{"location":"kolkata"}
    - slot{"location":"kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - slot{"location":"kolkata"}
    - slot{"cuisine":"Italian"}
    - utter_ask_price
    - slot{"location":"kolkata"}
    - slot{"cuisine":"Italian"}
* price_range{"price":"mid"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"location":"kolkata"}
    - utter_email_confirmation
* affirm
    - slot{"location":"kolkata"}
    - slot{"cuisine":"Italian"}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"Goa"}
    - slot{"location":"Goa"}
    - slot{"location":"Goa"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - slot{"cuisine":"chinese"}
    - utter_ask_price
    - slot{"location":"Goa"}
    - slot{"cuisine":"chinese"}
* price_range{"price":"low"}
    - slot{"price":"mid"}
    - action_search_restaurants
    - slot{"location":"Goa"}
    - utter_email_confirmation
* affirm
    - slot{"location":"Goa"}
    - slot{"cuisine":"chinese"}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"Ajmer"}
    - slot{"location":"Ajmer"}
    - slot{"location":"Ajmer"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - utter_ask_price
* price_range{"price":"Mid"}
    - slot{"price":"Mid"}
    - slot{"price":"Mid"}
    - action_search_restaurants
    - slot{"location":"Ajmer"}
    - utter_email_confirmation
* affirm
    - slot{"location":"Ajmer"}
    - slot{"cuisine":"South Indian"}
    - slot{"price":"Mid"}
    - utter_ask_email
    - slot{"location":"Ajmer"}
    - slot{"cuisine":"South Indian"}
    - slot{"price":"Mid"}
* get_email
    - action_send_email
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"cuisine":"chinese","location":"chandigarh"}
    - slot{"cuisine":"chinese"}
    - slot{"location":"chandigarh"}
    - slot{"cuisine":"chinese"}
    - slot{"location":"chandigarh"}
    - utter_ask_price
* price_range{"price":"High"}
    - slot{"price":"High"}
    - slot{"cuisine":"chinese"}
    - slot{"location":"chandigarh"}
    - slot{"price":"High"}
    - action_search_restaurants
    - slot{"location":"chandigarh"}
    - utter_email_confirmation
    - slot{"cuisine":"chinese"}
    - slot{"location":"chandigarh"}
    - slot{"price":"High"}
* get_email
    - action_send_email
    - utter_goodbye

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"Rishikesh"}
    - slot{"location":"Rishikesh"}
    - slot{"location":"Rishikesh"}
    - utter_wrong_location
    - slot{"location":"Rishikesh"}
    - utter_ask_location
    - slot{"location":"Rishikesh"}
* restaurant_search{"location":"Bhopal"}
    - slot{"location":"Bhopal"}
    - slot{"location":"Bhopal"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - slot{"location":"Rishikesh"}
    - slot{"location":"Bhopal"}
    - slot{"cuisine":"Italian"}
    - utter_ask_price
    - slot{"location":"Rishikesh"}
    - slot{"location":"Bhopal"}
    - slot{"cuisine":"Italian"}
* price_range{"price":"Low"}
    - slot{"price":"Low"}
    - action_search_restaurants
    - slot{"location":"Bhopal"}
    - utter_email_confirmation
* affirm

## New Story

* greet
    - utter_greet
* restaurant_search{"location":"Delhi"}
    - slot{"location":"Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Italian"}
    - slot{"cuisine":"Italian"}
    - utter_ask_price
* price_range{"price":"High"}
    - slot{"price":"High"}
    - action_search_restaurants
    - slot{"location":"Delhi"}
    - utter_email_confirmation
* get_email{"email":"pulkitkinra01@gmail.com"}
    - slot{"email":"pulkitkinra01@gmail.com"}
    - action_send_email
    - slot{"location":"Delhi"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* price_range{"price": "Mid"}
    - slot{"price": "Mid"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_email_confirmation
* get_email{"email": "sharat.chilaka@gmail.com"}
    - slot{"email": "sharat.chilaka@gmail.com"}
    - action_send_email
    - slot{"location": "Bangalore"}
* affirm
    - utter_goodbye
    - action_restart

## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- Hola

## intent:restaurant_search
- I’m hungry. Looking out for some good restaurants
- i'm looking for a place to eat
- I want to grab lunch
- search for restaurants
- show me restaurants
- I am searching for a dinner spot
- in [Gurgaon](location)
- [Mumbai](location)
- [Delhi](location)
- Oh, sorry, in [Goa](location)
- anywhere in [Shimmla](location)
- I am looking for some restaurants in [Bhopal](location).
- I am looking for some restaurants in [Jammu](location)
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- anywhere in the [Srinagar](location)
- please find me a restaurant in [ahmedabad](location)
- I am looking a restaurant in [294328](location)
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad](location)
- show me [chinese](cuisine) restaurants
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- I am looking for [asian fusion](cuisine) food
- can you find me a [chinese](cuisine) restaurant
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine)
- [chinese](cuisine)
- I am looking for [mexican indian fusion](cuisine)
- I’ll prefer [Italian](cuisine)
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- [Vellore](location) [indian](cuisine) restaurant
- please find me [chinese](cuisine) restaurant in [delhi](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- need food
- show me restaurants in [Shimla](location)
- show me restaurants in [Mumbai](location)
- show me restaurants in [shimla](location)
- show me some restaurants in [Mumbai](location)
- Show me some restaurants in [Mumbai](location)
- Need food
- [Goa](location)
- [American](cuisine)
- [Bhopal](location)
- [bengaluru](location)
- [bengaluru](location:Bangalore)
- [American](cuisine)

## intent:get_email
- yes. Please send it to [ahbcdj@dkj.com](email)
- [raju@race.com](email)
- yes please send at [abc@xyz.com](email)
- [sharat.chilaka@gmail.com](email)

## intent:price_range
- [Mid](price)
- [mid](price)
- [cheap](price)
- [High](price)
- [Low](price)
- show me some [expensive](price:high) resturants
- [Mid](price)

## intent:thankyou
- no. thanks
- thanks
- thank you!
- Thank you!

## synonym:4
- four

## synonym:Bangalore
- Bengaluru
- bengaluru

## synonym:Chennai
- Madras
- madras

## synonym:Delhi
- New Delhi
- delhi

## synonym:Hyderabad
- Secunderabad
- secunderabad

## synonym:Mumbai
- Bombay
- bombay

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- expensive

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:email
- ^[A-z0-9]+[A-z0-9._-]*@[A-z0-9._-]+\.[a-z]{2,}$

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
  data/cities.txt

## lookup:cuisine
- Chinese
- Mexican
- Italian
- American
- South Indian
- North Indian

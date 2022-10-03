import json
import urllib
import base64
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

token = "xoxb-2508506974611-4127154607221-dDGt1vT1SkPQH3vWHEdszNNW"
client = WebClient(token=token)

def app_home_opened(user_id, client):
	print("sending home screen")
	result = client.views_publish(
		user_id = user_id,
		view = {
			"type": "home",
			"blocks": [
		{
			"type": "actions",
			"elements": [
				{
					"type": "button",
					"text": {
						"type": "plain_text",
						"text": "Enter Score",
					},
					"value": "click_me_123",
					"action_id": "Score"
				}
			]
		}
	]
		})
	


def send_score_modal(trigger_id, client):
    print("sending score modal")
    result = client.views_open(
        trigger_id = trigger_id,
        view = {
            "type": "modal",
            "title" : {
            	"type": "plain_text",
            	"text" :"Enter Score"
            },
            "submit": {
            	"type" : 'plain_text',
            	"text" : "Send Score"
            	
            },
            "close":{
            	"type" : "plain_text",
            	"text": "Cancel"
            },
	        "blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Player A"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an Item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Eli Paul"
						},
						"value": "Eli"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ian Hay"
						},
						"value": "Ian"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Alex Swenson "
						},
						"value": "Alex"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ben Rush "
						},
						"value": "Ben"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ryan Lake "
						},
						"value": "Ryan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Charles Tipton"
						},
						"value": "Charles"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Jacob Domber "
						},
						"value": "Jacob"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Samuel Cotsarelis"
						},
						"value": "Samuel"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Matty Dubs "
						},
						"value": "Dubs"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Yoyo Tobunluepop "
						},
						"value": "Yoyo"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Harrison Seeley "
						},
						"value": "Harrison"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Vanel Joseph "
						},
						"value": "Vanel"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Peter Saliba "
						},
						"value": "King"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "George Haydock "
						},
						"value": "George"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Agustin Rodgriguez "
						},
						"value": "Agustin"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Santi Perfumo "
						},
						"value": "Santi"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Aidan Essig "
						},
						"value": "Aidan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Aleksis Viscokis "
						},
						"value": "Aleksis"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Callum Gow"
						},
						"value": "Callum"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ellan Ilfeld "
						},
						"value": "Ellan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Giovanni Hollis "
						},
						"value": "Giovani"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Hunter Brodie"
						},
						"value": "Hunter"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Jared Rudniki "
						},
						"value": "Jared"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Michael Duffy "
						},
						"value": "Michael"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Parth Sampat "
						},
						"value": "Parth"
					}
				],
				"action_id": "static_select-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Player B"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Eli Paul"
						},
						"value": "Eli"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ian Hay"
						},
						"value": "Ian"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Alex Swenson "
						},
						"value": "Alex"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ben Rush "
						},
						"value": "Ben"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ryan Lake "
						},
						"value": "Ryan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Charles Tipton"
						},
						"value": "Charles"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Jacob Domber "
						},
						"value": "Jacob"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Samuel Cotsarelis"
						},
						"value": "Samuel"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Matty Dubs "
						},
						"value": "Dubs"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Yoyo Tobunluepop "
						},
						"value": "Yoyo"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Harrison Seeley "
						},
						"value": "Harrison"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Vanel Joseph "
						},
						"value": "Vanel"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Peter Saliba "
						},
						"value": "King"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "George Haydock "
						},
						"value": "George"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Agustin Rodgriguez "
						},
						"value": "Agustin"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Santi Perfumo "
						},
						"value": "Santi"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Aidan Essig "
						},
						"value": "Aidan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Aleksis Viscokis "
						},
						"value": "Aleksis"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Callum Gow"
						},
						"value": "Callum"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Ellan Ilfeld "
						},
						"value": "Ellan"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Giovanni Hollis "
						},
						"value": "Giovani"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Hunter Brodie"
						},
						"value": "Hunter"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Jared Rudniki "
						},
						"value": "Jared"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Michael Duffy "
						},
						"value": "Michael"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Parth Sampat "
						},
						"value": "Parth"
					}
				],
				"action_id": "static_select-action"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Match Score"
			},
			"accessory": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "0-3"
						},
						"value": "B3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "1-3"
						},
						"value": "B4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "2-3"
						},
						"value": "B5"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3-0"
						},
						"value": "A3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3-1"
						},
						"value": "A4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3-2"
						},
						"value": "A5"
					}
				],
				"action_id": "static_select-action"
			}
		}
	]
}
                
        )



def lambda_handler(event, context):
	print(event)
	parsed = ''
	if event['isBase64Encoded'] == True:
		parsed = base64.b64decode(event['body'])
		parsed = parsed.decode('utf-8')
	else:
		parsed = event['body']
    
	parsed = urllib.parse.unquote(parsed)         
	parsed = json.loads(parsed)
    
	print(parsed)
	print(parsed['event']['type'])
	user_id = parsed['event']['user']
    
	if parsed['event']['type'] == "app_home_opened":
		app_home_opened(user_id, client)
        
    
	return {
        'statusCode' : 200,
        'body': "yewwww"
    }
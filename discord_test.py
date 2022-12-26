import requests
import json
import random
import time


def get_context():
    context_list = [
        "/imagine prompt genetic, sticker art design, kawaii illustration, white background",
    ]
    text = random.choice(context_list)
    return text


def chat(chanel_list,authorization_list):
    for authorization in authorization_list:
        header = {
            "Authorization": authorization,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        }
        for chanel_id in chanel_list:
            msg_info = {
                "type":2,
                "application_id":"936929561302675456",
                "guild_id":"662267976984297473",
                "channel_id": chanel_id,
                "session_id":"142fd5924f9a6ca0604b7c9cfebca05f",
                "data":{
                    "version":"987795925764280356",
                    "id":"972289487818334209",
                    "name":"info",
                    "type":1,
                    "options":[],
                    "application_command":{
                        "id":"972289487818334209",
                        "application_id":"936929561302675456",
                        "version":"987795925764280356",
                        "type":1,
                        "name":"info",
                        "description":"View information about your profile."},"attachments":[]},
                "nonce":"82329451214{}33232234".format(random.randrange(0, 1000))}
            
            msg_help = {
                "type":2,
                "application_id":"936929561302675456",
                "guild_id":"662267976984297473",
                "channel_id": chanel_id,
                "session_id":"142fd5924f9a6ca0604b7c9cfebca05f",
                "data":{
                    "version":"987795925764280355",
                    "id":"941673664900898876",
                    "name":"help",
                    "type":1,
                    "options":[],
                    "application_command":{
                        "id":"941673664900898876",
                        "application_id":"936929561302675456",
                        "version":"987795925764280355",
                        "type":1,
                        "name":"help",
                        },"attachments":[]},
                "nonce":"82329451214{}33232234".format(random.randrange(0, 1000))}
                
            msg_imagine = {
                "type":2,
                "application_id":"936929561302675456",
                "guild_id":"662267976984297473",
                "channel_id": chanel_id,
                "session_id":"142fd5924f9a6ca0604b7c9cfebca05f",
                "data":{
                    "version":"994261739745050686",
                    "id":"938956540159881230",
                    "name":"imagine",
                    "type":1,
                    "options":[{
                        "type":3,
                        "name":"prompt",
                        "value":"eyeball, sticker art design, kawaii illustration, white background"}],
                    "application_command":{
                        "id":"938956540159881230",
                        "application_id":"936929561302675456",
                        "version":"994261739745050686",
                        "default_permission":"true",
                        "default_member_permissions":"null",
                        "type":1,
                        "nsfw":"false",
                        "name":"imagine",
                        "description":"There are endless possibilities...",
                        "dm_permission":"true",
                        "options":[{
                            "type":3,
                            "name":"prompt",
                            "description":"The prompt to imagine",
                            "required":"true"}]},
                    "attachments":[]},
                "nonce":"82329451214{}33232234".format(random.randrange(0, 1000))}
            
            #url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
            url =  "https://discord.com/api/v9/interactions"
            try:
                res = requests.post(url=url, headers=header, data=json.dumps(msg_imagine))
                print(res.content)
            except:
                pass
            continue
        time.sleep(random.randrange(1, 3))


if __name__ == "__main__":
    chanel_list = ["989739763957391370"]
    authorization_list = ["MTA1MjU3NTI2NDc4MzIxNjY4MQ.Gl3Z8K.ndJKKWPxhlHk0hxwqmwg69KjZiikIrqZ8Zj5t4"]
    chat(chanel_list,authorization_list)    

    '''
    while True:
        try:
            chat(chanel_list,authorization_list)
            sleeptime = random.randrange(5, 10)
            time.sleep(sleeptime)
        except:
            break
    '''


import os
import telegram
import asyncio
import asana

async def main():

    # Note: Replace this value with your own personal access token
    personal_access_token_asana = os.environ["1/1203489910254785:ab0204bf2da01b02a1dc8db6058e521f"]

    # Construct an Asana client
    client = asana.Client.access_token(personal_access_token_asana)

    # Get your user info
    me = client.users.me()

    workspace_id = me['workspaces'][0]['gid']
    tasks = client.tasks.find_all(workspace=workspace_id, completed_since='now', assignee=me['gid'])

    ls = []

    for t in tasks:
        ls.append(t['name'])

    bot = telegram.Bot(os.environ["TELEGRAM_TOKEN"])
    async with bot:
        await bot.send_message(text='\n'.join(ls), chat_id=319846586)
    return "okay"


# def telegram_bot(request):
#     return asyncio.run(main())



# def telegram_bot(request):
#     bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
#     if request.method == "POST":
#         update = telegram.Update.de_json(request.get_json(force=True), bot)
#         chat_id = update.message.chat.id
#         # Reply with the same message
#         bot.sendMessage(chat_id=chat_id, text=update.message.text)
#         return "inside"
#     return "okay"
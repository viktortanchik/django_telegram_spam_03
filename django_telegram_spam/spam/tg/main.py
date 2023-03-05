from pyrogram import Client, filters

# api_id = 13729328
# api_hash = "9344d5d46317f096d8bde457e1a9bf53"


#app = Client("6283834705843", api_id=api_id, api_hash=api_hash)
api_id = 16526653
api_hash = "918872691e0a8ea8335cce787546eb3d"
#app = Client("6285776362281", api_id=api_id, api_hash=api_hash)#app.send_message('@viktortanchik','hi')
app = Client("6285298448807", api_id=api_id, api_hash=api_hash)#app.send_message('@viktortanchik','hi')
app.start()
app.send_message('@viktortanchik', 'hi')








#
# @app.on_message()
# async def echo(filters, message):
#     print(message)
# # @app.on_message(filters.text & filters.private)
# # async def echo(client, message):
# #     print(f'client:{client}')
# #     print(f'message:{message}')
# #     await message.reply(message.text)
# #
#
# app.run()
# #
# async def main():
#     async with Client("6283834705843", api_id, api_hash) as app:
#         await app.send_message("me", "Greetings from **Pyrogram**!")
#
#
# asyncio.run(main())

#
# @app.on_message()
# async def echo(filters, message):
#     await app.send_message('@viktortanchik', 'hi')
#     # print(f'client:{client}')
#     # print(f'message:{message}')
#
#     # if message.chat.id ==-680802628:
#     if message.chat.id == -707863092:
#         # print(f'client:{client}')
#         # print(f'message:{message}')
#         # print(f'message:{message.text}\nreactions:{message.reactions}')
#         mess = ''
#         try:
#
#             for i in message.reactions:
#                 print('emoji:', i.emoji)
#                 print('count:', i.count)
#                 print('chosen:', i.chosen)
#             print(f'message_id:{message.message_id}')
#             print(f'from_user.first_name:{message.from_user.first_name}')
#             print(f'from_user.username:{message.from_user.username}')
#             print(f'from_user.id:{message.from_user.id}')
#             print('###########################')
#         except TypeError:
#             pass
#

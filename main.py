from telebot import TeleBot

bot = TeleBot('5004212111:AAEreNUjOybQ0Yx8HaHe4Gx-z0HMs0BSgWk')
bot.remove_webhook()


CONTENT_TYPES = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]


@bot.channel_post_handler(content_types=CONTENT_TYPES)
def getChannelMessage(message):
    print("https://t.me/" + str(message.chat.username) + "/" + str(message.id))


@bot.message_handler(content_types=CONTENT_TYPES)
def getMessage(message):
    print("https://t.me/" + str(message.chat.username) + "/" + str(message.id))


bot.polling(none_stop=True)

import telebot
import qrcode

# Enter bot token from Bot Father
bot = telebot.TeleBot('<<bot_token>>')


@bot.message_handler()
def get_ip_info(message):

    # Get i/p text From Bot
    qr = message.text.strip()

    # Generat Qr Code & Save
    img = qrcode.make(qr)
    img.save('Qr Code.png')

    # Send Qr Code
    bot.send_photo(chat_id=message.from_user.id,
                   photo=open('Qr Code.png', 'rb'), caption=qr)
    bot.send_document(chat_id=message.from_user.id,
                      document=open('Qr Code.png', 'rb'), caption=qr)


while True:
    bot.polling()

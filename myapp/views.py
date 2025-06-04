from django.shortcuts import render
from asgiref.sync import async_to_sync
from telegram import Bot
from telegram.constants import ParseMode
from datetime import datetime
from django.contrib import messages

TELEGRAM_BOT_TOKEN = '7711402613:AAEv99JIVy42cFGR2cPjt9iBC5gaOyC_moE'
TELEGRAM_CHAT_ID = 7172540121

def index(request):
    if request.method == 'POST':
        input1 = request.POST.get('input1')  # kelish
        input2 = request.POST.get('input2')  # ketish
        phone = request.POST.get('step')
        if input1 and input2 and phone:
            try:
                # input sanalarni YYYY-MM-DD deb qabul qilib, DD.MM.YYYY formatiga o‘tkazamiz
                kelish_sana = datetime.strptime(input1, '%Y-%m-%d').strftime('%d.%m.%Y')
                ketish_sana = datetime.strptime(input2, '%Y-%m-%d').strftime('%d.%m.%Y')
            except ValueError:
                kelish_sana = input1
                ketish_sana = input2

            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            message = f"""
📅 *Kelish kuni:* {kelish_sana}
📅 *Ketish kuni:* {ketish_sana}
📞 *Telefon raqami:* {phone}
🕒 *Yuborilgan vaqt:* {now}
"""
            bot = Bot(token=TELEGRAM_BOT_TOKEN)
            try:
                async_to_sync(bot.send_message)(
                    chat_id=TELEGRAM_CHAT_ID,
                    text=message,
                    parse_mode=ParseMode.MARKDOWN
                )
     
                messages.add_message(request, messages.INFO, "Hello world.")
            except Exception as e:
                print("Xatolik yuz berdi:", e)
    return render(request, 'index.html')

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, MessageHandler, Filters

TOKEN = "6507673545:AAFGvHCZYQ5lHPKoYGh41lKbnrtLpk4ZyTo"

def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Menu Onboarding", callback_data='onboarding')],
        [InlineKeyboardButton("Tutor Regular", callback_data='regular')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query:
        query = update.callback_query
        query.edit_message_text(text='Pilih salah satu menu:', reply_markup=reply_markup)
    else:
        update.message.reply_text('Pilih salah satu menu:', reply_markup=reply_markup)

def handle_message(update: Update, context):
    text = update.message.text.lower()

    if "apa itu kelas mentoring?" in text:
        update.message.reply_text('Apa itu kelas Mentoring? 🤔\n\nBuat yang belum tahu, mentoring itu apa. Mentoring sama aja kayak kelas catchup 1 on 1. Bedanya mentoring lebih fokus untuk:\n\n- Review materi selama ini 📚\n- Banyakan ngobrol dengan anak 🗣️\n- Showcase project2 kedepannya 🖥️\n- Bertanya kendalanya apa selama dikelas ❓\n\nOutput mentoring: supaya anak mau lanjut belajar di algorithmics 👨‍💻')
    elif "apa itu catchup class?" in text or "apa itu kelas catchup" in text:
        update.message.reply_text('Apa itu catchup class? 🧐\n\nCatch up atau kelas untuk mengejar pelajaran yang tertinggal di group tersebut secara gratis dengan tutor masing-masing kelas secara private. Kelas catch up diberikan free 1x jika siswa melewatkan kelas 2-3x secara beruntun. Jika siswa kedepannya melewatkan 2 kelas secara beruntun maka siswa akan dikenakan biaya sebesar 90.000 untuk satu pertemuan. 💰')
    elif 'platform lemot?' in text or 'website algo down?' in text:
        update.message.reply_text('Jika platform lemot atau website Algorithmics sedang down, ikuti langkah berikut:\n\n'
                                  '1. Buka https://speedtest.net dan cek berapa speednya, jika di bawah 10Mbps ganti pakai hotspot handphone. Jika masih lambat 🔽\n'
                                  '2. Ganti link https://learn.alg.academy atau https://learn.algoritmika.org/ \n'
                                  '3. Jika masih bermasalah, download 1.1.1.1 di https://1.1.1.1/ lalu aktifkan new DNS atau VPN.')
    elif 'download aplikasi mac?' in text or 'tutorial download aplikasi macbook?' in text:
        update.message.reply_text('Download app di Mac 💻: Tutorial Video https://www.youtube.com/watch?v=OWaaw4O6NCc&ab_channel=virgiangalang 🎥')
        
    elif 'video untuk kelas pertama?' in text or 'video untuk parents sebelum kelas pertama?' in text or 'video sebelum kelas pertama?' in text:
        update.message.reply_text('Cara buka website Algorithmics & masuk online class 🖥️: Video Tutorial https://www.youtube.com/watch?v=OWEVfB6xAew&ab_channel=virgiangalang 🎥')

    elif 'link download scratch jr?' in text or 'link download scratchjr?' in text:
        update.message.reply_text('🔗 Download Scratch Jr https://jfo8000.github.io/ScratchJr-Desktop/')

    elif 'website tutorfaq?' in text or 'tutor faq?' in text:
        update.message.reply_text('📌 [FAQ Tutor](https://grateful-forest-e14.notion.site/FAQ-Tutor-CS-ISM-569b4f4bae804e679a64f6d3fbf318be)')

    elif 'website operasional?' in text or 'web operasional?' in text:
        update.message.reply_text('📌 [Web Operasional](https://bit.ly/linkoperational)')

    elif 'website quality?' in text or 'web quality?' in text:
        update.message.reply_text('📌 [Web Quality](https://lynk.id/tutorquality)')

    elif 'video instruksi?' in text or 'link video instruksi?' in text:
        update.message.reply_text('🎥 [Video Instruksi](https://www.youtube.com/playlist?list=PLu0GqhuukgN2pux9jTk8qfJxcOOwdHw0d)')

    elif 'tutor training dashboard?' in text or 'dashboard training?' in text:
        update.message.reply_text('👨‍🏫 [Dashboard Training](https://docs.google.com/spreadsheets/d/1BbYeF1_hNqVhy2ivhcKICXnOqHGZilDOarubCp0HgAI/edit#gid=0)')

        

def onboarding(update: Update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Tutor Regulation and SOP", url="https://docs.google.com/document/d/1-EuznHtmqus_BOyFvki11CGnDWBDfLCPzbbRof3Ik0E/edit#heading=h.gjdgxs")],
        [InlineKeyboardButton("Tutor CV", url="https://drive.google.com/drive/u/0/folders/1wa_oJSx01uY-bqJ2_Otc6gNCv6zFD8OD")],
        [InlineKeyboardButton("Your Available Schedule", url="https://docs.google.com/spreadsheets/d/1F5VQdXA0L9cLN1jnl7mTv2-EjW6GXZ5yABQNtvynOFM/edit#gid=383750057")],
        [InlineKeyboardButton("Onboarding Instruction", url="https://docs.google.com/document/d/13sgw4HG8J64Ukd9-VOZP1wr2VZyBQuRsmn-lQznIrws/edit")],
        [InlineKeyboardButton("Upcoming and Booking Schedule", url="https://docs.google.com/spreadsheets/d/1KOXz1icbtFYoHVNAHep9TAmi2lAj9yTbQahBxrr2FTo/edit#gid=0")],
        [InlineKeyboardButton("Onboarding To-do-list", url="https://docs.google.com/spreadsheets/d/1paTXgks4Vkdlc7OYpt05min0SzQ_tOH4wQXXHHNOmVo/edit#gid=0")],
        [InlineKeyboardButton("Kembali", callback_data='start')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Pilih salah satu link:", reply_markup=reply_markup)

def regular(update: Update, context):
    query = update.callback_query
    query.answer()

    keyboard = [
        [InlineKeyboardButton("Tutor Training Dashboard", url="https://docs.google.com/spreadsheets/d/1BbYeF1_hNqVhy2ivhcKICXnOqHGZilDOarubCp0HgAI/edit#gid=0")],
        [InlineKeyboardButton("Tutor Assessment", url="https://forms.gle/69gcqvh8k8y1RBiR6")],
        [InlineKeyboardButton("Tutor Training Schedule", url="https://docs.google.com/document/d/1AXvcEfHRmoEnhp7qacZi-lZ3-unXfCy8-AabK_M9ulY/edit?hl=ru")],
        [InlineKeyboardButton("Algorithmics Intruction Video", url="https://www.youtube.com/playlist?list=PLu0GqhuukgN2pux9jTk8qfJxcOOwdHw0d")],
        [InlineKeyboardButton("Kembali", callback_data='start')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text="Pilih salah satu link:", reply_markup=reply_markup)

def back_to_start(update: Update, context):
    start(update, context)

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(onboarding, pattern='^' + str('onboarding') + '$'))
    dp.add_handler(CallbackQueryHandler(regular, pattern='^' + str('regular') + '$'))
    dp.add_handler(CallbackQueryHandler(back_to_start, pattern='^' + str('start') + '$'))
    
    # Handler untuk pesan teks
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

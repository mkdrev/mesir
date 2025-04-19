from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os
import logging
from threading import Thread
from flask import Flask

# ===== SETUP LOGGING =====
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ===== KEEP ALIVE SERVER =====
web_app = Flask(__name__)

@web_app.route('/')
def home():
    return "Bot MESIR77 Aktif dan Berjalan!"

def run_flask():
    web_app.run(host='0.0.0.0', port=8080)

Thread(target=run_flask, daemon=True).start()

# ===== BOT CONFIGURATION =====
TOKEN = os.environ.get("BOT_TOKEN")
BASE_URL = "https://jali.me/Mesir77"
LIVECHAT_URL = "https://direct.lc.chat/17801934/"

# ===== COMMAND HANDLERS =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        chat_id = update.effective_chat.id

        # Send welcome message with photo
        await context.bot.send_photo(
            chat_id=chat_id,
            photo="https://i.pinimg.com/736x/56/7e/30/567e30d5dc7bd326c40c1d77335b010c.jpg",
            caption=f"Halo {user.first_name}, selamat datang di *MESIR77*! 🎰\n\n"
                    "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
            parse_mode="Markdown"
        )

        # Create interactive menu
        keyboard = [
            [InlineKeyboardButton("🎮 MAIN SEKARANG", web_app=WebAppInfo(url=BASE_URL))],
            [InlineKeyboardButton("📊 LIHAT RTP HARI INI", web_app=WebAppInfo(url=f"{BASE_URL}#rtp"))],
            [InlineKeyboardButton("🎁 PROMO TERBARU", web_app=WebAppInfo(url=f"{BASE_URL}#promo"))],
            [InlineKeyboardButton("📱 INFO KONTAK", web_app=WebAppInfo(url=BASE_URL))],
            [InlineKeyboardButton("💬 BANTUAN CS 24JAM", web_app=WebAppInfo(url=LIVECHAT_URL))],
        ]
        
        await context.bot.send_message(
            chat_id=chat_id,
            text="👇 *PILIH MENU DI BAWAH* 👇",
            reply_markup=InlineKeyboardMarkup(keyboard),
            parse_mode="Markdown"
        )

    except Exception as e:
        logger.error(f"Start command error: {e}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="⚠️ Maaf, terjadi gangguan. Silakan coba lagi nanti."
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ *Bantuan MESIR77 Bot*\n\n"
        "/start - Tampilkan menu utama\n"
        "/help - Tampilkan pesan bantuan ini\n\n"
        "Butuh bantuan lebih? Hubungi CS kami 24 jam!",
        parse_mode="Markdown"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if text in ['halo', 'hai', 'hi', 'hello']:
        await update.message.reply_text(
            f"Halo {update.effective_user.first_name}! 🎰\n"
            "Ketik /start untuk membuka menu MESIR77"
        )

# ===== MAIN APPLICATION =====
def main():
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # Add handlers
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
        
        logger.info("Starting MESIR77 Bot...")
        print("🔥 [BOT MESIR77 AKTIF DAN SIAP MELAYANI!] 🔥")
        
        app.run_polling(drop_pending_updates=True)
        
    except Exception as e:
        logger.error(f"Bot startup failed: {e}")
        print(f"❌ ERROR: {e}")

if __name__ == '__main__':
    main()

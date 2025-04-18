from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TOKEN = os.environ.get("BOT_TOKEN")  # Gunakan nama env yang aman dan jelas
app = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    await context.bot.send_photo(
        chat_id=chat_id,
        photo="https://i.pinimg.com/736x/56/7e/30/567e30d5dc7bd326c40c1d77335b010c.jpg",
        caption="Halo Ketua, selamat datang di *MESIR77!*\n\n"
                "Pilih menu di bawah untuk mulai bermain atau cek fitur lainnya.",
        parse_mode="Markdown"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 PLAY", web_app=WebAppInfo(url="https://jali.me/Mesir77"))],
        [InlineKeyboardButton("🎰 RTP GACOR", web_app=WebAppInfo(url="https://jali.me/Mesir77"))],
        [InlineKeyboardButton("🎁 PROMOTION", web_app=WebAppInfo(url="https://jali.me/Mesir77"))],
        [InlineKeyboardButton("📲 SOCIAL MEDIA", web_app=WebAppInfo(url="https://jali.me/Mesir77"))],
        [InlineKeyboardButton("💬 LIVECHAT", web_app=WebAppInfo(url="https://direct.lc.chat/17801934/"))],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=chat_id,
        text="Pilih salah satu opsi berikut:",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    print("[✅] Bot MESIR77 is running...")
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

import os
from http.server import BaseHTTPRequestHandler
import json
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN) if TOKEN else None

async def start(update, context):
    user_name = update.effective_user.first_name
    await update.message.reply_text(f"Hello {user_name}! 👋 Welcome to your Vercel-hosted serverless bot.")

def get_application():
    application = Application.builder().token(TOKEN).updater(None).build()
    application.add_handler(CommandHandler("start", start))
    return application

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length)
            json_data = json.loads(post_data.decode('utf-8'))

            import asyncio
            app = get_application()
            
            async def process():
                await app.initialize()
                update = Update.de_json(json_data, bot)
                await app.process_update(update)

            asyncio.run(process())

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'OK')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Telegram Bot is running on Vercel Serverless Functions!')

# Telegram Notify - Vercel Serverless

1. Repository’yi GitHub’a push et
2. Vercel’a bağla ve deploy et
3. Environment Variables:
   - BOT_TOKEN = Telegram Bot token
   - CHANNEL_ID = Kanal ID (örn: @onual_firsat)
   - NTFY_TOPIC = ntfy topic (örn: ulusehir)
4. Deploy tamam, URL: https://<proje-adı>.vercel.app/api/check
5. URL’yi cron-job veya Vercel Scheduler ile 1 dakikada bir tetikleyin.

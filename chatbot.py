import telebot
import requests

CHAVE = '6685830631:AAFDFJGsP4UvU-MW8I9_z8NQC_gKYdReeZQ'

bot = telebot.TeleBot(CHAVE)

def horospoco_api(signo):
  url = f"https://horoscope-api.p.rapidapi.com/pt/{signo}"

  headers = {
    "X-RapidAPI-Key": "2f455d724bmsh069c001b3423040p101288jsnc71b59ac6feb",
    "X-RapidAPI-Host": "horoscope-api.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers)

  return response.json()


@bot.message_handler()
def boas_vindas(msg):
  if(msg.text == "/horospoco"):
    signo(msg)
  else:
    bot.reply_to(msg, "Olá, eu sou o Chat do Luiz (o grande). Estou aqui para ajudar com o horóspoco \o/")


def signo(msg):
  signos = "Qual é seu Signo? 🔮\nEscolha um:\n*♈️ Aries*\n*♉️ Touro*\n*♊️ Gemeos*\n*♋️ Cancer*\n*♌️ Leao*\n*♍️ Virgem*\n*♎️ Libra*\n*♏️ Escorpiao*\n*♐️ Sagitario*\n*♑️ Capricornio*\n*♒️ Aquario*\n*♓️ Peixes*"
  enviar_msg = bot.send_message(msg.chat.id, signos, parse_mode="Markdown")
  bot.register_next_step_handler(enviar_msg, pegar_horoscopo_api)


def pegar_horoscopo_api(msg):
  signo = msg.text
  resposta = horospoco_api(signo)
  print(resposta)

  titulo = resposta['title']
  data = resposta['date']
  texto = resposta['text']

  horospoco_mensagem = f'*{titulo}*\n\n*Signo:* {signo}\n*Dia:* {data}\n\n{texto}'

  bot.send_message(msg.chat.id, "Aqui está o seu horóspoco!")
  bot.send_message(msg.chat.id, horospoco_mensagem, parse_mode="Markdown")

bot.infinity_polling()

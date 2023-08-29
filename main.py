# Author: João Pedro Campos
# Contact: ocamposfaria@gmail.com

# VERSION 1.1.2

#  #  #  #  #  #  #  #  IMPORTING LIBRARIES

# CMD ["pip3 install torch torchvision torchaudio"]
# from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
import discord
from discord.ext import tasks
import pytz
import datetime
import time
import yfinance as yf
import random
import platform
from dateutil.relativedelta import relativedelta

#  #  #  #  #  #  #  #  IMPORTING DATA AND SETTING STUFF UP

# setup discord
f = open('data/my_secret.txt')
my_secret = f.read()
f.close()

intents = discord.Intents.default() 
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)

CHANNEL_ID = 746537426243289152 # para tomar os meios de produção
# CHANNEL_ID = 984915233644642304 # para testes

# setup smart answers

# tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
# model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")

# setup porta dos fundos
f = open('data/porta_dos_fundos.txt') 
porta = f.read()
f.close()
porta = eval(porta)

# setup random
f = open('data/data_random.txt') 
fato = f.read()
f.close()
fato = eval(fato)
pessoa = ['o arthu', 'o danieu', 'o teteu', 'o juau', 'o gabireu', 'o totow']

# setup timezone
if platform.system() == 'Linux':
	time.tzset()  # set timezone for Linux
elif platform.system() == 'Windows':
	pass

# setup roleta russa
camara = 6 

# setup placar
placar = {}

def formatar_placar(placar):
	if placar == {}:
		return 'ninguém morreu ainda'
	else:
		decrescente = sorted(placar.items(), key=lambda x: x[1], reverse=True)
		return '```placar de mortes: \n' + "\n".join(f"{jogador}: {pontos}" for jogador, pontos in decrescente) + '```'

# setup nicholas cagezinho
nicolas_cage = 0
apenas_hora = datetime.datetime.now(pytz.timezone('Brazil/East')).strftime("%H")

#  #  #  #  #  #  #  #  EVENTS

@client.event
async def on_ready():
	channel = client.get_channel(CHANNEL_ID)
	print('We have logged in as {0.user}'.format(client))
	activity = discord.Activity(type=discord.ActivityType.listening, name="!comandos")
	send.start() # start loop when bot starts
	await client.change_presence(status=discord.Status.online, activity=activity)
	# await channel.send("i'm back bitches")
	# await channel.send("@ocamposfaria não esqueça de executar `fly scale count 1`")

@client.event
async def on_message(message):

# comandos
		if message.content.startswith('!comandos'):
				await message.channel.send(
			"""alguns comandos para você experimentar:

!oi juau robô
!perfil
!fala pessoal
!loteria
!porta dos fundos
!que vibe
!random
!adicionar [predicado]
!como jogar roleta russa 
!roleta russa
!placar
!perfil
!preço [ação]
!variação [ação] [qtde meses] meses

ou use !patch notes para ver as últimas atualizações""")

# respostas inteligentes
		if message.content.startswith('!smart'):
				# text = " ".join(message.content.split()[1:])
				# input = tokenizer(text, return_tensors="pt")
				# output = model.generate(**input)
				# output_treated = tokenizer.decode(output[0]).replace('<s>', '').replace('</s>', '').lower()
				# await message.channel.send(output_treated)
				await message.channel.send('minhas respostas inteligentes estão desligadas no momento.')

# saudações
		if message.content.startswith('!oi juau robô'):
				await message.channel.send(random.choice(['fala meu bom', 'olá otário', 'fala aí arrombado', 'coé carai', 'contigo eu não falo não', 'oi amigo']))

# indescritível
		if message.content.startswith('!que vibe'):
				await message.channel.send(
			'https://www.youtube.com/watch?v=R8gLxW3QFXY')

# fala pessoal
		if message.content.startswith('!fala pessoal'):
				await message.channel.send('piroca chegou')

# andréia
		for i in ['andrea', 'Andrea', 'andréa', 'Andréa']:
			if i in message.content:
				await message.reply('CUIDADO', mention_author=False)

# adicionar fato aleatório
		if message.content.startswith('!adicionar'):
				global fato
				mensagem = message.content
				fato.append(mensagem[11:])
				f = open('data/data_random.txt', 'w')
				f.write(str(fato))
				f.close()
				await message.channel.send('novo fato adicionado \'' + mensagem[11:] + '\'')

# perfil
		if message.content.startswith('!perfil'):
			await message.channel.send(file=discord.File('pics/robot_juau.png'))
			await message.channel.send('sim, esse sou eu')

# enviar fato aleatório
		if message.content.startswith('!random'):
				await message.channel.send(
						str(random.choice(pessoa)) + ' ' + str(random.choice(fato)))

# nicholas cagezinho
		if apenas_hora == '06':
				global nicolas_cage
				if nicolas_cage == 0:
						nicolas_cage = nicolas_cage + 1
						await message.channel.send(
				'https://www.youtube.com/watch?v=m3J0r--l-9w')
						await message.reply(
				'não, e olha o naipezera do moleque essa hora ó, hã he he he, seis hora da manhã e ele todo nicolas cagezinho já hã, turugudum tcha tcha, turugu tcha  turugudum tcha tcha')
						
# loteria 
		if message.content.startswith('!loteria'):
			x = random.random()
			if x > 0.0000000199:
				await message.channel.send('você não ganhou na loteria')
				
			else:
				await message.channel.send(
				'PQP VC GANHOU NA LOTERIA NÃO ACREDITO!!!!!!!!!!!!!!!!!!!!!!!!!!!')
				
# variação de ação
		if message.content.startswith('!variação '):
			try:
				lista = message.content.split()
				meses = int(lista[2])
				açao = lista[1]

				hoje = datetime.datetime.now(pytz.timezone('Brazil/East'))
				if datetime.datetime.weekday(hoje) == 5:
					hoje = hoje + relativedelta(days=-1)
				if datetime.datetime.weekday(hoje) == 6:
					hoje = hoje + relativedelta(days=-2)

				periodo = datetime.datetime.now(pytz.timezone('Brazil/East')) - relativedelta(months=meses)
				if datetime.datetime.weekday(periodo) == 5:
					periodo = periodo + relativedelta(days=2)
				if datetime.datetime.weekday(periodo) == 6:
					periodo = periodo + relativedelta(days=1)
					
				periodo_br = periodo.strftime("%d/%m/%y")  
				periodo_yf = periodo.strftime("%Y-%m-%d")
				hoje_yf = hoje.strftime("%Y-%m-%d")

				bovespa = yf.download(açao, start=periodo_yf, end=hoje_yf, progress=False)
				percentual = ((bovespa['Adj Close'][-1] / bovespa['Adj Close'][0]) - 1)
				percentual = "{:.1%}".format(percentual)

				try:
					await message.channel.send(str(açao) + ' variou ' + str(percentual) + ' entre seu fechamento ajustado em ' + str(periodo_br) + ' e agora')
				except Exception as e:
					print(e)
				# except:
				# 	await message.channel.send('ação não encontrada. consulte: <https://finance.yahoo.com>')
				# 	await message.channel.send('mentira se pa deu ruim')
		
			except Exception as e:
				print(e)		
			# except:
			#	await message.channel.send('acho que você não passou o comando corretamente. tente novamente')

# preço de ação
		if message.content.startswith('!preço'):
			try:
				lista = message.content.split()
				açao = lista[1]
				hoje = datetime.datetime.now(pytz.timezone('Brazil/East'))
				hoje_formatado = hoje.strftime("%Y-%m-%d")
				duas_semanas_atras = hoje - datetime.timedelta(days=14)
				duas_semanas_atras_formatado = duas_semanas_atras.strftime("%Y-%m-%d")

				bovespa = yf.download(açao, start=duas_semanas_atras_formatado, end=hoje_formatado, progress=False)
				preço = bovespa['Adj Close'].iloc[-1] # pega o valor mais recente disponível
				preço = "{:.5}".format(preço)
				await message.channel.send(str(açao) + ' tá valendo USD ' + str(preço) + ' nesse momento ou em sua última cotação')

			except Exception as e:
				print(e)
				await message.channel.send('ação não encontrada. consulte: <https://finance.yahoo.com>')

# porta dos fundos		
		if message.content == '!porta dos fundos':
			await message.channel.send(str(random.choice(porta)))
	
# roleta russa
		if message.content.startswith('!roleta russa'):
				global camara
				gatilho = random.random()
				prob = 1 / (camara)

				if gatilho > prob:
						await message.channel.send(
				str(message.author.name) + ' não morreu')
						await message.channel.send('agora o revólver só possui {} câmaras livre(s)'.format(camara - 1))
						camara = camara - 1
				else:
						await message.channel.send(str(message.author.name) + ' morreu :exploding_head: :gun: ')
						if str(message.author.name) in placar:
							placar[str(message.author.name)] += 1
						else:
							placar[str(message.author.name)] = 1
						camara = 6
						await message.channel.send(formatar_placar(placar))

# placar
		if message.content.startswith('!placar'):
				await message.channel.send(formatar_placar(placar))
				
# como jogar roleta russa
		if message.content.startswith('!como jogar roleta russa'):
				await message.channel.send('use o comando !roleta russa para rodar a câmara de um revólver e dar um tiro na sua cabeça. o revólver tem uma só bala e seis câmaras. se você não morrer, não é mais sua vez! para ver o placar com o histórico de mortes, !placar')

# patch notes
		if message.content.startswith('!patch notes'):
				await message.channel.send(
			'...')
				await message.channel.send(
			'>> substituição do pandas datareader por yfinance nos comandos de ações\n>> adicionado placar da roleta russa, etc. (outros minors)')
				await message.channel.send(
			'\n \n----> buy me a coffee! :coffee: ')


# @client.event
# async def on_message_delete(message):
#        await message.channel.send('apagou a mensagem né safado? <@' + str(message.author.id) + '>')

#  #  #  #  #  #  #  #  LOOP


@tasks.loop(seconds=60)
async def send():
	channel = client.get_channel(CHANNEL_ID)
	dia_semana = datetime.datetime.now(pytz.timezone('Brazil/East')).weekday()
	hora = datetime.datetime.now(pytz.timezone('Brazil/East')).strftime("%H:%M")
	data = datetime.datetime.now(pytz.timezone('Brazil/East')).strftime("%d/%m")
	
	try:
		if dia_semana == 2 and hora == '16:00':
			await channel.send(
					'https://www.youtube.com/watch?v=Tmy5JtL58dE')
			await channel.send(
					'são quatro horas da tarde de uma quarta-feira, não é?\nsemana praticamente encerrada @everyone')
			
		if dia_semana == 4 and hora == '08:30':
			await channel.send(
					'https://www.youtube.com/watch?v=8GX9--xhf_A')
			await channel.send(
					'GRAÇAS A DEUS É SEXTA-FEIRA HEIN @everyone')

		if data == '16/03' and hora == '08:00': #gabrieu
			await channel.send(file=discord.File('pics/gabrieu.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '27/08' and hora == '08:00': #arthu
			await channel.send(file=discord.File('pics/arthu.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '06/07' and hora == '08:00': #teteu
			await channel.send(file=discord.File('pics/teteu.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '13/01' and hora == '08:00': #heitor
			await channel.send(file=discord.File('pics/heitor.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '22/09' and hora == '08:00': #juau
			await channel.send(file=discord.File('pics/juau.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '11/04' and hora == '08:00': #daniel braga
			await channel.send(file=discord.File('pics/danieu braga.jpg'))
			await channel.send(
				'aniversário hoje!')

		if data == '03/08' and hora == '08:00': #danieu
			await channel.send(file=discord.File('pics/danieu.jpg'))
			await channel.send(
				'aniversário hoje!')
		
		else:
			print(f'{str(hora)} -> não há eventos no momento')
		
	except Exception as e:
		print(e)
		print(f'{str(hora)} -> erro inesperado!')

#  #  #  #  #  #  #  #  BE ALIVE 

client.run(my_secret)
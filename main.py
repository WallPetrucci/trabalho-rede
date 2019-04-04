"""
Gustavo Longo - 95281
Higor Freitas de Oliveira - 93957
Lucas Paschoal - 88376
Wallace Petrucci Neves - 95441
"""

class Camada:
	def __init__(self):
		self.set_funcionalidade(self.get_funcionalidade())

	def get_funcionalidade(self):
		return "Classe Base"

	def set_funcionalidade(self,func):
		self.funcionalidade = func

class Fisica(Camada):
	def __init__(self, status = False, dado = False):
		self.set_dado(dado)
		self.set_status(status)
		self.set_funcionalidade("Fisica")

	def set_dado(self, dado):
		self.dado = dado

	def set_status(self, status):
		if status is not False:
			self.status = status
			self.enlace = Enlace(mac="teste", dado=self.get_dado())
		else:			
			if self.enlace:
				del self.enlace
			self.status = False

	def get_status(self):
		return self.status

	def get_enlace(self):
		return self.enlace

	def get_dado(self):
		return self.dado


class Enlace(Camada):
	def __init__(self, mac, dado):
		self.set_mac(mac)
		self.set_dado(dado)
		self.rede = Rede(dado=self.get_dado() )
		self.set_funcionalidade("Enlace")

	def set_mac(self, mac):
		self.mac = mac

	def set_dado(self, dado):
		self.dado = dado

	def get_dado(self):
		return self.dado

	def get_mac(self):	
		return self.mac
		
class Rede(Camada):
	def __init__(self, dado, ip_destino = '127.0.0.1'):
		self.set_dado(dado)
		self.set_ip_destino(ip_destino)
		self.transporte = Transporte(self.get_ip_destino(), self.get_dado())
		self.set_funcionalidade("Rede")

	def set_dado(self, dado):
		self.dado = dado

	def set_ip_destino(self, ip_destino):
		self.ip_destino = ip_destino

	def get_ip_destino(self):
		return self.ip_destino

	def get_dado(self):
		return self.dado

class Transporte(Camada):
	def __init__(self, ip_destino, dado, tipo_conexao = "TCP/UDP"):
		self.set_ip_destino(ip_destino)
		self.set_dado(dado)
		self.set_tipo_conexao(tipo_conexao)
		self.transporte = Sessao(self.get_ip_destino(), self.get_dado(), self.get_tipo_conexao())
		self.set_funcionalidade("Transporte")

	def set_ip_destino(self, ip_destino):
		self.ip_destino = ip_destino

	def set_dado(self, dado):
		self.dado = dado

	def set_tipo_conexao(self, tipo_conexao):
		self.tipo_conexao = tipo_conexao

	def get_ip_destino(self):
		return self.ip_destino	

	def get_dado(self):
		return self.dado

	def get_tipo_conexao(self):
		return self.tipo_conexao

class Sessao(Camada):
	def __init__(self, ip_destino, dado, tipo_conexao, direcao = "HalfDuplex"):
		self.set_ip_destino(ip_destino)		
		self.set_tipo_conexao(tipo_conexao)
		self.set_direcao(direcao)
		self.set_dado(dado)
		self.apresentacao = Apresentacao(self.get_pack())
		self.set_funcionalidade("Sessao")

	def set_ip_destino(self, ip_destino):
		self.ip_destino = ip_destino

	def set_dado(self, dado):
		self.package = list()
		if dado:
			self.package.extend([self.tipo_conexao, self.direcao, self.ip_destino])


	def set_tipo_conexao(self, tipo_conexao):
		self.tipo_conexao = tipo_conexao

	def set_direcao(self, direcao):
		self.direcao = direcao

	def get_ip_destino(self, ip_destino):
		return self.ip_destino	

	def get_pack(self):
		return self.package

	def get_tipo_conexao(self):
		return self.tipo_conexao

	def get_direcao(self):
		return self.direcao


class Apresentacao(Camada):
	def __init__(self, pack):
		self.set_pack(pack)
		self.aplicacao = Aplicacao(self.texto)
		self.set_funcionalidade("Apresentacao")

	def set_pack(self, pack):
		if pack:
			self.texto = "Tipo de Conexao: {} \n Direcao: {} \n Ip Destino: {} \n Dado: Hello World".format(pack[0], pack[1], pack[2])

	def get_pack():
		return self.pack
		

class Aplicacao(Camada):
	def __init__(self, texto):
		self.resp = input("Voce deseja ver a mensagem do seu amigo?[Y/y - N/n]")
		self.set_funcionalidade("Aplicacao")

		if self.resp is "Y" or self.resp is "y":
			print(texto)
			return

		print("Deu ruim pra caralho mano!")
		



obj = Fisica(True, True)
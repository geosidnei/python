'''
137_udp.py
Este código foi digitado a partir do visualizado em:
Canal Ignorância Zero/ Pedro Forli
Aulas Python - 137 - Programação para Internet III: UDP
link do youtube: https://www.youtube.com/watch?v=98CGGGiBX5k
Data que assisti a aula: 7 de setembro de 2023.

UDP consiste de um protocolo que faz uma conexão que 
envia dados sem segurança ao seu destino.
Isto signifia que o UDP manda dados para um endereço e
não verifica se o endereço os recebeu ou não. isso não
depende de estar ou não conectado a uma rede.
Se não estiver conectado, as informações enviadas ficarão
perdidar para sempre na internet. 
Puxa, que poético... parece até um astronauta desligado da
nave na qual viajou...
UDP é mais rápido, porque não verifica se os dados chegaram ou não. Ele só os envia. 
É muito comum para 
* telefonia VOIP, 
* jogos online e 
* streaming de videos.
'''
from socket import *

def main():
    # Cria host e port number
    host = ""
    port = 5_000
    
    # Cria socket
    # SOCK_DGRAM é do protocolo UDP.
    server = socket(AF_INET, SOCK_DGRAM)
    
    #Indica que o servidor foi iniciado
    print('Servidor iniciado')
    
    # Bloco infinito do servidor
    while True:
        # Recebe a data e o endereço da conexão
        data, endereco = server.recvfrom(1024)
        
        # Imprime as informações da conexão
        print('Mensagem recebida de', str(endereco))
        print('Recebemos do cliente:', str(data))
        
        #Vamos mandar de volta a mensagem em eco 
        resposta = "Eco --> " + str(data)
        server.sendto(data, endereco)
     
    # Fecha o servidor
    server.close()

if __name__ == '__main__':
    main()
 
# os códigos da aula 137 funcionaram, estou feliz por isso.

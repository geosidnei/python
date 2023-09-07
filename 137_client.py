'''
137_client.py

Este código foi digitado a partir do visualizado em:
Canal Ignorância Zero/ Pedro Forli
Aulas Python - 137 - Programação para Internet III: UDP
link do youtube: https://www.youtube.com/watch?v=98CGGGiBX5k
Data que assisti a aula: 7 de setembro de 2023.
'''
from socket import *

def main():
    # Cria host e port number
    host = "localhost"
    port = 5_000
    
    # O servidor será um par endereço/port
    server = (host, port)
    
    # Criamos o socket
    conexao = socket(AF_INET, SOCK_DGRAM)
    conexao.bind((host, port))
    
    # Vamos mandar mensagem enquanto for diferente de sair (s)
    msg = input('-->')
    
    while msg != 's':
        # Mandamos a mensagem via conexão
        conexao.sendto(msg.encode(), server)
        
        # Recebemos uma resposta do servidor
        data, endereco = conexao.recvfrom(1024)
        
        # Imprime a mensagem recebida
        print('Recebida --> ', str(data))
        
        # Podemos mandar mais mensagens
        
        msg = input('-->')
        
        
    # Fecha a conexão
    conexao.close()

if __name__ == '__main__':
    main()

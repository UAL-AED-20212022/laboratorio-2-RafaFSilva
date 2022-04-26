from LinkedList import *

def main():

    lista_ligada = LinkedList()

    while True:
        try:
            comandos = input().split()
        except EOFError:
            return
        if comandos[0] == 'RPI':
            RPI(lista_ligada, comandos)
        if comandos[0] == 'RPF':
            RPF(lista_ligada, comandos)
        if comandos[0] == 'RPDE':
            RPDE(lista_ligada, comandos)
        if comandos[0] == "RPAE":
            RPAE(lista_ligada, comandos[2], comandos[1])
        if comandos[0] == 'RPII':
            RPII(lista_ligada, comandos)
        if comandos[0] == 'VNE':
            VNE(lista_ligada, comandos)
        if comandos[0] == 'VP':
            VP(lista_ligada, comandos)
        if comandos[0] == 'EPE':
            EPE(lista_ligada, comandos)
        if comandos[0] == 'EUE':
            EUE(lista_ligada)
        if comandos[0] == 'EP':
            EP(lista_ligada, comandos)

def RPI(lista_ligada, comandos):
    país_novo = comandos[1]
    lista_ligada.insert_at_start(país_novo)
    lista_ligada.traverse_list()

def RPF(lista_ligada, comandos):
    país_novo = comandos[1]
    lista_ligada.insert_at_end(país_novo)
    lista_ligada.traverse_list()

def RPDE(lista_ligada, comandos):
    país_novo = comandos[2]
    país_registado = comandos[1]
    lista_ligada.insert_after_item(país_novo, país_registado)
    lista_ligada.traverse_list()

def RPAE(lista_ligada, pais_registado, pais_novo):
    lista_ligada.insert_before_item(pais_registado, pais_novo)
    lista_ligada.traverse_list()

def RPII(lista_ligada, comandos):
    país_novo = comandos[1]
    índice = int(comandos[2])
    lista_ligada.insert_at_index(índice, país_novo)
    lista_ligada.traverse_list()

def VNE(lista_ligada, número_elementos):
    número_elementos = lista_ligada.get_count()
    print(f'O número de elementos são {número_elementos}.')

def VP(lista_ligada, comandos):
    país_verificado = comandos[1]
    if lista_ligada.search_item(país_verificado) == False:
        print(f'O país {país_verificado} não se encontra na lista.')
    else:
        print(f'O país {país_verificado} encontra-se na lista.')

def EPE(lista_ligada, país_eliminado):
    país_eliminado = lista_ligada.start_node.item
    lista_ligada.delete_at_start()
    print(f'O país {país_eliminado} foi eliminado da lista.')

def EUE(lista_ligada):
    país_eliminado = lista_ligada.get_last_node()
    lista_ligada.delete_at_end()
    print(f'O país {país_eliminado} foi eliminado da lista.')

def EP(lista_ligada, comandos):
    país_eliminado = comandos[1]
    if lista_ligada.search_item(país_eliminado) == True:
        lista_ligada.delete_element_by_value(país_eliminado)
        print(f'O páis {país_eliminado} foi eliminado da lista.')
    else:
        print(f'O país {país_eliminado} não se encontra na lista.')
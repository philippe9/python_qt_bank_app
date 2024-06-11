import sys
from controllers.client_controller import *
from logger import LOGGER
from prettytable import PrettyTable, MARKDOWN, ORGMODE 
from pick import pick

personnes = []
get_index_question = "Quel est l'index de la personne ? (Commencez a 0) \n"
error_auth_message = "Identifiants incorrects."
good_bye_message = 'Au revoir !'
R = "\033[0;31;40m" #RED
G = "\033[0;32;40m" # GREEN
Y = "\033[0;33;40m" # Yellow
B = "\033[0;34;40m" # Blue
N = "\033[0m" # Reset
identifiant = ''
user = Client()
def menu():
    options = ['Dépôt', 'Retrait', 'Transfert', 'Historique des operations', 'Solde du comptes','Pour sortir du programme']
    
    option, index = pick(options, "Quel operation voulez vous effectuer ?", indicator='=>', default_index=0)
    
    match str(index + 1):
        case "1":
            do_depot()
        case "2":
            do_retrait()
        case "3":
            do_transfert()
        case "4":
            user_historique()
        case "5":
            user_solde()
        case "6":
            print(good_bye_message)
            sys.exit()
        case _:
            print(good_bye_message)
            sys.exit()
    
def do_depot():
    global identifiant
    print('Veuillez saissir les infos pour le depot')
    amount = int(input("Saisissez le montant : "))
    user_pin = input("Saisissez votre code pin : ")
    transaction_solde = deposit_customer_account(identifiant, user_pin, amount)
    if(transaction_solde.login_done and transaction_solde.depot_done):
        print(transaction_solde.message_depot + "\n")
        continue_operation()
    else:
        print(transaction_solde.message_login+ "\n")
        do_depot()
    
    
def do_retrait():
    global identifiant
    print('Veuillez saissir les infos pour le retrait')
    amount = int(input("Saisissez le montant : "))
    user_pin = input("Saisissez votre code pin : ")
    transaction_solde = retrieve_customer_account(identifiant, user_pin, amount)
    
    if(transaction_solde.login_done):
        if(transaction_solde.retrait_done):
            print(transaction_solde.message_retrait + "\n")
            continue_operation()
        else:
            print(transaction_solde.message_retrait + "\n")
            do_retrait()
    else:
        print(transaction_solde.message_login + "\n")
        continue_operation()
    
def do_transfert():
    global identifiant
    print('Veuillez saissir les infos pour le transfert')
    amount = int(input("Saisissez le montant : "))
    reciever_account_num = input("Saisissez le Numero de compte beneficiaire : ")
    user_pin = input("Saisissez votre code pin : ")
    transaction_solde = do_transaction(identifiant, user_pin, amount, reciever_account_num)
    
    if(transaction_solde.login_done):
        if(transaction_solde.transfert_done):
            print(transaction_solde.message_transfert + "\n")
            continue_operation()
        else:
            print(transaction_solde.message_transfert + "\n")
            do_transfert()
    else:
        print(transaction_solde.message_login + "\n")
        continue_operation()
    
def user_historique():
    global identifiant
    print("Veuillez saissir les infos pour l'historique")
    nb = input("Le nombre de transactions a afficher(10 par defaut) : ")
    if nb == '':
        nb = 10
    user_pin = input("Saisissez votre code pin : ")
    current_user = login_customer(identifiant, user_pin)
    trxs = list_user_transaction(identifiant, user_pin, 10 if nb < 0 else int(nb) )
    
    table = PrettyTable()
    

    table.field_names = ["Montant", "Type", "Compte emmeteur","Compte recepteur", "Date de l'operation","Mat operation"]
    for i, item in enumerate(trxs):
        if item.type == 'DEPOT':
             table.add_row([f"{str(item.montant)} FCFA", G+item.type+N, item.compte_emmeteur_obj.nom, item.compte_recepteur_obj.nom, item.date.strftime('%a %d/%m/%Y , %H:%M:%S'),item.matricule_transaction])
        if item.type == 'RETRAIT':
            table.add_row([f"{str(item.montant)} FCFA", R+item.type+N, item.compte_emmeteur_obj.nom, item.compte_recepteur_obj.nom, item.date.strftime('%a %d/%m/%Y , %H:%M:%S'),item.matricule_transaction])
        if item.type == 'TRANSACTION':
            if item.compte_recepteur_obj.identifiant == current_user:
                table.add_row([f"{str(item.montant)} FCFA", G+item.type+N, item.compte_emmeteur_obj.nom, item.compte_recepteur_obj.nom, item.date.strftime('%a %d/%m/%Y , %H:%M:%S'),item.matricule_transaction])
            else:
                table.add_row([f"{str(item.montant)} FCFA", R+item.type+N, item.compte_emmeteur_obj.nom, item.compte_recepteur_obj.nom, item.date.strftime('%a %d/%m/%Y , %H:%M:%S'),item.matricule_transaction])

    table.set_style(ORGMODE)
    
    print(table)
    continue_operation()
    # menu()
def user_solde():
    global identifiant
    print('Veuillez saissir les infos pour avoir votre solde')
    user_pin = input("Saisissez votre code pin : ")
    login_done = login_customer(identifiant, user_pin)
    if(login_done):
        print(f"Votre solde est de {G}{login_done.solde} FCFA{N}")
        continue_operation()
    else:
        print(error_auth_message)
        user_solde()
def initial_auth():
    global identifiant
    identifiant = input("Entrez votre identifiant : ")
    pin = input("Entrez votre code pin : ")
    
    user = login_customer(identifiant, pin)
    if(user):
        identifiant = user.identifiant
        menu()
    else:
        print(error_auth_message)
        initial_auth()
def continue_operation():
    confirm = input("Voulez vous continuer avec une autre operation ? [y/N]")
    if(confirm == 'y'):
        menu()
    else:
        print(good_bye_message)
        sys.exit()
    
LOGGER.remove()
print("Bienvenue dans la banque python! \n")
initial_auth()

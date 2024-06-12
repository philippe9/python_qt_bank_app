from models.models import Client
from models.enums import TYPE_TRANSACTION, ETAT_TRANSACTION
from models.models import Transaction
from repository.client_repo import create_user, login_user, update_user_solde, get_user
from logger import LOGGER
from models.return_model import ReturnModel
from repository.transaction_repo import create_transaction, list_transactions

def add_user(user_name:str, pin: str):
    # return Client(
    #     nom="toddthebod",
    #     prenom="Password123lmao",
    #     num_compte="12341123",
    #     pin="12345",
    #     solde=20000,
    #     identifiant="melo",
    # )
    login_customer(user_name, pin)

def login_customer(identifiant:str, pin: str)-> Client | bool:
    if(len(identifiant) < 5 and len(pin) < 3):
        return False
    return login_user(identifiant, pin)

def retrieve_customer_account(identifiant:str, pin: str, amount: int)->ReturnModel :
    user = login_user(identifiant, pin)
    if(user is not None and user is not False):
        if(user.solde > amount):
            retrait = update_user_solde(user.num_compte, user.solde - amount)
            
            transaction = create_transaction(Transaction(
            montant=amount,
            compte_emmeteur = user.num_compte,
            compte_recepteur = user.num_compte,
            type = TYPE_TRANSACTION['RETRAIT'],
            etat = ETAT_TRANSACTION['SUCCESS'],
            ))
            if(retrait and transaction):
                return ReturnModel(True, False, True, False,'','',f"Votre retrait de {amount} FCFA dans votre compte s'est effectue avec success. Votre nouveau solde est de {retrait} FCFA")
        else :
            return ReturnModel(True,False,False, False,'','',"Votre solde est insuffisant pour effectuer la transaction")
    else :
        return ReturnModel(False)

def deposit_customer_account(identifiant:str, pin: str, amount: int)->ReturnModel :
    user = login_user(identifiant, pin)
    if(user is not None and user is not False):
        depot = update_user_solde(user.num_compte, user.solde + amount)
        
        transaction = create_transaction(Transaction(
            montant=amount,
            compte_emmeteur = user.num_compte,
            compte_recepteur = user.num_compte,
            type = TYPE_TRANSACTION['DEPOT'],
            etat = ETAT_TRANSACTION['SUCCESS'],
        ))
        if(depot and transaction):
            return ReturnModel(True, True, False, False,'',f"Votre depot de {amount} FCFA dans votre compte s'est effectue avec success. Votre nouveau solde est de {depot} FCFA")
        else:
            return ReturnModel(True, False, False, False,'',"Erreur l'ors de la transaction")
    return ReturnModel(False)


def do_transaction(identifiant: str, pin: str, amount:int, compte_recepteur:str) -> ReturnModel:
    user = login_user(identifiant, pin)
    if(user is not None and user is not False):
        receiver = get_user(compte_recepteur)
        if(receiver is not None and receiver is not False):
            if(user.solde > amount):
                depot = update_user_solde(receiver.num_compte, receiver.solde + amount)
                retrait = update_user_solde(user.num_compte, user.solde - amount)
        
                transaction = create_transaction(Transaction(
                montant=amount,
                compte_emmeteur = user.num_compte,
                compte_recepteur = receiver.num_compte,
                type = TYPE_TRANSACTION['TRANSACTION'],
                etat = ETAT_TRANSACTION['SUCCESS'],
                ))
                if(depot and transaction and retrait):
                    return ReturnModel(True, False, False, True,'','','',f"Votre depot de {amount} FCFA vers le compte {receiver.num_compte} s'est effectue avec success. Votre nouveau solde est de {retrait} FCFA")
            else:
                return ReturnModel(True,False,False,False, '','','',"Votre solde est insuffisant pour effectuer la transaction")
        else:
            return ReturnModel(False,False,False,False, '','','',"Le compte recepteur n'existe pas")
    return ReturnModel(False)
def list_user_transaction(identifiant: str, pin: str,nombre_trx: int) -> bool |list[Transaction] :
    user = login_user(identifiant, pin)
    if(user is not None and user is not False):
        return list_transactions(nombre_trx, user.num_compte)
    return False    
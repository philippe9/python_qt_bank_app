from models.models import Client
from models.models import Transaction
from database import session
from logger import LOGGER
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from helpers.random_string import generate_random_string
from sqlalchemy import or_

def create_transaction(transaction: Transaction) -> Transaction:
    """
    Create a new transaction.
    :param Transaction transaction: New transaction record to create.

    :return: Optional[Transaction]
    """
    try:
        transaction.matricule_transaction = generate_random_string()
       
        session.add(transaction)  # Add the transaction
        session.commit()  # Commit the change
        LOGGER.success(f"Created transaction repo: {transaction}")
        return transaction
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

def list_transactions(nombre_trx: int, num_compte: int) -> list[Transaction]:
    """
    List transactions.
    :param int nombre_trx: Le nombre de transactions a extraire.
    :param int num_compte: Le compte qui a besoin de ses transactions.
.join(Client, onclause=Transaction.compte_emmeteur == Client.num_compte)
    :return: Optional[Transaction]
    """
    try:
        transactions = session.query(Transaction).join(Client, onclause=or_(Transaction.compte_emmeteur == Client.num_compte, Transaction.compte_recepteur == Client.num_compte)).filter(or_(Transaction.compte_emmeteur == num_compte, Transaction.compte_recepteur == num_compte)).limit(nombre_trx).all()
       
        return transactions
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e
from database import session
from models.models import Client
from logger import LOGGER
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
import hashlib

def create_user(client: Client) -> Client:
    """
    Create a new user if num_compte isn't already taken.
    :param User user: New user record to create.

    :return: Optional[User]
    """
    try:
        existing_user = session.query(Client).filter(Client.num_compte == client.num_compte).first()
        if existing_user is None:
            client.pin = hashlib.md5(client.pin.encode()).hexdigest()
            session.add(client)  # Add the user
            session.commit()  # Commit the change
            LOGGER.success(f"Created user repo: {client}")
            return client
        else:
            LOGGER.warning(f"Users already exists in database: {existing_user}")
            return session.query(Client).filter(Client.num_compte == client.num_compte).first()
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

def login_user(identifiant:str, pin: str) -> Client | bool:
    """
    Take user's credentials and search is the account is existing.
    :param identifiant str: User's identifier.
    :param pin str: User password

    :return: Optional[User]
    :return: Optional[Boolean]
    """
    user_pin = hashlib.md5(pin.encode()).hexdigest()
    try:
        existing_user = session.query(Client).filter(Client.identifiant == identifiant, Client.pin == user_pin ).first()
        if existing_user is None: 
            LOGGER.warning(f"This user with identifier {identifiant} and pin {user_pin} doesn't exist in the database")
            return False
        else:
            LOGGER.success(f"Logged user: {existing_user}")
            return existing_user
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

def get_user(num_compte:str) -> Client | bool: 
    """
    Get user acount is existing.
    :param identifiant str: User's identifier.
    :param pin str: User password

    :return: Optional[User]
    :return: Optional[Boolean]
    """
    try:
        existing_user = session.query(Client).filter(Client.num_compte == num_compte).first()
        if existing_user is None: 
            LOGGER.warning(f"This user with identifier {num_compte} doesn't exist in the database")
            return False
        else:
            LOGGER.success(f"Logged user: {existing_user}")
            return existing_user
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

def update_user_solde(num_compte: str, solde: int)-> bool|int:
    """
    Update user account.
    :param num_compte str: User's num_compte.
    :param solde str: User solde

    :return: Optional[Boolean]
    """
    try:
        res = session.query(Client).filter(Client.num_compte == num_compte).update({Client.solde: solde})
        if res is None: 
            LOGGER.warning(f"This user with identifier {num_compte} doesn't exist in the database")
            return False
        else:
            LOGGER.success(f"Solde de l'Utilisateur {num_compte} mis a jour a {solde}")
            return solde
    except IntegrityError as e:
        LOGGER.error(e.orig)
        raise e.orig
    except SQLAlchemyError as e:
        LOGGER.error(f"Unexpected error when creating user: {e}")
        raise e

"""Declare models and relationships."""
from sqlalchemy import Column, DateTime, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from database import engine
Base = declarative_base()


class Client(Base):
    """Client account."""
    
    __tablename__ = "client"
   
    id_client = Column(Integer, primary_key=True, autoincrement="auto")
    nom = Column(String(255))
    prenom = Column(String(255))
    pin = Column(String(200), nullable=False)
    solde = Column(Integer, nullable=False)
    num_compte = Column(String(10), unique=True, nullable=False)
    identifiant = Column(String(20), nullable=False)
    is_admin = Column(Boolean, default=False)
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    trx_emit = relationship(
        "Transaction",
        foreign_keys="[Transaction.compte_emmeteur]",
        back_populates="compte_emmeteur_obj",
        cascade="all, delete",
    )
    trx_recu = relationship(
        "Transaction",
        foreign_keys="[Transaction.compte_recepteur]",
        back_populates="compte_recepteur_obj",
        cascade="all, delete",
    )
    def __repr__(self):
        return f"<User id={self.id_client}, nom={self.nom}, identifiant={self.identifiant}>"

class Transaction(Base):
    """Transaction Table."""

    __tablename__ = "transaction"

    id_transaction = Column(Integer, primary_key=True, autoincrement="auto")
    montant = Column(Integer, nullable=False)
    date = Column(DateTime, server_default=func.now())
    matricule_transaction = Column(String(20), unique=True, nullable=False)
    compte_emmeteur = Column("compte_emmeteur",String(10), ForeignKey('client.num_compte'), nullable=False)
    compte_recepteur = Column("compte_recepteur",String(10), ForeignKey('client.num_compte'), nullable=False)
    
    # compte_emmeteur_obj = relationship("Client")
    # compte_recepteur_obj = relationship("Client")
    compte_emmeteur_obj = relationship("Client", foreign_keys=[compte_emmeteur], back_populates="trx_emit")
    compte_recepteur_obj = relationship("Client", foreign_keys=[compte_recepteur], back_populates="trx_recu")
    
    etat = Column(String(20), nullable=False)
    type = Column(String(20), nullable=False)
    
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<User id={self.id_transaction}, montant={self.montant}, etat={self.etat}>"
    
Base.metadata.create_all(engine)

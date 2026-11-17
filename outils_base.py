"""Base SQLite de la boutique et outils SQL utilisés par l'agent."""
import sqlite3
from langchain_core.tools import tool
BASE = "boutique.db"

def creer_base():
    """(Re)crée la base avec quelques commandes de démonstration."""
    con = sqlite3.connect(BASE)
    con.executescript(
    """
    DROP TABLE IF EXISTS retours;
    DROP TABLE IF EXISTS commandes;
    CREATE TABLE commandes (
        id INTEGER PRIMARY KEY,
        client TEXT,
        produit TEXT,
        montant REAL,
        statut TEXT,
        date_livraison TEXT
        );
    CREATE TABLE retours (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        commande_id INTEGER REFERENCES commandes(id),
        motif TEXT,
        date_demande TEXT DEFAULT (date('now'))
        );
    INSERT INTO commandes VALUES
    (1001, 'Amine Trabelsi', 'Clavier mécanique', 120.0, 'en
    préparation', NULL),
    (1002, 'Sarra Ben Ali', 'Écran 24 pouces', 450.0,
    'expédiée', NULL),
    (1003, 'Yassine Kammoun', 'Souris sans fil', 35.0,
    'livrée', date('now', '-10 days')),
    (1004, 'Mariem Gargouri', 'Casque audio', 89.0,
    'livrée', date('now', '-30 days'));
    """
)
    con.commit()
    con.close()
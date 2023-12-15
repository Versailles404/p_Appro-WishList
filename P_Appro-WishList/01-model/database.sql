CREATE TABLE t_souhait(
   idSouhait VARCHAR(50),
   nom VARCHAR(500),
   prix CURRENCY,
   lien VARCHAR(500),
   caractéristique VARCHAR(100),
   description VARCHAR(1000),
   PRIMARY KEY(idSouhait)
);

CREATE TABLE t_utilisateur(
   idUtilisateur VARCHAR(50),
   pseudo VARCHAR(50),
   nom VARCHAR(100),
   prénom VARCHAR(50),
   date_de_naissance DATE,
   langue VARCHAR(50),
   PRIMARY KEY(idUtilisateur)
);

CREATE TABLE souhaiter(
   idSouhait VARCHAR(50),
   idUtilisateur VARCHAR(50),
   nom VARCHAR(100),
   jj_mm_aaaa DATE,
   PRIMARY KEY(idSouhait, idUtilisateur),
   FOREIGN KEY(idSouhait) REFERENCES t_souhait(idSouhait),
   FOREIGN KEY(idUtilisateur) REFERENCES t_utilisateur(idUtilisateur)
);

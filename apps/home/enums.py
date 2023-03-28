CODE_BRANCHE = '01'
# sexe pour personnes physiques
FEMME = 0
HOMME = 1

choix_genre = (
    (FEMME, 'FEMME'),
    (HOMME, 'HOMME'),
)
# ----- ELEMENTS DE PERIODE -------
# les mois
JANVIER = 1
FEVRIER = 2
MARS = 3
AVRIL = 4
MAI = 5
JUIN = 6
JUILLET = 7
AOUT = 8
SEPTEMBRE = 9
OCTOBRE = 10
NOVEMBRE = 11
DECEMBRE = 12
# les trimestres
PREMIER_TRIMESTRE = 13
DEUXIEME_TRIMESTRE = 14
TROISIEME_TRIMESTRE = 15
QUATRIEME_TRIMESTRE = 16
# les semestres
PREMIER_SEMESTRE = 17
DEUXIEME_SEMESTRE = 18
# anne
ANNEE = 19

choix_periode_cotisation = {
    (JANVIER, 'JANVIER'),
    (FEVRIER, 'FEVRIER'),
    (MARS, 'MARS'),
    (AVRIL, 'AVRIL'),
    (MAI, 'MAI'),
    (JUIN, 'JUIN'),
    (JUILLET, 'JUILLET'),
    (AOUT, 'AOUT'),
    (SEPTEMBRE, 'SEPTEMBRE'),
    (OCTOBRE, 'OCTOBRE'),
    (NOVEMBRE, 'NOVEMBRE'),
    (DECEMBRE, 'DECEMBRE'),
    (PREMIER_TRIMESTRE, '1er TRIMESTRE'),
    (DEUXIEME_TRIMESTRE, '2e TRIMESTRE'),
    (TROISIEME_TRIMESTRE, '3e TRIMESTRE'),
    (QUATRIEME_TRIMESTRE, '4e TRIMESTRE'),
    (PREMIER_SEMESTRE, '1er SEMESTRE'),
    (DEUXIEME_SEMESTRE, '2e SEMESTRE'),
    (ANNEE, 'ANNEE'),
}

# type de cotisation
AUTRE = 0
ANNUEL = 1
SEMESTREIL = 2
TRIMESTRIEL = 3
MENSUEL = 4
JOURNALIER = 5
choix_type_cotisation = (
    (AUTRE , "AUTRE"),
    (JOURNALIER, "JOURNALIER"),
    (MENSUEL , "MENSUEL"),
    (TRIMESTRIEL , "TRIMESTRIEL"),
    (SEMESTREIL , "SEMESTREIL"),
    (ANNUEL , "ANNUEL"),
)
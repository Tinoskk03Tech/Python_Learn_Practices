#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// =============================================================
// 1. DEFINITION DES STRUCTURES (Respect du MLD)
// =============================================================

// Structure chargée en RAM
typedef struct {
    int id_type;
    char nom_type[30];
    float prix_jour_personne;
} TypeEmplacement;

// Structures stockées sur Disque
typedef struct {
    int id_emplacement;
    int id_type_emplacement; // Clé étrangère
    float surface;
    int nbre_personne_max;
    int est_supprime;        // Suppression logique (1=supprimé)
} Emplacement;

typedef struct {
    int id_client;
    char nom_client[50];
    char contact_client[50];
    int est_supprime;
} Client;

typedef struct {
    int id_sejour;
    int id_client;          // Clé étrangère
    int id_emplacement;     // Clé étrangère
    char date_debut[11];
    char date_fin[11];
    int nb_personnes;
    int est_supprime;
} Sejour;

// =============================================================
// 2. VARIABLES GLOBALES ET FICHIERS
// =============================================================

TypeEmplacement *tabTypes = NULL;
int nbTypes = 0;

const char *F_TYPES = "types.dat";
const char *F_EMPLACEMENTS = "emplacements.dat";
const char *F_CLIENTS = "clients.dat";
const char *F_SEJOURS = "sejours.dat";

// =============================================================
// 3. GESTION DES TYPES (Chargement / Dechargement / Affichage)
// =============================================================

void initTypesParDefaut() {
    FILE *f = fopen(F_TYPES, "wb");
    if (f) {
        TypeEmplacement base[4] = {
            {1, "Caravane", 13.50},
            {2, "Tente", 11.00},
            {3, "Camping-Car", 14.00},
            {4, "Bungalow", 17.50}
        };
        fwrite(base, sizeof(TypeEmplacement), 4, f);
        fclose(f);
    }
}

void chargerTypes() {
    FILE *f = fopen(F_TYPES, "rb");
    if (!f) {
        initTypesParDefaut();
        f = fopen(F_TYPES, "rb");
    }

    fseek(f, 0, SEEK_END);
    long taille = ftell(f);
    nbTypes = taille / sizeof(TypeEmplacement);
    rewind(f);

    tabTypes = (TypeEmplacement*) malloc(nbTypes * sizeof(TypeEmplacement));
    if (tabTypes != NULL) {
        fread(tabTypes, sizeof(TypeEmplacement), nbTypes, f);
    }
    fclose(f);
}

void dechargerTypes() {
    if (tabTypes != NULL) {
        free(tabTypes);
        tabTypes = NULL;
    }
}

// Recherche le nom d'un type par son ID (depuis la RAM)
const char* getNomType(int id) {
    for(int i=0; i<nbTypes; i++) {
        if(tabTypes[i].id_type == id) return tabTypes[i].nom_type;
    }
    return "Inconnu";
}

// Affiche le tableau des types (Demandé au début)
void afficherTableauTypes() {
    printf("\n");
    printf("############################################################\n");
    printf("#            TYPES D'EMPLACEMENTS (Charge en RAM)          #\n");
    printf("############################################################\n");
    printf("| %-4s | %-25s | %-15s |\n", "ID", "NOM DU TYPE", "PRIX/JOUR (EUR)");
    printf("|------|---------------------------|-------------------|\n");
    for(int i=0; i<nbTypes; i++) {
        printf("| %-4d | %-25s | %-15.2f |\n",
               tabTypes[i].id_type, tabTypes[i].nom_type, tabTypes[i].prix_jour_personne);
    }
    printf("------------------------------------------------------------\n");
}

// =============================================================
// 4. FONCTIONS UTILITAIRES (Génériques)
// =============================================================

int genererId(const char *nomFichier, size_t tailleStruct) {
    FILE *f = fopen(nomFichier, "rb");
    if (!f) return 1;
    fseek(f, 0, SEEK_END);
    int id = (ftell(f) / tailleStruct) + 1;
    fclose(f);
    return id;
}

// =============================================================
// 5. GESTION CLIENTS (CRUD COMPLET)
// =============================================================

void ajouterClient() {
    Client c;
    c.id_client = genererId(F_CLIENTS, sizeof(Client));
    c.est_supprime = 0;

    printf("\n--- AJOUT CLIENT ---\n");
    printf("Nom complet : "); scanf(" %[^\n]", c.nom_client);
    printf("Contact : "); scanf(" %[^\n]", c.contact_client);

    FILE *f = fopen(F_CLIENTS, "ab");
    fwrite(&c, sizeof(Client), 1, f);
    fclose(f);
    printf(">> Client ajoute (ID: %d)\n", c.id_client);
}

void listerClients() {
    FILE *f = fopen(F_CLIENTS, "rb");
    if (!f) { printf("Pas de clients.\n"); return; }
    Client c;
    printf("\n--- LISTE CLIENTS ---\n");
    while(fread(&c, sizeof(Client), 1, f)) {
        if(!c.est_supprime)
            printf("[%d] %s (Contact: %s)\n", c.id_client, c.nom_client, c.contact_client);
    }
    fclose(f);
}

void modifierClient() {
    int id, trouve = 0;
    listerClients();
    printf("ID du client a modifier : "); scanf("%d", &id);

    FILE *f = fopen(F_CLIENTS, "rb+");
    Client c;
    while(fread(&c, sizeof(Client), 1, f)) {
        if(c.id_client == id && !c.est_supprime) {
            printf("Nouveau Nom : "); scanf(" %[^\n]", c.nom_client);
            printf("Nouveau Contact : "); scanf(" %[^\n]", c.contact_client);

            fseek(f, -sizeof(Client), SEEK_CUR);
            fwrite(&c, sizeof(Client), 1, f);
            trouve = 1;
            printf(">> Client modifie.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> ID introuvable.\n");
}

void supprimerClient() {
    int id, trouve = 0;
    listerClients();
    printf("ID du client a supprimer : "); scanf("%d", &id);

    FILE *f = fopen(F_CLIENTS, "rb+");
    Client c;
    while(fread(&c, sizeof(Client), 1, f)) {
        if(c.id_client == id && !c.est_supprime) {
            c.est_supprime = 1; // Suppression logique
            fseek(f, -sizeof(Client), SEEK_CUR);
            fwrite(&c, sizeof(Client), 1, f);
            trouve = 1;
            printf(">> Client supprime.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> ID introuvable.\n");
}

// =============================================================
// 6. GESTION EMPLACEMENTS (CRUD COMPLET)
// =============================================================

void ajouterEmplacement() {
    Emplacement e;
    e.id_emplacement = genererId(F_EMPLACEMENTS, sizeof(Emplacement));
    e.est_supprime = 0;

    printf("\n--- AJOUT EMPLACEMENT ---\n");
    // On re-affiche les types pour aider l'utilisateur
    afficherTableauTypes();
    printf("ID du Type : "); scanf("%d", &e.id_type_emplacement);
    printf("Surface (m2) : "); scanf("%f", &e.surface);
    printf("Nb Personnes Max : "); scanf("%d", &e.nbre_personne_max);

    FILE *f = fopen(F_EMPLACEMENTS, "ab");
    fwrite(&e, sizeof(Emplacement), 1, f);
    fclose(f);
    printf(">> Emplacement ajoute (ID: %d)\n", e.id_emplacement);
}

void listerEmplacements() {
    FILE *f = fopen(F_EMPLACEMENTS, "rb");
    if (!f) { printf("Pas d'emplacements.\n"); return; }
    Emplacement e;
    printf("\n--- LISTE EMPLACEMENTS ---\n");
    printf("| ID | Type             | Surf. | Pers |\n");
    while(fread(&e, sizeof(Emplacement), 1, f)) {
        if(!e.est_supprime) {
            printf("| %-2d | %-16s | %-5.1f | %-4d |\n",
                   e.id_emplacement, getNomType(e.id_type_emplacement), e.surface, e.nbre_personne_max);
        }
    }
    fclose(f);
}

void modifierEmplacement() {
    int id, trouve = 0;
    listerEmplacements();
    printf("ID a modifier : "); scanf("%d", &id);

    FILE *f = fopen(F_EMPLACEMENTS, "rb+");
    Emplacement e;
    while(fread(&e, sizeof(Emplacement), 1, f)) {
        if(e.id_emplacement == id && !e.est_supprime) {
            printf("Nouveau ID Type : "); scanf("%d", &e.id_type_emplacement);
            printf("Nouvelle Surface : "); scanf("%f", &e.surface);
            printf("Nouveau Nb Pers : "); scanf("%d", &e.nbre_personne_max);

            fseek(f, -sizeof(Emplacement), SEEK_CUR);
            fwrite(&e, sizeof(Emplacement), 1, f);
            trouve = 1;
            printf(">> Emplacement modifie.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> Introuvable.\n");
}

void supprimerEmplacement() {
    int id, trouve = 0;
    listerEmplacements();
    printf("ID a supprimer : "); scanf("%d", &id);

    FILE *f = fopen(F_EMPLACEMENTS, "rb+");
    Emplacement e;
    while(fread(&e, sizeof(Emplacement), 1, f)) {
        if(e.id_emplacement == id && !e.est_supprime) {
            e.est_supprime = 1;
            fseek(f, -sizeof(Emplacement), SEEK_CUR);
            fwrite(&e, sizeof(Emplacement), 1, f);
            trouve = 1;
            printf(">> Emplacement supprime.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> Introuvable.\n");
}

// =============================================================
// 7. GESTION SEJOURS (CRUD COMPLET)
// =============================================================

void ajouterSejour() {
    Sejour s;
    s.id_sejour = genererId(F_SEJOURS, sizeof(Sejour));
    s.est_supprime = 0;

    printf("\n--- NOUVEAU SEJOUR ---\n");
    listerClients();
    printf("ID Client : "); scanf("%d", &s.id_client);

    listerEmplacements();
    printf("ID Emplacement : "); scanf("%d", &s.id_emplacement);

    printf("Date Debut (JJ/MM/AAAA) : "); scanf("%s", s.date_debut);
    printf("Date Fin (JJ/MM/AAAA) : "); scanf("%s", s.date_fin);
    printf("Nb Personnes : "); scanf("%d", &s.nb_personnes);

    FILE *f = fopen(F_SEJOURS, "ab");
    fwrite(&s, sizeof(Sejour), 1, f);
    fclose(f);
    printf(">> Sejour cree (ID: %d)\n", s.id_sejour);
}

void listerSejours() {
    FILE *f = fopen(F_SEJOURS, "rb");
    if (!f) { printf("Pas de sejours.\n"); return; }
    Sejour s;
    printf("\n--- LISTE SEJOURS ---\n");
    while(fread(&s, sizeof(Sejour), 1, f)) {
        if(!s.est_supprime) {
            printf("[#%d] Client:%d -> Emplac:%d | %s au %s (%d pers)\n",
                   s.id_sejour, s.id_client, s.id_emplacement, s.date_debut, s.date_fin, s.nb_personnes);
        }
    }
    fclose(f);
}

void modifierSejour() {
    int id, trouve = 0;
    listerSejours();
    printf("ID Sejour a modifier : "); scanf("%d", &id);

    FILE *f = fopen(F_SEJOURS, "rb+");
    Sejour s;
    while(fread(&s, sizeof(Sejour), 1, f)) {
        if(s.id_sejour == id && !s.est_supprime) {
            printf("Nouveau Debut : "); scanf("%s", s.date_debut);
            printf("Nouvelle Fin : "); scanf("%s", s.date_fin);
            printf("Nouveau Nb Personnes : "); scanf("%d", &s.nb_personnes);
            // On pourrait modifier client/emplacement aussi si besoin

            fseek(f, -sizeof(Sejour), SEEK_CUR);
            fwrite(&s, sizeof(Sejour), 1, f);
            trouve = 1;
            printf(">> Sejour modifie.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> Introuvable.\n");
}

void supprimerSejour() {
    int id, trouve = 0;
    listerSejours();
    printf("ID Sejour a supprimer : "); scanf("%d", &id);

    FILE *f = fopen(F_SEJOURS, "rb+");
    Sejour s;
    while(fread(&s, sizeof(Sejour), 1, f)) {
        if(s.id_sejour == id && !s.est_supprime) {
            s.est_supprime = 1;
            fseek(f, -sizeof(Sejour), SEEK_CUR);
            fwrite(&s, sizeof(Sejour), 1, f);
            trouve = 1;
            printf(">> Sejour supprime.\n");
            break;
        }
    }
    fclose(f);
    if(!trouve) printf(">> Introuvable.\n");
}

// =============================================================
// 8. MENU PRINCIPAL
// =============================================================

int main() {
    // 1. Chargement des Types au lancement
    chargerTypes();

    // 2. Affichage des Types AVANT le menu (Exigence utilisateur)
    afficherTableauTypes();

    int choix = 0;
    int sousChoix = 0;

    do {
        printf("\n====================================\n");
        printf("       GESTION CAMPING MANAGER      \n");
        printf("====================================\n");
        printf("1. GESTION CLIENTS\n");
        printf("2. GESTION EMPLACEMENTS\n");
        printf("3. GESTION SEJOURS\n");
        printf("4. RE-AFFICHER TYPES (Tableau)\n");
        printf("0. QUITTER\n");
        printf("------------------------------------\n");
        printf("Votre choix : ");
        scanf("%d", &choix);

        switch(choix) {
            case 1:
                printf("\n--- MENU CLIENTS ---\n");
                printf("1. Creer\n2. Modifier\n3. Supprimer\n4. Lister\nChoix: ");
                scanf("%d", &sousChoix);
                if(sousChoix==1) ajouterClient();
                else if(sousChoix==2) modifierClient();
                else if(sousChoix==3) supprimerClient();
                else if(sousChoix==4) listerClients();
                break;

            case 2:
                printf("\n--- MENU EMPLACEMENTS ---\n");
                printf("1. Creer\n2. Modifier\n3. Supprimer\n4. Lister\nChoix: ");
                scanf("%d", &sousChoix);
                if(sousChoix==1) ajouterEmplacement();
                else if(sousChoix==2) modifierEmplacement();
                else if(sousChoix==3) supprimerEmplacement();
                else if(sousChoix==4) listerEmplacements();
                break;

            case 3:
                printf("\n--- MENU SEJOURS ---\n");
                printf("1. Creer\n2. Modifier\n3. Supprimer\n4. Lister\nChoix: ");
                scanf("%d", &sousChoix);
                if(sousChoix==1) ajouterSejour();
                else if(sousChoix==2) modifierSejour();
                else if(sousChoix==3) supprimerSejour();
                else if(sousChoix==4) listerSejours();
                break;

            case 4:
                afficherTableauTypes();
                break;

            case 0:
                printf("Fermeture et sauvegarde...\n");
                break;
            default:
                printf("Choix invalide.\n");
        }
    } while (choix != 0);

    // 3. Déchargement de la mémoire à la fermeture
    dechargerTypes();

    return 0;
}
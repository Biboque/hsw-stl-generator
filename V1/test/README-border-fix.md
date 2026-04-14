# Babique's HSW Generator v1.3.6 - Border Visibility Fix

## Description
Version corrigée du générateur HSW avec la résolution du problème de visibilité des bordures épaissies lors du changement de visibilité des calques.

## Corrections apportées

### Problème résolu
Quand on rendait un calque visible, les épaisseurs doublées (bordures épaissies) des calques cachés restaient visibles à l'écran.

### Modifications du code

1. **Fonction `addBorderMesh`** :
   - Ajout de la vérification de visibilité du calque avant d'ajouter les bordures à la scène
   - Les borderMeshes ne sont créés que si le calque est visible

2. **Fonction `applyLayerVisibilityToPiece`** :
   - Extension pour gérer aussi la visibilité des borderMeshes
   - Synchronisation de la visibilité des bordures avec celle du mesh principal

3. **Fonction `setLayerVisibility`** :
   - Création automatique des borderMeshes manquants quand on rend un calque visible
   - Assure la cohérence quand `showBorder` est activé globalement

## Fichiers
- `index.html` : Version principale avec les corrections
- `BABIQUES-HSW-GENERATOR-v1.3.6.html` : Version officielle v1.3.6
- `BABIQUES-HSW-GENERATOR-v1.3.5-border-fix.html` : Copie de sauvegarde de la version précédente

## Test des corrections
1. Créer plusieurs calques avec des pièces
2. Activer les bordures épaissies globalement
3. Cacher certains calques
4. Vérifier que seules les bordures des calques visibles sont affichées
5. Rendre un calque visible et vérifier que ses bordures apparaissent correctement

## Historique des versions
- `BABIQUES-HSW-GENERATOR-v1.3.4a.html` : Version sans corrections de visibilité des bordures
- `BABIQUES-HSW-GENERATOR-v1.3.5-border-fix.html` : Version de développement avec corrections
- `BABIQUES-HSW-GENERATOR-v1.3.6.html` : Version officielle avec corrections intégrées
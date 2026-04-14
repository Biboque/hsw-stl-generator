# Babique's HSW Generator - Changelog

## Version 2.0.0 (2026-04-14)

### ✨ New Major Features
- **Layer System**: Complete layer management with visibility controls, custom colors, drag-and-drop reordering, and grouping/ungrouping
- **Enhanced 3D Preview**: Improved Three.js integration with better rendering, orthographic/perspective toggle, and advanced camera controls
- **Shape Library Expansion**: All shapes (Hexagon, Pentagon, Trapezoid, Diamond, Shard, Tier, Quarter, Triangle) now available in Hollow, Solid, and Fixing variants
- **Advanced Selection Tools**: Multi-select with Shift+click, rubber band selection, context menus for batch operations
- **Mirror Operations**: X, Y, Z axis mirroring with visual feedback
- **Border Reinforcement**: Double thickness option for sturdier panels
- **Improved UI/UX**: Modern dark theme, better HUD layout, tooltips, and responsive design

### 🎯 Behavior Improvements
- **Selection Mode**: Default click behavior now deselects all and selects single piece; Shift+click for multi-select
- **Layer Visibility**: Proper synchronization between piece visibility and border meshes
- **Session Management**: Robust save/load with localStorage, JSON import/export
- **Undo/Redo System**: Enhanced history management with Ctrl+Z/Ctrl+Y

### 🔧 Technical Enhancements
- **Performance**: Optimized rendering and mesh generation
- **Accessibility**: Better keyboard navigation and screen reader support
- **Cross-browser**: Improved compatibility across modern browsers
- **Code Structure**: Refactored for maintainability and new features

### 📁 Files
- `BABIQUES-HSW-GENERATOR-v2.0.0.html`: Complete rewrite with all new features

---

## Version 1.3.6c (2026-04-07)

### 🎯 Améliorations du comportement de sélection
- **Comportement de sélection amélioré** : Changement du mode de sélection par défaut
  - **Clic normal** : Désélectionne toutes les pièces et sélectionne uniquement la pièce cliquée
  - **Clic + Shift** : Mode multi-sélection (ajouter/retirer des pièces de la sélection actuelle)
  - Plus intuitif pour la plupart des cas d'usage

### 📁 Fichiers
- `BABIQUES-HSW-GENERATOR-v1.3.6c.html` : Version avec comportement de sélection amélioré

---

## Version 1.3.6b (2026-04-07)

### 🎨 Améliorations de l'interface utilisateur
- **Échange des couleurs de sélection** : Inversion des couleurs jaune et vert pour améliorer la lisibilité
  - Prévisualisation (survol) : contours **jaunes** pour indiquer qu'une pièce va être sélectionnée
  - Sélection active : contours **verts** pour indiquer qu'une pièce est sélectionnée
  - Changement appliqué aux contours et aux overlays transparents

### 📁 Fichiers
- `BABIQUES-HSW-GENERATOR-v1.3.6b.html` : Version officielle avec améliorations d'interface

---

## Version 1.3.6 (2026-04-06)

### ✨ Corrections majeures
- **Correction de la visibilité des bordures épaissies** : Les épaisseurs doublées respectent maintenant la visibilité des calques individuels
  - Les bordures épaissies des calques cachés ne restent plus visibles quand d'autres calques sont rendus visibles
  - Synchronisation automatique entre visibilité des pièces et de leurs bordures épaissies
  - Création conditionnelle des borderMeshes selon la visibilité du calque

### 🔧 Corrections techniques
- Modification de `addBorderMesh()` pour vérifier la visibilité du calque avant ajout à la scène
- Extension de `applyLayerVisibilityToPiece()` pour gérer la visibilité des borderMeshes
- Amélioration de `setLayerVisibility()` pour créer les borderMeshes manquants lors de l'activation d'un calque

### 📁 Fichiers
- `BABIQUES-HSW-GENERATOR-v1.3.6.html` : Version officielle avec corrections intégrées
- `README-border-fix.md` : Documentation des corrections apportées

---

## Version 1.3.5 (2026-04-06)

### ✨ Corrections majeures
- **Résolution des pièces corrompues après déplacement** : Correction des problèmes de Map JavaScript causant des corruptions lors de grands déplacements de groupes
- **Amélioration de la robustesse du système de sélection** : Bypasse des Maps corrompus pour la détection de clics et l'affichage des highlights

### 🔧 Corrections techniques
- Raycasting indépendant des Maps dans `handleClick()`
- Fonction de secours dans `highlightSinglePiece()` pour retrouver les meshes
- Nettoyage robuste des highlights avec `scene.traverse()`

---

## Version 1.3.4a (2026-04-05)

### ✨ Fonctionnalités
- Version de développement avec corrections partielles

---

## Versions précédentes (1.3.0 - 1.3.4)
- Développement initial et corrections mineures
- Système de calques et bordures épaissies
- Interface utilisateur et contrôles
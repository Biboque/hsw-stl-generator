# 🐝 Babique's HSW Generator – Free browser-based STL generator for the Honeycomb Storage Wall system

Hey everyone! I've been using the **HSW (Honeycomb Storage Wall)** system by [@RostaP](https://www.printables.com/model/152592-honeycomb-storage-wall) for a while and wanted a faster way to design custom panels. So I built a tool: a **single HTML file** that runs entirely in your browser — no install, no account, no server.

🔗 **[teef-babique.top](https://teef-babique.top)**
*(or just download the HTML file and open it locally — it works offline too)*

---

## What is HSW?

The Honeycomb Storage Wall is a brilliant 3D-printable modular wall storage system. Hexagonal tiles click into a grid of wall-mounted panels, letting you organize tools, accessories, or whatever you need. If you haven't seen it yet, check out RostaP's original model on Printables.

---

## What does this generator do?

It lets you **paint a custom layout** on a hex grid and export it directly as a **printable STL file** — no OpenSCAD, no slicing software needed to generate the geometry.

### Shapes available

Each shape comes in 3 variants: **Hollow** (standard HSW slot), **Solid** (filler panel), and **Fixing** (screw hole for wall mounting).

| Shape | Description |
|---|---|
| **Hexagon** | Full hexagon |
| **Pentagon** | Half-hex on one side |
| **Trapezoid** | Bottom half of a hexagon |
| **Diamond** | Angled diamond shape (30°–150°) |
| **Shard** | Half-diamond (bottom-left fragment) |
| **Tier** | Third of a hexagon |
| **Quarter** | Quarter of a hexagon |
| **Triangle** | Sixth of a hexagon |

### Features

- 🖱️ **Click to place, right-click to remove** — or hold Space to paint, Ctrl to erase in bulk
- ↩️ **Undo / Redo** (Ctrl+Z / Ctrl+Y)
- 🪞 **Mirror tools** — flip your layout on X, Y or Z axis instantly
- 🔲 **Double thickness** — reinforces border cells for sturdier panels
- 💾 **Session save** — your work is saved locally in your browser
- 📤 **JSON export/import** — share or back up your layouts
- 📦 **STL export** — ready to slice and print
- 📐 **Live stats** — element count and panel dimensions update in real time
- 🌐 **FR / EN** — toggle language in one click
- 🔭 **3D preview** — switch between perspective and orthographic view, orbit, zoom, pan

### Technical details

- Built as a **single self-contained HTML file** (~3400 lines)
- Uses **Three.js** (loaded from CDN) for 3D rendering and STL export
- 100% client-side — **no data collected, no server, no tracking**
- Sessions saved in `localStorage`
- Works in any modern browser (Chrome, Firefox, Edge, Safari)

---

## How to use it

1. Open the tool (online or locally)
2. Select a shape and variant from the sidebar
3. Click on the hex grid to place pieces
4. Use Mirror, Double thickness or Eraser as needed
5. Hit **Export STL** — done!

### Keyboard shortcuts

| Action | Shortcut |
|---|---|
| Undo | Ctrl+Z |
| Redo | Ctrl+Y |
| Place one piece | Click |
| Erase one piece | Right click |
| Paint mode | Space + hover |
| Erase mode | Ctrl + hover |
| Lock rotation | Shift + hover |
| Zoom | Wheel |
| Pan | Right click + move |
| Toggle perspective | P |
| Center view | F |

---

## Credits & license

- HSW system originally designed by **@RostaP** — [Printables](https://www.printables.com/model/152592-honeycomb-storage-wall)
- Inspired by [HSW Designer by perplexinglabs](https://gridfinity.perplexinglabs.com/pr/hsw/0/0) and the [Customizable HSW OpenSCAD model](https://www.printables.com/model/380870-customizable-honeycomb-storage-wall-openscad/files)
- Generator made by **Babique** — licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) (free for personal, non-commercial use)

If you find it useful, there's a Ko-fi link on the page 🙂

---

*Happy to hear feedback, bug reports, or shape requests in the comments!*

---

## Changelog

### v1.2.1
- Fixed mirror system for Diamond and Shard shapes
- Fixed Diamond shape rendering in debug mirror tool
- Added Diamond and Shard to `INDEXED_PREFIXES` and `remapIndexedType`

### v1.2.0
- Added **Diamond** shape (Hollow, Solid, Fixing)
- Added **Shard** shape (Hollow, Solid, Fixing)
- New icons for Diamond and Shard buttons
- Added debug mirror tool for testing shape reflections
- Fixed mirror maps for Shard

---

## Changelog

### v1.2.1
- Fixed mirror system for Diamond and Shard shapes
- Fixed Diamond shape rendering in debug mirror tool
- Added Diamond and Shard to `INDEXED_PREFIXES` and `remapIndexedType`

### v1.2.0
- Added **Diamond** shape (Hollow, Solid, Fixing)
- Added **Shard** shape (Hollow, Solid, Fixing)
- New icons for Diamond and Shard buttons
- Added debug mirror tool for testing shape reflections
- Fixed mirror maps for Shard

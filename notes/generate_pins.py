#!/usr/bin/env python3
"""
Génère des visuels de pins Pinterest (1000x1500px) à partir des photos déjà utilisées
sur le blog, avec le titre du pin en overlay texte lisible sur fond assombri.

Usage : /tmp/pinvenv/bin/python3 notes/generate_pins.py
Sortie : notes/pins-output/<slug>.jpg
"""

import os
import textwrap
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = os.path.join(ROOT, "src", "assets")
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pins-output")

FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REGULAR = "/System/Library/Fonts/Supplemental/Arial.ttf"

W, H = 1000, 1500
BRAND = "Chat d'Appartement"

# (slug, image source, titre du pin — voir notes/pinterest-pins.md pour le texte complet)
PINS = [
    ("amenager-coin-chat-petit-appartement", "blog-cat-house.jpg",
     "Aménager un coin pour son chat dans un petit appartement"),
    ("avis-petlibro-polar", "blog-petlibro-polar.jpg",
     "PETLIBRO Polar : mon avis après 2 semaines"),
    ("chat-appartement-canicule", "blog-heat-wave.jpg",
     "Canicule et chat d'appartement : les astuces qui marchent"),
    ("chat-appartement-rentree-retour-bureau", "blog-return-work-cat.jpg",
     "Rentrée : aider son chat à retrouver ses repères"),
    ("chat-griffe-canape-malgre-griffoir", "blog-sofa-mark.jpg",
     "Chat qui griffe le canapé malgré le griffoir : pourquoi ?"),
    ("chat-miaule-nuit-appartement-causes-solutions", "blog-meow-cat.jpg",
     "Chat qui miaule la nuit : causes et solutions"),
    ("chat-ne-boit-pas-assez-eau", "blog-cat-drink-water.jpg",
     "Mon chat ne boit pas assez : comment l'encourager"),
    ("chat-prend-poids-appartement", "blog-food-cat.jpg",
     "Chat en surpoids en appartement : causes et solutions"),
    ("chat-sennuie-signes-solutions", "blog-cat-bored.jpg",
     "Chat qui s'ennuie : les signes à repérer"),
    ("chat-urine-hors-litiere-causes-solutions", "blog-litter-cat-2.jpg",
     "Chat qui urine hors de la litière : causes et solutions"),
    ("combien-temps-chat-seul-appartement", "blog-cat-alone.jpg",
     "Combien de temps laisser un chat seul en appartement ?"),
    ("enlever-poils-chat-canape-vetements-lit", "blog-cat-hair.jpg",
     "Poils de chat : comment les enlever partout dans la maison"),
    ("enrichir-territoire-chat-appartement", "chaton-hero-appartement.jpg",
     "Le guide complet pour enrichir le territoire de son chat"),
    ("introduire-deuxieme-chat-appartement", "blog-two-cats.jpg",
     "Adopter un 2e chat : réussir la présentation en appartement"),
    ("meilleur-arbre-a-chat-appartement", "blog-cat-tree.jpg",
     "Bien choisir son arbre à chat pour un appartement"),
    ("meilleur-distributeur-croquettes-anti-glouton", "blog-keeble-dispenser.jpg",
     "Le guide du distributeur de croquettes anti-glouton"),
    ("meilleur-griffoir-mural-appartement", "blog-griffoir-mural.jpg",
     "Préserver ses meubles : le guide du griffoir mural"),
    ("meilleure-litiere-anti-odeurs-appartement", "blog-litter-cat.jpg",
     "La meilleure litière anti-odeurs pour un appartement"),
    ("occuper-chat-seul-appartement", "blog-cat-bored.jpg",
     "Comment occuper un chat seul toute la journée"),
    ("plantes-toxiques-chat-appartement", "blog-toxic-plant.jpg",
     "Plantes toxiques pour les chats : la liste à connaître"),
    ("securiser-fenetres-balcon-chat-appartement", "blog-window-secure.jpg",
     "Sécuriser fenêtres et balcon pour un chat d'intérieur"),
]


def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def fit_cover(img, target_w, target_h):
    """Recadre l'image en 'cover' pour remplir exactement target_w x target_h."""
    src_ratio = img.width / img.height
    target_ratio = target_w / target_h
    if src_ratio > target_ratio:
        new_height = target_h
        new_width = int(new_height * src_ratio)
    else:
        new_width = target_w
        new_height = int(new_width / src_ratio)
    img = img.resize((new_width, new_height), Image.LANCZOS)
    left = (new_width - target_w) // 2
    top = (new_height - target_h) // 2
    return img.crop((left, top, left + target_w, top + target_h))


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def generate_pin(slug, source_image, title):
    src_path = os.path.join(ASSETS, source_image)
    img = Image.open(src_path).convert("RGB")
    img = fit_cover(img, W, H)

    # Overlay dégradé sombre en bas pour la lisibilité du texte
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    gradient_height = int(H * 0.6)
    for i in range(gradient_height):
        alpha = int(235 * (i / gradient_height) ** 1.3)
        y = H - gradient_height + i
        draw_overlay.line([(0, y), (W, y)], fill=(0, 0, 0, alpha))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)

    draw = ImageDraw.Draw(img)

    # Titre du pin
    title_font = load_font(FONT_BOLD, 64)
    max_text_width = W - 120
    lines = wrap_text(draw, title, title_font, max_text_width)
    line_height = 76
    total_text_height = len(lines) * line_height
    y = H - 180 - total_text_height

    for line in lines:
        text_width = draw.textlength(line, font=title_font)
        x = (W - text_width) / 2
        # Léger contour noir pour renforcer la lisibilité sur tout type de fond
        for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
            draw.text((x + dx, y + dy), line, font=title_font, fill=(0, 0, 0, 255))
        draw.text((x, y), line, font=title_font, fill=(255, 255, 255, 255))
        y += line_height

    # Bandeau nom de marque en bas (pas d'emoji : Arial standard ne les rend pas)
    brand_font = load_font(FONT_REGULAR, 34)
    brand_text = BRAND.upper()
    brand_width = draw.textlength(brand_text, font=brand_font)
    draw.text(((W - brand_width) / 2, H - 90), brand_text, font=brand_font, fill=(255, 255, 255, 230))

    os.makedirs(OUTPUT, exist_ok=True)
    out_path = os.path.join(OUTPUT, f"{slug}.jpg")
    img.convert("RGB").save(out_path, quality=90)
    print(f"✓ {out_path}")


if __name__ == "__main__":
    for slug, source_image, title in PINS:
        generate_pin(slug, source_image, title)

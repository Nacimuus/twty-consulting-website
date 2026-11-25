# twty.fr — Twty Consulting / Nacim Touenti

Site statique bilingue (FR principal, EN dans `/en/`), hébergé sur GitHub Pages (www.twty.fr).

## Modifier le contenu

Les pages HTML sont générées. Ne modifiez pas directement les `.html` à la racine ou dans `/en/` :

1. Éditez le texte dans `_build/content_fr.py` (français) ou `_build/content_en.py` (anglais).
   Les coordonnées (email, téléphones, LinkedIn, lien de prise de RDV) sont dans `_build/site_config.py`.
2. Régénérez le site depuis la racine du dépôt :

   ```
   python3 _build/build.py
   ```

3. Vérifiez en local : `python3 -m http.server` puis ouvrez http://localhost:8000
4. Commitez les fichiers générés.

Le générateur produit aussi `sitemap.xml`, `robots.txt`, `llms.txt` et des pages de redirection
pour les anciennes URL (`services.html`, `payment-systems.html`, `training.html`…).

## Structure

- `assets/css/site.css` : styles (thème sombre bleu canard et or, polices Unbounded et Manrope)
- `assets/js/site.js` : fond animé, étincelles des boutons, apparitions au défilement, menu mobile, formulaire de contact
- `assets/img/` : images WebP optimisées, logo, image de partage `og-twty.jpg`
- `Nacim.html` : page de profil NFC (non indexée), indépendante du reste du site
  (styles `assets/css/nacim.css`, script `assets/js/nacim.js`, contact `assets/vcards/nacim.vcf`).
  Bilingue FR/EN selon la langue du téléphone. Pour la photo, voir le commentaire dans `Nacim.html`.

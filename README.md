# Chat d'Appartement — blog

Blog Astro sur le thème des chats d'appartement, monétisé via publicité (Google AdSense) et liens
d'affiliation (Amazon Associates, etc.), déployé sur Netlify.

## Démarrage rapide

```sh
npm install
npm run dev
```

Le site tourne alors sur `http://localhost:4321`.

## Commandes

| Commande           | Action                                              |
| :------------------ | :--------------------------------------------------- |
| `npm install`        | Installe les dépendances                             |
| `npm run dev`         | Lance le serveur de dev sur `localhost:4321`          |
| `npm run build`       | Build le site en statique/SSR dans `./dist/`          |
| `npm run preview`     | Prévisualise le build en local avant déploiement      |
| `npm run astro ...`   | Commandes CLI Astro (`astro add`, `astro check`, ...) |

## Structure du projet

```text
├── public/                   fichiers statiques (favicon, robots.txt à ajouter)
├── src/
│   ├── assets/                images et polices
│   ├── components/            composants Astro réutilisables
│   │   ├── AffiliateLink.astro   lien d'affiliation (rel="sponsored nofollow")
│   │   └── AdSlot.astro          emplacement pub AdSense (inactif tant que ADSENSE_CLIENT_ID est vide)
│   ├── content/blog/           articles (Markdown / MDX)
│   ├── layouts/BlogPost.astro  gabarit d'article
│   ├── pages/                  routes du site (accueil, blog, about, pages légales)
│   └── consts.ts               titre, description, identifiants pub/affiliation
├── astro.config.mjs           config Astro + intégrations (mdx, sitemap, netlify)
├── netlify.toml                config de build Netlify
└── package.json
```

## Avant la mise en ligne : checklist monétisation

1. **`src/consts.ts`**
   - Renseigner `ADSENSE_CLIENT_ID` une fois le compte Google AdSense créé et le site validé.
   - Renseigner `AMAZON_AFFILIATE_TAG` (ou utiliser directement vos liens complets dans les articles).
   - Vérifier `SITE_OWNER_NAME` / `SITE_CONTACT_EMAIL`.
2. **Pages légales** (`src/pages/mentions-legales.astro`, `politique-de-confidentialite.astro`) :
   compléter les champs marqués `<em>À compléter avant mise en ligne</em>` (adresse, SIRET le cas
   échéant, bannière de consentement cookies RGPD — obligatoire dès qu'AdSense est actif en UE).
3. **Bannière de consentement cookies (CMP)** : à intégrer avant d'activer AdSense pour les
   visiteurs européens (ex. Axeptio, Didomi, Cookiebot, ou la solution CMP intégrée d'AdSense).
4. **Programme d'affiliation** : demander l'accès au [Programme Partenaires
   Amazon](https://partenaires.amazon.fr/) (ou autre régie d'affiliation) puis remplacer les `href`
   d'exemple dans les articles par vos vrais liens trackés.
5. **Google AdSense** : créer un compte sur [adsense.google.com](https://www.google.com/adsense/),
   soumettre le site une fois qu'il a du contenu et du trafic, attendre validation avant d'activer
   `ADSENSE_CLIENT_ID`.
6. **`astro.config.mjs`** : mettre à jour `site` avec le nom de domaine définitif (nécessaire pour
   un sitemap et des URLs canoniques corrects).
7. Ajouter un `public/robots.txt` si besoin de règles spécifiques (par défaut tout est indexable).

## Ajouter un article

Créer un fichier dans `src/content/blog/mon-article.md` (ou `.mdx` si vous avez besoin d'utiliser
des composants comme `<AffiliateLink />`) avec le frontmatter suivant :

```yaml
---
title: 'Titre de l’article'
description: 'Résumé pour le SEO et les réseaux sociaux'
pubDate: 2026-07-15
heroImage: '../../assets/mon-image.jpg' # optionnel
---
```

Pour insérer un lien d'affiliation dans un article `.mdx` :

```mdx
import AffiliateLink from '../../components/AffiliateLink.astro';

<AffiliateLink href="https://www.amazon.fr/dp/XXXXXXXXX?tag=VOTRE-TAG-21" label="Voir le produit" />
```

## Déploiement sur Netlify

Le projet utilise déjà l'adaptateur `@astrojs/netlify` (SSR léger, principalement pour les
sessions/fonctions futures — la majorité des pages restent pré-rendues en statique).

### Option A — via l'interface Netlify (recommandé pour démarrer)

1. Pousser ce dossier sur un dépôt GitHub/GitLab.
2. Sur [app.netlify.com](https://app.netlify.com/), **Add new site → Import an existing project**.
3. Sélectionner le dépôt. Netlify détecte automatiquement la config Astro (`netlify.toml` fourni) :
   - Build command : `npm run build`
   - Publish directory : `dist`
4. Déployer. Le site est alors accessible sur `<nom>.netlify.app`.
5. Une fois un nom de domaine acheté, le brancher dans **Site configuration → Domain management**,
   puis mettre à jour `site` dans `astro.config.mjs`.

### Option B — via la CLI Netlify

```sh
npm install -g netlify-cli
netlify login
netlify init      # relie le dossier local à un site Netlify (nouveau ou existant)
netlify deploy --build           # déploiement de prévisualisation
netlify deploy --build --prod    # déploiement en production
```

## Pour aller plus loin

- [Documentation Astro](https://docs.astro.build)
- [Déploiement Astro sur Netlify](https://docs.astro.build/en/guides/deploy/netlify/)
- [Content Collections Astro](https://docs.astro.build/en/guides/content-collections/)
- [Google AdSense — bien démarrer](https://support.google.com/adsense/answer/9724)
- [Programme Partenaires Amazon](https://partenaires.amazon.fr/)

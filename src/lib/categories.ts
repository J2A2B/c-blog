// Configuration des pages de catégorie (/blog/categorie/[tag]/).
//
// Chaque article a un champ `tags` (voir src/content.config.ts), mais tous les tags ne
// méritent pas leur propre page :
// - "chat-appartement" est présent sur quasiment tous les articles (trop générique)
// - "conseils" est trop vague pour constituer une vraie catégorie éditoriale
// Ces deux tags sont donc volontairement exclus des pages de catégorie.
//
// "comparatif" et "matériel" apparaissent quasi toujours ensemble sur les guides d'achat :
// plutôt que deux pages redondantes, ils sont regroupés sous une seule catégorie
// "Guides d'achat" (slug "guides-achat").
//
// Pour ajouter une nouvelle catégorie : ajoute une entrée dans CATEGORY_CONFIG avec le(s)
// tag(s) source(s), un slug d'URL, un titre et une intro éditoriale courte. Un nouveau tag
// thématique qui n'a pas d'entrée ici n'aura simplement pas de page de catégorie générée
// (et ne sera pas affiché comme lien cliquable sur les articles).

export interface CategoryConfig {
	/** Identifiant d'URL : la page est générée sur /blog/categorie/{slug}/ */
	slug: string;
	/** Nom affiché dans les titres, breadcrumbs, etc. */
	label: string;
	/** Titre <title>/H1 optimisé SEO pour la page de catégorie. */
	pageTitle: string;
	/** Meta description de la page de catégorie. */
	pageDescription: string;
	/** Intro éditoriale (2-3 phrases) affichée en haut de la page de catégorie. */
	intro: string;
	/** Tag(s) bruts des articles qui alimentent cette catégorie. */
	tags: string[];
}

export const CATEGORY_CONFIG: CategoryConfig[] = [
	{
		slug: 'comportement',
		label: 'Comportement',
		pageTitle: "Comportement du chat d'appartement : tous nos articles",
		pageDescription:
			"Miaulements nocturnes, griffades, ennui, agressivité, cohabitation entre chats... nos guides pour comprendre et accompagner le comportement d'un chat qui vit exclusivement en intérieur.",
		intro:
			"Un chat 100% intérieur n'a pas les mêmes exutoires qu'un chat qui sort librement : ses comportements — miaulements, griffades, agitation nocturne, ennui — s'expriment autrement et demandent une lecture adaptée. Cette catégorie rassemble nos articles pour comprendre ce que ton chat essaie de te dire et l'accompagner au quotidien en appartement.",
		tags: ['comportement'],
	},
	{
		slug: 'sante',
		label: 'Santé',
		pageTitle: "Santé du chat d'appartement : tous nos articles",
		pageDescription:
			"Poids, hydratation, canicule et autres sujets de santé propres à la vie en intérieur : nos guides pour surveiller et préserver le bien-être physique de ton chat d'appartement.",
		intro:
			"La vie en intérieur expose un chat à des risques spécifiques : sédentarité, prise de poids, hydratation insuffisante ou vulnérabilité aux fortes chaleurs. Cette catégorie regroupe nos articles pour repérer les signes d'alerte et adopter les bons réflexes santé au quotidien.",
		tags: ['santé'],
	},
	{
		slug: 'guides-achat',
		label: "Guides d'achat",
		pageTitle: "Guides d'achat pour chat d'appartement : comparatifs et tests",
		pageDescription:
			"Arbres à chat, griffoirs muraux, litières, distributeurs de croquettes, fontaines à eau... nos comparatifs et tests de matériel pensés pour la vie en appartement.",
		intro:
			"Bien choisir son matériel change vraiment le quotidien d'un chat d'intérieur, à condition de sélectionner des produits adaptés aux contraintes d'un appartement (espace réduit, odeurs, bruit). Retrouve ici tous nos comparatifs et tests pour équiper ton chat sans te tromper.",
		tags: ['comparatif', 'matériel'],
	},
	{
		slug: 'securite',
		label: 'Sécurité',
		pageTitle: "Sécurité du chat d'appartement : tous nos articles",
		pageDescription:
			"Fenêtres, balcons, plantes toxiques : nos guides pour sécuriser un intérieur et éviter les accidents domestiques chez un chat qui vit en appartement.",
		intro:
			"Un appartement recèle des dangers propres au cadre de vie du chat d'intérieur : fenêtres oscillo-battantes, balcons, plantes toxiques à portée de patte. Cette catégorie réunit nos articles pour sécuriser ton logement et prévenir les accidents évitables.",
		tags: ['sécurité'],
	},
	{
		slug: 'plantes',
		label: 'Plantes',
		pageTitle: "Plantes et chat d'appartement : tous nos articles",
		pageDescription:
			"Quelles plantes d'intérieur sont dangereuses pour un chat et lesquelles privilégier : nos articles pour concilier végétation d'intérieur et sécurité féline.",
		intro:
			"Beaucoup de plantes d'intérieur populaires sont toxiques pour les chats, parfois gravement. Cette catégorie rassemble nos articles pour savoir lesquelles éviter et comment aménager un intérieur végétalisé sans risque pour ton chat.",
		tags: ['plantes'],
	},
];

/** Tags volontairement exclus des pages de catégorie (trop génériques). */
export const EXCLUDED_TAGS = ['chat-appartement', 'conseils'];

/** Retrouve la config de catégorie correspondant à un tag brut d'article, si elle existe. */
export function getCategoryForTag(tag: string): CategoryConfig | undefined {
	return CATEGORY_CONFIG.find((cat) => cat.tags.includes(tag));
}

# This file has not been used yet!
# This is for store strings in perfect hashing table, so the first step needs to convert the string into integer 
numWords = 1000
words =  [
"abbots",
"abdicate",
"abhorrent",
"absolutist",
"absolutists",
"abstract",
"accomplish",
"accumulate",
"acquittal",
"acres",
"actual",
"adults",
"adventurously",
"aeolian",
"affixes",
"agakhan",
"aid",
"alining",
"alleles",
"almshouses",
"altitudes",
"alto",
"ambassadorial",
"amenity",
"ammonium",
"amputee",
"anarchy",
"anatomists",
"ancestries",
"anise",
"annal",
"antagonist",
"antennas",
"anthologise",
"apertures",
"appointing",
"apron",
"arbitrators",
"arcana",
"arcane",
"archaeologists",
"arrested",
"artfully",
"ascending",
"asked",
"aspersion",
"aspirations",
"assailant",
"assents",
"assessor",
"assimilation",
"assortments",
"assuaged",
"astronomic",
"asylums",
"asymptotic",
"atrocities",
"attorneys",
"auctioning",
"audit",
"aupair",
"austerely",
"autarchy",
"authenticating",
"avenge",
"avenue",
"avidly",
"baker",
"banked",
"banshees",
"barber",
"basest",
"behaves",
"belie",
"benignly",
"besides",
"besieging",
"betoken",
"betroths",
"biassing",
"biblicists",
"bibliographical",
"biceps",
"bigamous",
"billings",
"billowing",
"bird",
"birthrights",
"bison",
"blackshirts",
"blended",
"blizzard",
"blob",
"bloodier",
"bloodstream",
"blow",
"boardgames",
"boardroom",
"bobbies",
"bonny",
"booby",
"bored",
"borne",
"borneo",
"bosnia",
"bowls",
"boyishly",
"bracer",
"brainstorm",
"breakdowns",
"briny",
"broaching",
"brooks",
"brow",
"brunches",
"buggered",
"bunyan",
"burghers",
"burials",
"buries",
"burlesque",
"burrow",
"butts",
"bylaw",
"cabman",
"cacti",
"calipers",
"calve",
"camouflage",
"canard",
"canaries",
"canonry",
"carboniferous",
"career",
"caver",
"ceded",
"celebrations",
"cemeteries",
"censored",
"centimes",
"centrifugation",
"certainties",
"chalks",
"chamomile",
"characterful",
"charades",
"charter",
"chastisement",
"cheapskates",
"cheats",
"checkered",
"cheeseburgers",
"cheesemaking",
"chipboard",
"chopin",
"chopper",
"chops",
"chorale",
"choristers",
"chromosomal",
"chuckles",
"cinematographer",
"citruses",
"clavichord",
"clerics",
"climatologists",
"cloakrooms",
"cloistered",
"closedcircuit",
"closures",
"clumber",
"clutters",
"coders",
"codifying",
"coiffure",
"coinciding",
"coins",
"collectives",
"collieries",
"collinear",
"combustibles",
"comedown",
"comfortingly",
"commendably",
"compares",
"complexities",
"concerned",
"concerts",
"conclusion",
"conditionality",
"conducted",
"confess",
"confidentiality",
"confuse",
"congeniality",
"conglomerates",
"congruences",
"conjoined",
"conquer",
"conservatives",
"consigns",
"consoles",
"consonant",
"consorted",
"construing",
"consumerism",
"contentment",
"continuities",
"contract",
"contributes",
"contritely",
"controller",
"convects",
"conventicle",
"conveyancing",
"conveys",
"cornices",
"corporal",
"cosmetic",
"cotton",
"couloir",
"counteracting",
"counterpointed",
"countrymen",
"coxcomb",
"coxes",
"craftiest",
"creamery",
"credence",
"creeper",
"cretins",
"cribs",
"cringes",
"cripple",
"croons",
"crossbars",
"crossexamination",
"crucifix",
"crueler",
"cruises",
"crusaded",
"cuttingly",
"cycling",
"czar",
"daisy",
"damnify",
"danced",
"darkly",
"debited",
"decaffeinated",
"decelerate",
"declassification",
"declined",
"decriminalising",
"deductible",
"defy",
"degas",
"deism",
"demeaned",
"den",
"dendrochronological",
"dermatology",
"dermic",
"deserters",
"designing",
"detractor",
"devilishly",
"dews",
"diagonalised",
"dichotomy",
"dictatorially",
"diffuser",
"dimmest",
"directing",
"disaggregation",
"disassociated",
"disaster",
"disclaimed",
"disclaiming",
"discolour",
"discontent",
"discussion",
"disillusion",
"disparity",
"disrespect",
"dissimilarities",
"dissimilarity",
"dissipating",
"dissociative",
"distantly",
"distension",
"distributable",
"divergent",
"diversification",
"documenting",
"dome",
"domed",
"domes",
"domination",
"domino",
"dormitory",
"doubly",
"dovecote",
"dozy",
"drags",
"draughtsmanship",
"dray",
"dressings",
"dressmaking",
"drill",
"drones",
"duality",
"dullest",
"dungeon",
"dunghill",
"duodenum",
"duplicability",
"dwelling",
"ear",
"ecclesiastic",
"ecologist",
"editing",
"educationally",
"educative",
"effulgent",
"eigenvalues",
"eire",
"elect",
"electric",
"electromagnet",
"electron",
"elk",
"embassy",
"emissivity",
"encamp",
"encephalopathy",
"endomorphism",
"engendered",
"engulf",
"enthrone",
"enthusiasm",
"entice",
"entrance",
"entrepreneurship",
"enumerator",
"epinephrine",
"epsilon",
"equivocal",
"era",
"erecter",
"escarpment",
"esplanade",
"esquires",
"exalts",
"excavate",
"excerpt",
"excess",
"excuse",
"executable",
"expansively",
"expatriates",
"expertness",
"explicate",
"extolling",
"extra",
"extracted",
"extragalactic",
"extraordinarily",
"exults",
"fable",
"facsimiles",
"factorise",
"falls",
"falsifying",
"fared",
"fascia",
"fashion",
"fastens",
"featuring",
"feinting",
"felling",
"fencings",
"ferment",
"fetes",
"fettered",
"feuded",
"fifes",
"finalise",
"finch",
"findings",
"fingerless",
"finisher",
"fireproofed",
"fireside",
"flabby",
"flamboyant",
"flexion",
"flintlocks",
"floater",
"flyaway",
"fobbed",
"folds",
"footmen",
"forename",
"forenames",
"forensically",
"forgeries",
"fortified",
"forwarder",
"foundation",
"foxtrots",
"frankfurter",
"freehand",
"frictions",
"frivolities",
"frond",
"furnishing",
"futilely",
"gadding",
"gaging",
"galactic",
"gale",
"gallic",
"gambit",
"gangling",
"gangrene",
"garbles",
"garlanded",
"gasholder",
"gating",
"gaucherie",
"gelatine",
"geochemical",
"germanic",
"gerund",
"gibed",
"girlishness",
"glace",
"glans",
"gleanings",
"gleefulness",
"glittered",
"glowers",
"gluey",
"gnostic",
"goodhope",
"gouging",
"governments",
"grafting",
"grail",
"grandpas",
"grantee",
"granulocyte",
"grasp",
"greece",
"grew",
"groomers",
"gropingly",
"ground",
"groundsheet",
"guava",
"guessable",
"guzzlers",
"hackneyed",
"haemophiliacs",
"haitian",
"hallucinations",
"haloed",
"haltered",
"hammered",
"hammers",
"hankered",
"hardly",
"hasnt",
"headlamp",
"headmastership",
"healthful",
"heartbreak",
"heathenism",
"heathers",
"heathland",
"hectoring",
"heeding",
"heightening",
"helpings",
"hermeneutic",
"hikers",
"hinnies",
"hinting",
"histologically",
"hollowed",
"homelier",
"homeowner",
"honeycombed",
"horrendous",
"horsey",
"horticultural",
"houston",
"huffy",
"hunger",
"hyperboloid",
"hypocritical",
"ideologue",
"imagination",
"imbibe",
"immovable",
"imperialist",
"imperialistic",
"impression",
"imputed",
"inaptly",
"inconsiderable",
"incubator",
"inculcated",
"indescribable",
"indication",
"inductive",
"indulging",
"inelastic",
"inelegantly",
"infects",
"inferences",
"injecting",
"injudiciously",
"inkpad",
"innovate",
"inoculate",
"inoculation",
"inquisitors",
"insemination",
"insignificance",
"insolvency",
"inspecting",
"instantaneously",
"interception",
"interchange",
"interdependence",
"internationalists",
"internationally",
"interpolate",
"interpreting",
"interrupted",
"interstices",
"intervention",
"intone",
"invaders",
"investiture",
"inviolate",
"irks",
"ironmongers",
"irons",
"issuable",
"itinerants",
"jailing",
"jalopy",
"jockeying",
"jot",
"journeyed",
"journeys",
"judicature",
"jukeboxes",
"jumpier",
"junctions",
"kernels",
"keyboard",
"khaki",
"kilter",
"kindle",
"kitchen",
"kits",
"kleptomaniacs",
"knee",
"knuckling",
"kongo",
"kwachas",
"labellings",
"lacquers",
"laden",
"lancets",
"lapdogs",
"lapped",
"lawbreaker",
"lawmen",
"layoffs",
"leafier",
"leathers",
"legatees",
"length",
"lengthening",
"lens",
"leper",
"levelled",
"lexicographical",
"liaising",
"libel",
"lifeboats",
"lightheadedness",
"limekiln",
"lit",
"locate",
"loitering",
"lonelier",
"lordship",
"lorry",
"louts",
"lovely",
"lowercase",
"lubber",
"ludicrousness",
"lugs",
"lustreless",
"luxuriant",
"lymphomas",
"made",
"madmen",
"magnetodynamics",
"mailing",
"majesties",
"manageable",
"manager",
"managership",
"manuscripts",
"maple",
"maquettes",
"margate",
"martens",
"masochists",
"masquerade",
"matches",
"materialistically",
"mathematicians",
"maturity",
"mean",
"meander",
"meaning",
"meatier",
"medium",
"medlar",
"megahertz",
"memory",
"mends",
"merchantmen",
"methane",
"microbial",
"microbiological",
"midas",
"middleclass",
"migrate",
"mildness",
"militancy",
"misbehaved",
"miscegenation",
"misspell",
"misuse",
"mitres",
"moat",
"mode",
"modernity",
"molts",
"monopole",
"monotheists",
"mooning",
"moonlight",
"mooring",
"moralist",
"morphogenetic",
"mortgages",
"motivational",
"motorised",
"mouthing",
"mouthparts",
"movable",
"munificent",
"mural",
"murmurings",
"museum",
"musicals",
"mustered",
"nethermost",
"neurotically",
"newlook",
"nitpicking",
"nominates",
"nominees",
"nosey",
"novelists",
"nozzles",
"nudities",
"nutritious",
"nutshell",
"objectors",
"obnoxious",
"obtrude",
"occident",
"occupying",
"occurs",
"oceanic",
"odiousness",
"omnibus",
"oner",
"onwards",
"oral",
"orphan",
"orphans",
"outcry",
"outflows",
"outgrew",
"outlined",
"outraging",
"outweigh",
"overcook",
"overfill",
"overpressure",
"overweening",
"padlocking",
"paleface",
"palliative",
"pampering",
"pampers",
"pane",
"panelled",
"papers",
"parallelograms",
"parchment",
"pardons",
"pastoral",
"patent",
"patrons",
"paunchy",
"paying",
"payrolls",
"pens",
"pensioning",
"peppered",
"perambulated",
"percussion",
"perish",
"permeated",
"personalisation",
"perspicuous",
"pesticides",
"petrology",
"pets",
"petticoat",
"phenomenon",
"phonemic",
"photogenic",
"picnic",
"piecemeal",
"pineapple",
"piper",
"pitch",
"pivot",
"planed",
"plexus",
"ploy",
"plucker",
"pocketful",
"polishes",
"politician",
"polkas",
"polycyclic",
"polymerase",
"polyps",
"poplars",
"populace",
"population",
"pore",
"porphyritic",
"portals",
"portcullises",
"possession",
"potent",
"power",
"praise",
"praising",
"preached",
"precis",
"preciseness",
"prefaces",
"preferable",
"preference",
"preferring",
"premolar",
"preposterous",
"pressings",
"printouts",
"probabilistically",
"problematical",
"proclaim",
"proficiency",
"prohibit",
"prohibits",
"promise",
"proposers",
"prospers",
"protean",
"puller",
"pupa",
"pupae",
"purgatorial",
"putt",
"pyjamas",
"pyridine",
"quadrupeds",
"qualifies",
"quarry",
"questionable",
"quiff",
"radioactively",
"radiotherapy",
"rainforests",
"rancour",
"rang",
"rankling",
"ransacking",
"rarer",
"rasped",
"ratification",
"rationale",
"rayon",
"realising",
"reanimated",
"rebooted",
"rebuffed",
"reciprocal",
"recoiled",
"recommendable",
"reconfigurations",
"recordings",
"recruited",
"recures",
"redecorated",
"redeposition",
"redirects",
"referrals",
"refine",
"reflection",
"reflex",
"reflux",
"reformulation",
"refraction",
"rehearsal",
"reheated",
"reinforced",
"reinterpreted",
"reiterating",
"relationship",
"relevance",
"relieve",
"relinquished",
"remained",
"remedies",
"reorder",
"reordered",
"repairing",
"repairman",
"repast",
"repents",
"repercussions",
"replicators",
"repopulated",
"reportedly",
"reposing",
"represent",
"repulsed",
"resend",
"residual",
"respond",
"restraining",
"retirement",
"retorts",
"retracting",
"retrieval",
"reunion",
"reverse",
"reverting",
"revoking",
"rewind",
"rhombuses",
"rifting",
"righthanded",
"rigorous",
"riots",
"ripeness",
"rivalled",
"rivers",
"roan",
"robbers",
"rockfall",
"roosts",
"roughing",
"roughly",
"rowdy",
"runniest",
"rustic",
"rustler",
"sacking",
"sacristy",
"sadomasochism",
"salespeople",
"salmon",
"saluted",
"sampan",
"sanctifying",
"sarong",
"satyr",
"saving",
"sawyers",
"scanners",
"schoolmistress",
"scintillator",
"scorched",
"scrapers",
"scratchiest",
"screamers",
"screaming",
"scrutineers",
"scythed",
"seabird",
"seal",
"seasoning",
"secretion",
"secretions",
"sectional",
"seductive",
"semesters",
"sent",
"septic",
"sequestrated",
"set",
"shakeup",
"shameless",
"sharer",
"shetland",
"shiveringly",
"shockers",
"shoddiness",
"shorted",
"shorten",
"shrouds",
"shun",
"shunter",
"shutters",
"shuttled",
"sidereal",
"sifting",
"sighting",
"signing",
"simmers",
"singable",
"sipper",
"sisterinlaw",
"skew",
"skimpy",
"skippering",
"skittle",
"sky",
"slag",
"slain",
"sledging",
"slick",
"slickest",
"slid",
"slithering",
"slobber",
"sloths",
"sluggards",
"sluicing",
"slung",
"smallish",
"smokiness",
"smudging",
"snapping",
"sneaking",
"sniffed",
"snippets",
"snobbishness",
"snoek",
"snowiest",
"snuffles",
"sobering",
"socialise",
"softy",
"solo",
"soso",
"spacers",
"spacious",
"specialist",
"specifically",
"spelling",
"spending",
"spinechilling",
"spirit",
"spiritedl",
"spoils",
"spooky",
"sprouts",
"sputnik",
"squashes"]
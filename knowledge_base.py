CLASS_NAMES = [
    "Rice Leaf Roller","Rice Leaf Caterpillar","Paddy Stem Maggot",
    "Asiatic Rice Borer","Yellow Rice Borer","Rice Gall Midge",
    "Rice Stemfly","Brown Plant Hopper","White Backed Plant Hopper",
    "Small Brown Plant Hopper","Rice Water Weevil","Rice Leafhopper",
    "Dragonfly","Ladybird Beetle","Spider"
]

# Minimal pest information used by the backend and frontend
pest_info = {
    "Rice Leaf Roller": {
        "impact": "Causes significant defoliation by rolling leaves, leading to 10-20% yield loss in severe infestations",
        "eggs": "Laid singly or in small groups on the underside of rice leaves, hatch in 4-6 days",
        "control": "Use pheromone traps for monitoring, encourage natural parasitoids, apply neem oil spray during early infestation, maintain proper field sanitation",
        "pesticide": "Spinosad (organic) or Lambda-cyhalothrin - highly effective against young larvae with minimal environmental impact"
    },
    "Rice Leaf Caterpillar": {
        "impact": "Larvae consume leaf tissues causing window-like holes, can reduce photosynthesis efficiency by 30-40%",
        "eggs": "Laid in clusters (20-30 eggs) on the underside of leaves, incubation period of 3-5 days",
        "control": "Spray neem solutions at early larval stage, manual removal of affected leaves, encourage natural enemies like wasps and spiders",
        "pesticide": "Neem oil or Bt (Bacillus thuringiensis) - organic options safe for beneficial insects and environment"
    },
    "Paddy Stem Maggot": {
        "impact": "Larvae tunnel inside stems causing wilting, deadhearts, and complete crop failure in severe cases",
        "eggs": "Laid near the base of rice stems in the soil, develop within 2-3 weeks into larvae",
        "control": "Practice field sanitation by removing crop residue, apply granular insecticides at tillering stage, use clean seeds and seedlings",
        "pesticide": "Fipronil or Carbofuran (granules) - systemic action controls soil-dwelling larvae and provides plant protection"
    },
    "Asiatic Rice Borer": {
        "impact": "Major pest causing 20-40% yield loss through stem boring, creates entry point for secondary infections",
        "eggs": "Laid on stems and leaves in groups covered with frass, hatch in 4-10 days depending on temperature",
        "control": "Plant resistant varieties, release natural enemies like Trichogramma wasps, avoid excessive nitrogen fertilizer",
        "pesticide": "Dichlorvos or Diflubenzuron - effective against eggs and early instars, prevents internal stem damage"
    },
    "Yellow Rice Borer": {
        "impact": "Severe pest causing 30-50% yield loss, more destructive than Asiatic borer in some regions",
        "eggs": "Laid on leaf sheaths in brown clusters, develop into larvae in 5-7 days",
        "control": "Targeted spraying during peak emergence, use pheromone traps for monitoring, maintain water in fields to reduce pest habitat",
        "pesticide": "Isoprocarb or Phenthoate - contact and stomach action pesticides effective during egg-laying and early instar stages"
    },
    "Rice Gall Midge": {
        "impact": "Forms abnormal galls on panicles preventing grain development, can cause 100% crop loss in susceptible varieties",
        "eggs": "Laid on flowering panicles, develop into larvae within developing galls",
        "control": "Use tolerant rice varieties, adjust planting dates to avoid pest emergence, remove affected panicles manually",
        "pesticide": "Diamethoate or Imidacloprid - systemic insecticides that translocate in plant tissue and control gall formation"
    },
    "Rice Stemfly": {
        "impact": "Causes stem infestation and internal damage, reduces tillering and grain filling",
        "eggs": "Laid near the base of rice plants in moist soil, larvae develop over 2-3 weeks",
        "control": "Crop rotation with non-host crops, maintain field sanitation, apply insecticides if threshold exceeded",
        "pesticide": "Chlorpyrifos or Triazophos - effective against newly hatched larvae before they enter the stem"
    },
    "Brown Plant Hopper": {
        "impact": "Sucks plant sap and transmits viral diseases like rice ragged stunt and rice grassy stunt viruses",
        "eggs": "Inserted into leaf sheaths and stems, have incubation period of 5-7 days",
        "control": "Proper water management to reduce hopper habitat, release natural enemies, use resistant varieties, yellow sticky traps",
        "pesticide": "Imidacloprid or Acetamiprid - systemic neo-nicotinoids that control population effectively and prevent disease transmission"
    },
    "White Backed Plant Hopper": {
        "impact": "Similar to brown plant hopper, transmits viruses and causes stunting and yellowing of rice plants",
        "eggs": "Laid on leaf sheaths and stems, hatch in 7-10 days",
        "control": "Biological control using parasitoid wasps, regular monitoring with sticky traps, avoid excessive nitrogen fertilizer",
        "pesticide": "Carbosulfan or Dimethoate - fast-acting insecticide that kills nymphs and adults before they transmit viruses"
    },
    "Small Brown Plant Hopper": {
        "impact": "Causes leaf yellowing, reduced plant vigor, and can transmit plant viruses in some regions",
        "eggs": "Laid on rice leaves, have development period of 6-8 days",
        "control": "Field sanitation to remove host plants, use reflective mulch, encourage natural predators and parasitoids",
        "pesticide": "Malathion or Quinalphos - broad-spectrum insecticide effective against hoppers at all growth stages"
    },
    "Rice Water Weevil": {
        "impact": "Adults chew on leaves causing shot-hole damage, larvae feed on roots causing stunting and yield loss",
        "eggs": "Laid in waterlogged soil near rice plants, larvae develop within soil over 2-3 weeks",
        "control": "Proper water management to dry fields periodically, use resistant varieties, apply systemic insecticides at seedling stage",
        "pesticide": "Carbofuran or Fipronil GR - granular formulations applied at soil level control root-feeding larvae effectively"
    },
    "Rice Leafhopper": {
        "impact": "Transmits tungro virus and other rice-limiting viruses, causes symptom expression and yield loss",
        "eggs": "Laid in leaf tissue, development period of 7-10 days depending on temperature",
        "control": "Use tungro-resistant rice varieties, control weeds hosting the pest, manage population with natural enemies",
        "pesticide": "Thiamethoxam or Imidacloprid - systemic insecticides that prevent virus transmission by killing leafhoppers"
    },
    "Dragonfly": {
        "impact": "Beneficial predator of mosquitoes and small insects, helps control pest populations naturally",
        "eggs": "Laid in or near water bodies, have aquatic nymph stage that lasts several months to years",
        "control": "Protect aquatic habitats and maintain water levels in fields to encourage dragonfly populations",
        "pesticide": "Not applicable - beneficial insect, do not use pesticides"
    },
    "Ladybird Beetle": {
        "impact": "Beneficial predator that feeds on aphids, scale insects, and mites, one beetle can consume 50+ pests daily",
        "eggs": "Laid on leaves, hatch in 3-4 days, larvae are highly voracious feeders",
        "control": "Avoid broad-spectrum insecticide sprays, maintain flowering plants for nectar and pollen, create beetle-friendly habitats",
        "pesticide": "Not applicable - beneficial insect, do not use pesticides"
    },
    "Spider": {
        "impact": "Highly beneficial predator that controls multiple pest species, one spider can consume 100+ pests per season",
        "eggs": "Protected in egg sacs on plants or under bark, multiple sacs per season",
        "control": "Encourage spider populations by avoiding pesticides, maintaining vegetation cover, creating refugia with plant debris",
        "pesticide": "Not applicable - beneficial insect, do not use pesticides"
    }
}






def text(self):
	
	zone = ['ses jambe','ses bras','sa tete','son torse','son dos']
	attack_zone = ['la droite','la gauche','le haut','le bas']



	self.description_text = """Un énorme robot quadripede vous a remarquez.\n
	Son enveloppe corporel change soudainement pour un rouge écarlate,\n
	ainsi qu'une vapeur brulante sort de plusieurs orifices sur son armures!\n\n
	Vous devez survivre par tout les moyens !\n"""

	self.attack_text = """Son armure semble impénétrable a première vue mais {} est resté d'une couleur jaune ?\n
	Des arcs électrique parcoure {}, pret a déviez sur vous""".format(true_zone, false_zone)
	#Utilise une liste composé de plusieurs [plusieurs parties de corps], pour décrire quel zone attaqué 

	self.afterattack_text  = """Vous lui explosé {} et un bruit méchanique difforme sort de son corp, comme si une partie ne répondé plus.\n""".format(true_zone)

	self.defense_text = """Attention ! Le robot vous attaque par {}.\n""".format(attack_zone)

	self.afterdefense_text = """Vous esquivez de justesse {} pret a vous écraser !""".format(zone)

	self.dead_text = """Des bouts de métal encore brulant jonchent le sol, certaine partie semble encore intacte et font encore des bruit étrange.\n"""


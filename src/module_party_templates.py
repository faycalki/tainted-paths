from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
	("none", "none", icon_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("rescued_prisoners", "Rescued Prisoners", icon_gray_knight|pf_label_small, 0, fac_commoners, courage_7|merchant_personality, []),

	("enemy", "Enemy", icon_gray_knight|pf_label_small, 0, fac_undeads, courage_7|merchant_personality, []),

	("kingdom_hero_party", "War Party", icon_gray_knight|pf_always_visible|pf_default_behavior|pf_show_faction, 0, fac_commoners, soldier_personality, []),

	("bandit_party", "Bandits", icon_axeman|pf_always_visible|pf_default_behavior|pf_show_faction, 0, fac_commoners, bandit_personality, []),

	("caravan_party", "Traders", icon_peasant|pf_always_visible|pf_default_behavior|pf_show_faction, 0, fac_commoners, courage_7|merchant_personality, []),

	("pirate_party", "Pirates", icon_axeman|pf_always_visible|pf_default_behavior|pf_show_faction, 0, fac_commoners, bandit_personality, []),

]
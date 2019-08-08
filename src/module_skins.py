from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1;
comp_greater_than = 1;

skins = [
	(
		"man", 0, "aman_body", "aman_calf_l", "am_handL", "male_head",
		[(20, 0, 0.7, -0.6, "Chin_Size"),
		(260, 0, -0.6, 1.4, "Chin_Shape"),
		(10, 0, -0.5, 0.9, "Chin_Forward"),
		(240, 0, 0.9, -0.8, "Jaw_Width"),
		(210, 0, -0.5, 1.0, "Jaw_Position"),
		(250, 0, 0.8, -1.0, "Mouth-Nose_Distance"),
		(200, 0, -0.3, 1.0, "Mouth_Width"),
		(50, 0, -1.5, 1.0, "Cheeks"),
		(60, 0, -0.4, 1.35, "Nose_Height"),
		(70, 0, -0.6, 0.7, "Nose_Width"),
		(80, 0, 1.0, -0.1, "Nose_Size"),
		(270, 0, -0.5, 1.0, "Nose_Shape"),
		(90, 0, -0.2, 1.4, "Nose_Bridge"),
		(100, 0, -0.3, 1.5, "Cheek_Bones"),
		(150, 0, -0.2, 3.0, "Eye_Width"),
		(110, 0, 1.5, -0.9, "Eye_to_Eye_Dist"),
		(120, 0, 1.9, -1.0, "Eye_Shape"),
		(130, 0, -0.5, 1.1, "Eye_Depth"),
		(140, 0, 1.0, -1.2, "Eyelids"),
		(160, 0, 1.3, -0.2, "Eyebrow_Position"),
		(170, 0, -0.1, 1.9, "Eyebrow_Height"),
		(220, 0, -0.1, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.1, 1.6, "Eyebrow_Shape"),
		(230, 0, 1.2, -0.7, "Temple_Width"),
		(30, 0, -0.6, 0.9, "Face_Depth"),
		(40, 0, 0.9, -0.6, "Face_Ratio"),
		(190, 0, 0.0, 0.95, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4", "man_hair_yu20", "man_hair_yu19", "man_hair_yu7", "man_hair_yu2", "man_hair_yu1", "man_hair_yu3", "man_hair_yu10", "man_hair_yu18", "man_hair_yu6", "man_hair_yu8", "man_hair_yu9", "man_hair_yu12", "man_hair_yu17", "man_hair_yu11", "man_hair_yu13", "man_hair_yu14", "man_hair_yu15", "man_hair_yu16", "man_hair_yu4", "man_hair_yu21", "man_hair_yu22", "man_hair_y2", "man_hair_y", "shoulderhair", "shortlayer", "shortcut", "shortbob", "hairmessy", "slickedback", "man_hair_r", "man_hair_s", "man_hair_bd_03", "man_hair_bd_04", "man_hair_bd_05", "man_hair_bd_06", "man_hair_yu20", "man_hair_yu19", "man_hair_yu17"],
		["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
		[
			("manface_young_2", 0xffcbe0e0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
			("manface_midage", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_young", 0xffd0e0e0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
			("manface_young_3", 0xffdceded, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
			("manface_7", 0xffc0c8c8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_midage_2", 0xfde4c8d8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
			("manface_rugged", 0xffb0aab5, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_african", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_asian1", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian2", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian3", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffaeb0a6, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2", 0xffd0c8c1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_white1", 0xffe0e8e8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
			("manface_mideast3", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_8", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_han", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_white1", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_white2", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_white3", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_black1", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
		"skel_human", 1.0, psys_game_blood, psys_game_blood_2,
		[
			[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
			[0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
			[1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
			[0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
			[0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
			[2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)]
		]
	),

	(
		"woman", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "norm_handL", "female_head",
		[(230, 0, 0.8, -1.0, "Chin_Size"),
		(220, 0, -1.0, 1.0, "Chin_Shape"),
		(10, 0, -1.2, 1.0, "Chin_Forward"),
		(20, 0, -0.6, 1.2, "Jaw_Width"),
		(40, 0, -0.7, 1.0, "Jaw_Position"),
		(270, 0, 0.9, -0.9, "Mouth-Nose_Distance"),
		(30, 0, -0.5, 1.0, "Mouth_Width"),
		(50, 0, -0.5, 1.0, "Cheeks"),
		(60, 0, -0.5, 1.0, "Nose_Height"),
		(70, 0, -0.5, 1.1, "Nose_Width"),
		(80, 0, 1.5, -0.3, "Nose_Size"),
		(240, 0, -1.0, 0.8, "Nose_Shape"),
		(90, 0, 0.0, 1.1, "Nose_Bridge"),
		(100, 0, -0.5, 1.5, "Cheek_Bones"),
		(150, 0, -0.4, 1.0, "Eye_Width"),
		(110, 0, 1.0, 0.0, "Eye_to_Eye_Dist"),
		(120, 0, -0.2, 1.0, "Eye_Shape"),
		(130, 0, -0.1, 1.6, "Eye_Depth"),
		(140, 0, -0.2, 1.0, "Eyelids"),
		(160, 0, -0.2, 1.2, "Eyebrow_Position"),
		(170, 0, -0.2, 0.7, "Eyebrow_Height"),
		(250, 0, -0.4, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.5, 1.2, "Eyebrow_Shape"),
		(260, 0, 1.0, -0.7, "Temple_Width"),
		(200, 0, -0.5, 1.0, "Face_Depth"),
		(210, 0, -0.5, 0.9, "Face_Ratio"),
		(190, 0, -0.4, 0.8, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_hair_song_02", "woman_hair_song_03", "woman_hair_song_04", "woman_hair_song_05", "woman_hair_song_06", "woman_hair_song_07", "woman_ren_hair_14", "straightshoulderrrr", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("dontknow_womanface3", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff0c0d19]),
			("Jed_Q_w_1", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
			("womanface_b2", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff0c0d19]),
			("dontknow_womanface4", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
			("dontknow_womanface1", 0xffe3e8ef, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
			("womanface_yiy_3", 0xffe3e8ef, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
			("womanface_hanhun_3", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_asia", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("Jed_Q_w_1", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("Jed_Q_w_1", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface3", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"male_another", 0, "aman_body", "aman_calf_l", "am_handL", "male_head2",
		[(240, 0, -0.4, 0.3, "Chin_Size"),
		(230, 0, -0.4, 0.8, "Chin_Shape"),
		(250, 0, -0.25, 0.55, "Chin_Forward"),
		(130, 0, -0.5, 1.0, "Jaw_Width"),
		(120, 0, -0.5, 0.6, "Lower_Lip"),
		(110, 0, -0.2, 0.6, "Upper_Lip"),
		(100, 0, 0.2, -0.2, "Mouth-Nose_Distance"),
		(90, 0, 0.55, -0.55, "Mouth_Width"),
		(30, 0, -0.3, 0.3, "Nostril_Size"),
		(60, 0, 0.25, -0.25, "Nose_Height"),
		(40, 0, -0.2, 0.3, "Nose_Width"),
		(70, 0, -0.3, 0.4, "Nose_Size"),
		(50, 0, 0.2, -0.3, "Nose_Shape"),
		(80, 0, -0.3, 0.65, "Nose_Bridge"),
		(160, 0, -0.2, 0.25, "Eye_Width"),
		(190, 0, -0.25, 0.15, "Eye_to_Eye_Dist"),
		(170, 0, -0.85, 0.85, "Eye_Shape"),
		(200, 0, -0.3, 0.7, "Eye_Depth"),
		(180, 0, -1.5, 1.5, "Eyelids"),
		(20, 0, 0.6, -0.25, "Cheeks"),
		(260, 0, -0.6, 0.5, "Cheek_Bones"),
		(220, 0, 0.8, -0.8, "Eyebrow_Height"),
		(210, 0, -0.75, 0.75, "Eyebrow_Shape"),
		(10, 0, -0.6, 0.5, "Temple_Width"),
		(270, 0, -0.3, 1.0, "Face_Depth"),
		(150, 0, -0.25, 0.45, "Face_Ratio"),
		(140, 0, -0.4, 0.5, "Face_Width"),
		(280, 0, 1.0, 1.0, "Post-Edit")],

		["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y1232312", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v222", "man_hair_ttttt", "man_hair_y666", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y1122", "man_hair_u3213", "man_hair_y312", "man_hair_y2", "man_hair_y4321", "man_hair_yu20", "man_hair_yu19", "man_hair_yu7", "man_hair_yu2312", "man_hair_yu1", "man_hair_yu3", "man_hair_yu10", "man_hair_yu1819", "man_hair_yu6", "man_hair_yu8", "man_hair_yu9", "man_hair_yu12", "man_hair_yu17", "man_hair_yu11312", "man_hair_yu13", "man_hair_yu141414", "man_hair_yu15", "man_hair_yu16", "man_hair_yu4", "man_hair_yu21", "man_hair_yu22", "man_hair_y2", "man_hair_yyyyy", "shoulderhair", "shortlayer", "shortcut", "shortbob", "hairmessy", "slickedback", "man_hair_r", "man_hair_s", "man_hair_bd_03", "man_hair_bd_04", "man_hair_bd_05", "man_hair_bd_06", "man_hair_yu20", "man_hair_yu19", "man_hair_yu17"],
		["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
		[
			("manface_young_2", 0xffcbe0e0, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
			("manface_midage", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_young", 0xffd0e0e0, ["hair_blonde"], [0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
			("manface_young_3", 0xffdceded, ["hair_blonde"], [0xff2f180e, 0xff171313, 0xff007080c]),
			("manface_7", 0xffc0c8c8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_midage_2", 0xfde4c8d8, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
			("manface_rugged", 0xffb0aab5, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_african", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_asian1", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian2", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian3", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffaeb0a6, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2", 0xffd0c8c1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_white1", 0xffe0e8e8, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19]),
			("manface_mideast3", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_8", 0xffe0e8e8, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_han", 0xffe3e8e1, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_white1", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_white2", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_white3", 0xffdfefe1, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
			("manface_black1", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xff807c8a, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
		"skel_human", 1.0, psys_game_blood, psys_game_blood_2,
		[
			[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
			[0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
			[1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
			[0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
			[0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
			[2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)]
		]
	),

	(
		"female_asian", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "norm_handL", "female_head_new",
		[(230, 0, 0.8, -1.0, "Chin_Size"),
		(220, 0, -1.0, 1.0, "Chin_Shape"),
		(10, 0, -1.2, 1.0, "Chin_Forward"),
		(20, 0, -0.6, 1.2, "Jaw_Width"),
		(40, 0, -0.7, 1.0, "Jaw_Position"),
		(270, 0, 0.9, -0.9, "Mouth-Nose_Distance"),
		(30, 0, -0.5, 1.0, "Mouth_Width"),
		(50, 0, -0.5, 1.0, "Cheeks"),
		(60, 0, -0.5, 1.0, "Nose_Height"),
		(70, 0, -0.5, 1.1, "Nose_Width"),
		(80, 0, 1.5, -0.3, "Nose_Size"),
		(240, 0, -1.0, 0.8, "Nose_Shape"),
		(90, 0, 0.0, 1.1, "Nose_Bridge"),
		(100, 0, -0.5, 1.5, "Cheek_Bones"),
		(150, 0, -0.4, 1.0, "Eye_Width"),
		(110, 0, 1.0, 0.0, "Eye_to_Eye_Dist"),
		(120, 0, -0.2, 1.0, "Eye_Shape"),
		(130, 0, -0.1, 1.6, "Eye_Depth"),
		(140, 0, -0.2, 1.0, "Eyelids"),
		(160, 0, -0.2, 1.2, "Eyebrow_Position"),
		(170, 0, -0.2, 0.7, "Eyebrow_Height"),
		(250, 0, -0.4, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.5, 1.2, "Eyebrow_Shape"),
		(260, 0, 1.0, -0.7, "Temple_Width"),
		(200, 0, -0.5, 1.0, "Face_Depth"),
		(210, 0, -0.5, 0.9, "Face_Ratio"),
		(190, 0, -0.4, 0.8, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_hair_song_02222", "woman_hair_song_03", "woman_hair_song_04", "woman_hair_song_05", "woman_hair_yu12", "ponytailfem", "woman_ren_hair_14", "straightshoulderrrr", "RANs07", "woman_corean_hair_25", "woman_ren_hair_14", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("womanface_young", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_b", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_a", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_brown", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"male_npc", 0, "aman_body", "aman_calf_l", "am_handL", "invalid_item",
		[],

		["blank_head", "yelushaleng"],
		[],
		["hair_blonde"],
		[],
		[
			("invalid_item", 0xffcbe0e0, ["hair_blonde"], [0xffffffff]),
			("invalid_item", 0xff807c8a, ["hair_blonde"], [0xffffffff])
		],
		[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
		"skel_human", 1.05, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"female_npc_euro", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "norm_handL", "invalid_item",
		[],

		["ww_face_40", "ww_face_41", "ww_face_42", "ww_face_43", "ww_face_04", "ww_face_34", "ww_face_44", "ww_face_45", "ww_face_14", "ww_face_46", "ww_face_47", "ww_face_13", "ww_face_10", "ww_face_16", "ww_face_48", "ww_face_49", "ww_face_50", "ww_face_02", "ww_face_01", "ww_face_08", "ww_face_11", "ww_face_52", "ww_face_51", "ww_face_15", "ww_face_03", "ww_face_53", "ww_face_14", "ww_face_14"],
		[],
		["hair_blonde"],
		[],
		[
			("invalid_item", 0xffe3e8ef, ["hair_blonde"], [0xffffffff]),
			("invalid_item", 0xffaf9f7e, ["hair_blonde"], [0xffffffff])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"black_male", 0, "bman_body", "bman_calf_l", "bm_handL", "male_head",
		[(20, 0, 0.7, -0.6, "Chin_Size"),
		(260, 0, -0.6, 1.4, "Chin_Shape"),
		(10, 0, -0.5, 0.9, "Chin_Forward"),
		(240, 0, 0.9, -0.8, "Jaw_Width"),
		(210, 0, -0.5, 1.0, "Jaw_Position"),
		(250, 0, 0.8, -1.0, "Mouth-Nose_Distance"),
		(200, 0, -0.3, 1.0, "Mouth_Width"),
		(50, 0, -1.5, 1.0, "Cheeks"),
		(60, 0, -0.4, 1.35, "Nose_Height"),
		(70, 0, -0.6, 0.7, "Nose_Width"),
		(80, 0, 1.0, -0.1, "Nose_Size"),
		(270, 0, -0.5, 1.0, "Nose_Shape"),
		(90, 0, -0.2, 1.4, "Nose_Bridge"),
		(100, 0, -0.3, 1.5, "Cheek_Bones"),
		(150, 0, -0.2, 3.0, "Eye_Width"),
		(110, 0, 1.5, -0.9, "Eye_to_Eye_Dist"),
		(120, 0, 1.9, -1.0, "Eye_Shape"),
		(130, 0, -0.5, 1.1, "Eye_Depth"),
		(140, 0, 1.0, -1.2, "Eyelids"),
		(160, 0, 1.3, -0.2, "Eyebrow_Position"),
		(170, 0, -0.1, 1.9, "Eyebrow_Height"),
		(220, 0, -0.1, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.1, 1.6, "Eyebrow_Shape"),
		(230, 0, 1.2, -0.7, "Temple_Width"),
		(30, 0, -0.6, 0.9, "Face_Depth"),
		(40, 0, 0.9, -0.6, "Face_Ratio"),
		(190, 0, 0.0, 0.95, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y12", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v", "man_hair_t", "man_hair_y6", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y11", "man_hair_u", "man_hair_y", "man_hair_y2", "man_hair_y4", "man_hair_yu20", "man_hair_yu19", "man_hair_yu7", "man_hair_yu2", "man_hair_yu1", "man_hair_yu3", "man_hair_yu10", "man_hair_yu18", "man_hair_yu6", "man_hair_yu8", "man_hair_yu9", "man_hair_yu12", "man_hair_yu17", "man_hair_yu11", "man_hair_yu13", "man_hair_yu14", "man_hair_yu15", "man_hair_yu16", "man_hair_yu4", "man_hair_yu21", "man_hair_yu22", "man_hair_y2", "man_hair_y", "shoulderhair", "shortlayer", "shortcut", "shortbob", "hairmessy", "slickedback", "man_hair_r", "man_hair_s", "man_hair_bd_03", "man_hair_bd_04", "man_hair_bd_05", "man_hair_bd_06", "man_hair_yu20", "man_hair_yu19", "man_hair_yu17"],
		["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
		[
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black1", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black2", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("manface_black3", 0xffcbe0e0, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
		"skel_human", 1.0, psys_game_blood, psys_game_blood_2,
		[
			[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
			[0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
			[1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
			[0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
			[0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
			[2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)]
		]
	),

	(
		"female_corprus", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "norm_handL", "corprus_female_head",
		[(40, 0, -1.0, 0.0, "Caucassian_2"),
		(30, 0, 0.0, 1.0, "Caucassian_1"),
		(10, 0, 0.0, 1.0, "Forehead"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_ren_hair_14", "woman_hair_song_03", "woman_corean_hair_25", "woman_hair_song_05", "RANs07", "woman_hair_song_07", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("womanface_young_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
			("womanface_b_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
			("womanface_caucas_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff502a19, 0xff19100c, 0xff0c0d19]),
			("womanface_young_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_b_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"ro_man", 0, "rom_body", "rom_calf_l", "rom_handL", "male_head2",
		[(240, 0, -0.4, 0.3, "Chin_Size"),
		(230, 0, -0.4, 0.8, "Chin_Shape"),
		(250, 0, -0.25, 0.55, "Chin_Forward"),
		(130, 0, -0.5, 1.0, "Jaw_Width"),
		(120, 0, -0.5, 0.6, "Lower_Lip"),
		(110, 0, -0.2, 0.6, "Upper_Lip"),
		(100, 0, 0.2, -0.2, "Mouth-Nose_Distance"),
		(90, 0, 0.55, -0.55, "Mouth_Width"),
		(30, 0, -0.3, 0.3, "Nostril_Size"),
		(60, 0, 0.25, -0.25, "Nose_Height"),
		(40, 0, -0.2, 0.3, "Nose_Width"),
		(70, 0, -0.3, 0.4, "Nose_Size"),
		(50, 0, 0.2, -0.3, "Nose_Shape"),
		(80, 0, -0.3, 0.65, "Nose_Bridge"),
		(160, 0, -0.2, 0.25, "Eye_Width"),
		(190, 0, -0.25, 0.15, "Eye_to_Eye_Dist"),
		(170, 0, -0.85, 0.85, "Eye_Shape"),
		(200, 0, -0.3, 0.7, "Eye_Depth"),
		(180, 0, -1.5, 1.5, "Eyelids"),
		(20, 0, 0.6, -0.25, "Cheeks"),
		(260, 0, -0.6, 0.5, "Cheek_Bones"),
		(220, 0, 0.8, -0.8, "Eyebrow_Height"),
		(210, 0, -0.75, 0.75, "Eyebrow_Shape"),
		(10, 0, -0.6, 0.5, "Temple_Width"),
		(270, 0, -0.3, 1.0, "Face_Depth"),
		(150, 0, -0.25, 0.45, "Face_Ratio"),
		(140, 0, -0.4, 0.5, "Face_Width"),
		(280, 0, 1.0, 1.0, "Post-Edit")],

		["man_hair_s", "man_hair_m", "man_hair_n", "man_hair_o", "man_hair_y10", "man_hair_y1232312", "man_hair_p", "man_hair_r", "man_hair_q", "man_hair_v222", "man_hair_ttttt", "man_hair_y666", "man_hair_y3", "man_hair_y7", "man_hair_y9", "man_hair_y1122", "man_hair_u3213", "man_hair_y312", "man_hair_y2", "man_hair_y4321", "man_hair_yu20", "man_hair_yu19", "man_hair_yu7", "man_hair_yu2312", "man_hair_yu1", "man_hair_yu3", "man_hair_yu10", "man_hair_yu1819", "man_hair_yu6", "man_hair_yu8", "man_hair_yu9", "man_hair_yu12", "man_hair_yu17", "man_hair_yu11312", "man_hair_yu13", "man_hair_yu141414", "man_hair_yu15", "man_hair_yu16", "man_hair_yu4", "man_hair_yu21", "man_hair_yu22", "man_hair_y2", "man_hair_yyyyy", "shoulderhair", "shortlayer", "shortcut", "shortbob", "hairmessy", "slickedback", "man_hair_r", "man_hair_s", "man_hair_bd_03", "man_hair_bd_04", "man_hair_bd_05", "man_hair_bd_06", "man_hair_yu20", "man_hair_yu19", "man_hair_yu17"],
		["beard_e", "beard_d", "beard_k", "beard_l", "beard_i", "beard_j", "beard_z", "beard_m", "beard_n", "beard_y", "beard_p", "beard_o", "beard_v", "beard_f", "beard_b", "beard_c", "beard_t", "beard_u", "beard_r", "beard_s", "beard_a", "beard_h", "beard_g"],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		["beard_blonde", "beard_red", "beard_brunette", "beard_black", "beard_white"],
		[
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian1_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_asian3", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_8_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_han_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast3_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast1", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c]),
			("manface_mideast2_ro", 0xffbbb6ae, ["hair_blonde"], [0xff171313, 0xff007080c])
		],
		[(voice_die, "snd_man_die"), (voice_hit, "snd_man_hit"), (voice_grunt, "snd_man_grunt"), (voice_grunt_long, "snd_man_grunt_long"), (voice_yell, "snd_man_yell"), (voice_stun, "snd_man_stun"), (voice_victory, "snd_man_victory")],
		"skel_human", 1.0, psys_game_blood, psys_game_blood_2,
		[
			[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)],
			[0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
			[1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
			[0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
			[-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
			[0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
			[2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)]
		]
	),

	(
		"black_female_corprus", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "bk_handL", "corprus_female_head",
		[(40, 0, -1.0, 0.0, "Caucassian_2"),
		(30, 0, 0.0, 1.0, "Caucassian_1"),
		(10, 0, 0.0, 1.0, "Forehead"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_ren_hair_14", "woman_hair_song_03", "woman_corean_hair_25", "woman_hair_song_05", "RANs07", "woman_hair_song_07", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("womanface_african_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_gaolu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"female_npc_asia", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "norm_handL", "invalid_item",
		[],

		["ww_face_05", "ww_face_23", "ww_face_18", "ww_face_28", "ww_face_37", "ww_face_19", "ww_face_18", "ww_face_21", "ww_face_36", "ww_face_25", "ww_face_24", "ww_face_09", "ww_face_38", "ww_face_17", "ww_face_25", "ww_face_20", "ww_face_20", "ww_face_21"],
		[],
		["hair_blonde"],
		[],
		[
			("invalid_item", 0xffe3e8ef, ["hair_blonde"], [0xffffffff]),
			("invalid_item", 0xffaf9f7e, ["hair_blonde"], [0xffffffff])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"female_npc_low_height_euro", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "whi_handL", "invalid_item",
		[],

		["ww_face_30", "ww_face_31", "ww_face_32", "ww_face_12", "ww_face_39", "ww_face_03", "ww_face_35", "ww_face_33"],
		[],
		["hair_blonde"],
		[],
		[
			("invalid_item", 0xffe3e8ef, ["hair_blonde"], [0xffffffff]),
			("invalid_item", 0xffaf9f7e, ["hair_blonde"], [0xffffffff])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.87, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"female_npc_low_height_asia", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "lig_handL", "invalid_item",
		[],

		["ww_face_22", "ww_face_07", "ww_face_29", "ww_face_24", "ww_face_27", "ww_face_06", "ww_face_07", "ww_face_26"],
		[],
		["hair_blonde"],
		[],
		[
			("invalid_item", 0xffe3e8ef, ["hair_blonde"], [0xffffffff]),
			("invalid_item", 0xffaf9f7e, ["hair_blonde"], [0xffffffff])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.87, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"black_woman", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "bk_handL", "female_head",
		[(230, 0, 0.8, -1.0, "Chin_Size"),
		(220, 0, -1.0, 1.0, "Chin_Shape"),
		(10, 0, -1.2, 1.0, "Chin_Forward"),
		(20, 0, -0.6, 1.2, "Jaw_Width"),
		(40, 0, -0.7, 1.0, "Jaw_Position"),
		(270, 0, 0.9, -0.9, "Mouth-Nose_Distance"),
		(30, 0, -0.5, 1.0, "Mouth_Width"),
		(50, 0, -0.5, 1.0, "Cheeks"),
		(60, 0, -0.5, 1.0, "Nose_Height"),
		(70, 0, -0.5, 1.1, "Nose_Width"),
		(80, 0, 1.5, -0.3, "Nose_Size"),
		(240, 0, -1.0, 0.8, "Nose_Shape"),
		(90, 0, 0.0, 1.1, "Nose_Bridge"),
		(100, 0, -0.5, 1.5, "Cheek_Bones"),
		(150, 0, -0.4, 1.0, "Eye_Width"),
		(110, 0, 1.0, 0.0, "Eye_to_Eye_Dist"),
		(120, 0, -0.2, 1.0, "Eye_Shape"),
		(130, 0, -0.1, 1.6, "Eye_Depth"),
		(140, 0, -0.2, 1.0, "Eyelids"),
		(160, 0, -0.2, 1.2, "Eyebrow_Position"),
		(170, 0, -0.2, 0.7, "Eyebrow_Height"),
		(250, 0, -0.4, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.5, 1.2, "Eyebrow_Shape"),
		(260, 0, 1.0, -0.7, "Temple_Width"),
		(200, 0, -0.5, 1.0, "Face_Depth"),
		(210, 0, -0.5, 0.9, "Face_Ratio"),
		(190, 0, -0.4, 0.8, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_hair_song_02222", "woman_hair_song_03", "woman_hair_song_04", "woman_hair_song_05", "woman_hair_song_06", "woman_hair_song_07", "woman_ren_hair_14", "straightshoulderrrr", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_mu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african_mu", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_african", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"ro_woman", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "ro_handL", "female_head",
		[(230, 0, 0.8, -1.0, "Chin_Size"),
		(220, 0, -1.0, 1.0, "Chin_Shape"),
		(10, 0, -1.2, 1.0, "Chin_Forward"),
		(20, 0, -0.6, 1.2, "Jaw_Width"),
		(40, 0, -0.7, 1.0, "Jaw_Position"),
		(270, 0, 0.9, -0.9, "Mouth-Nose_Distance"),
		(30, 0, -0.5, 1.0, "Mouth_Width"),
		(50, 0, -0.5, 1.0, "Cheeks"),
		(60, 0, -0.5, 1.0, "Nose_Height"),
		(70, 0, -0.5, 1.1, "Nose_Width"),
		(80, 0, 1.5, -0.3, "Nose_Size"),
		(240, 0, -1.0, 0.8, "Nose_Shape"),
		(90, 0, 0.0, 1.1, "Nose_Bridge"),
		(100, 0, -0.5, 1.5, "Cheek_Bones"),
		(150, 0, -0.4, 1.0, "Eye_Width"),
		(110, 0, 1.0, 0.0, "Eye_to_Eye_Dist"),
		(120, 0, -0.2, 1.0, "Eye_Shape"),
		(130, 0, -0.1, 1.6, "Eye_Depth"),
		(140, 0, -0.2, 1.0, "Eyelids"),
		(160, 0, -0.2, 1.2, "Eyebrow_Position"),
		(170, 0, -0.2, 0.7, "Eyebrow_Height"),
		(250, 0, -0.4, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.5, 1.2, "Eyebrow_Shape"),
		(260, 0, 1.0, -0.7, "Temple_Width"),
		(200, 0, -0.5, 1.0, "Face_Depth"),
		(210, 0, -0.5, 0.9, "Face_Ratio"),
		(190, 0, -0.4, 0.8, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_hair_song_02", "woman_hair_song_03", "woman_hair_song_04", "woman_hair_song_05", "woman_hair_song_06", "woman_hair_song_07", "woman_ren_hair_14", "straightshoulderrrr", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("dontknow_womanface3_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("Jed_Q_w_1_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_b2_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface4_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface1_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_yiy_3_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_hanhun_3_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("womanface_asia_ro", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface5", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface5", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c]),
			("dontknow_womanface5", 0xffe3e8ef, ["hair_blonde"], [0xff120808, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

	(
		"ro_woman_rok", skf_use_morph_key_10, "woman_body", "awoman_calf_l", "ro_handL", "female_head_new",
		[(230, 0, 0.8, -1.0, "Chin_Size"),
		(220, 0, -1.0, 1.0, "Chin_Shape"),
		(10, 0, -1.2, 1.0, "Chin_Forward"),
		(20, 0, -0.6, 1.2, "Jaw_Width"),
		(40, 0, -0.7, 1.0, "Jaw_Position"),
		(270, 0, 0.9, -0.9, "Mouth-Nose_Distance"),
		(30, 0, -0.5, 1.0, "Mouth_Width"),
		(50, 0, -0.5, 1.0, "Cheeks"),
		(60, 0, -0.5, 1.0, "Nose_Height"),
		(70, 0, -0.5, 1.1, "Nose_Width"),
		(80, 0, 1.5, -0.3, "Nose_Size"),
		(240, 0, -1.0, 0.8, "Nose_Shape"),
		(90, 0, 0.0, 1.1, "Nose_Bridge"),
		(100, 0, -0.5, 1.5, "Cheek_Bones"),
		(150, 0, -0.4, 1.0, "Eye_Width"),
		(110, 0, 1.0, 0.0, "Eye_to_Eye_Dist"),
		(120, 0, -0.2, 1.0, "Eye_Shape"),
		(130, 0, -0.1, 1.6, "Eye_Depth"),
		(140, 0, -0.2, 1.0, "Eyelids"),
		(160, 0, -0.2, 1.2, "Eyebrow_Position"),
		(170, 0, -0.2, 0.7, "Eyebrow_Height"),
		(250, 0, -0.4, 0.9, "Eyebrow_Depth"),
		(180, 0, -1.5, 1.2, "Eyebrow_Shape"),
		(260, 0, 1.0, -0.7, "Temple_Width"),
		(200, 0, -0.5, 1.0, "Face_Depth"),
		(210, 0, -0.5, 0.9, "Face_Ratio"),
		(190, 0, -0.4, 0.8, "Face_Width"),
		(280, 0, 0.0, 1.0, "Post-Edit")],

		["woman_hair_p", "woman_hair_n", "woman_hair_o", "woman_hair_q", "woman_hair_r", "woman_hair_t", "woman_hair_s", "woman_hair_gaolu_0", "woman_hair_yu12", "woman_hair_song_02222", "ponytailfem", "woman_hair_yu1yyy", "woman_hair_yu2", "woman_hair_yu3yy", "woman_hair_yu4yy", "woman_hair_yu5", "woman_hair_yu6yy", "woman_hair_yu7yy", "woman_hair_yu8yy", "woman_hair_yu9", "woman_hair_yu10", "woman_hair_yu11", "woman_hair_yu12", "woman_hair_yu13yy", "woman_hair_yu14", "woman_hair_yu15", "woman_hair_yu20", "woman_hair_yu17", "woman_hair_yu18", "woman_hair_yu19", "woman_hair_yu16", "woman_hair_yu21", "woman_hair_yu22", "woman_hair_yu23", "courthair", "ponytail", "longstraight", "longshoulder", "maidenhairrrr", "straightshoulderrrr", "hair_ren03_option", "woman_hair_song_02222", "woman_hair_song_03", "woman_hair_song_04", "woman_hair_song_05", "woman_hair_yu12", "ponytailfem", "woman_ren_hair_14", "straightshoulderrrr", "RANs07", "woman_corean_hair_25", "woman_ren_hair_14", "extrahair8", "extrahair11"],
		[],
		["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"],
		[],
		[
			("womanface_young_ro", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_b_ro", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_a_ro", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c]),
			("womanface_brown_ro", 0xffe3e8ef, ["hair_blonde"], [0xff19100c, 0xff0c0d19, 0xff007080c])
		],
		[(voice_die, "snd_woman_die"), (voice_hit, "snd_woman_hit"), (voice_yell, "snd_woman_yell")],
		"skel_human_female", 0.94, psys_game_blood, psys_game_blood_2,
		[
			
		]
	),

]
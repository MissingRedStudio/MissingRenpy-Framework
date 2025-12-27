define DIM_MATRIX = TintMatrix("#999999") 
define NORMAL_MATRIX = IdentityMatrix()

define default_chara_transition = Dissolve(0.3)
define chara_move_transition = MoveTransition(0.5)

transform chara_pos(x_align=0.5):
    default_chara_pos(x_align)
    xzoom 1.0

transform chara_pos_f(x_align=0.5):
    default_chara_pos(x_align)
    xzoom -1.0

transform default_chara_pos(x_align=0.5):
    xanchor 0.5
    yanchor 0.0
    yalign 0.0
    xalign x_align
    zoom 0.75

define pos_left      = chara_pos(0.35)
define pos_center    = chara_pos(0.5)
define pos_right     = chara_pos(0.65)
define pos_far_left  = chara_pos(0.0)
define pos_far_right = chara_pos(1.0)

define pos_left_f      = chara_pos_f(0.35)
define pos_center_f    = chara_pos_f(0.5)
define pos_right_f     = chara_pos_f(0.65)
define pos_far_left_f  = chara_pos_f(0.0)
define pos_far_right_f = chara_pos_f(1.0)

define standard_expressions = [
    "normal", "happy", "laugh", "blush", "shock", "angry",
    "sad", "anxious", "ponder", "bored", "eyes_closed", "smile", 
    "cry", "scared", "surprise_p", "disappoint"
]

transform trans_dim:
    matrixcolor DIM_MATRIX

transform trans_normal:
    matrixcolor NORMAL_MATRIX

init -1 python:
    import os 

    sprite_map = {}
    for file_path in renpy.list_files():
        if file_path.lower().endswith(('.png', '.webp')):
            filename = os.path.basename(file_path)
            sprite_map[filename] = file_path

    def setExpr_logic(characters, expression, isTalking=False):
        
        active_transform = trans_dim if not isTalking else trans_normal
        
        char_list = characters if isinstance(characters, list) else [characters] 

        for char_tag in char_list:
            full_image_tag = char_tag + " " + expression
                        
            renpy.show(
                full_image_tag,
                at_list=[active_transform],
                layer='master'
            )

        return True

    def SetupCharacter(char_data):
        short_name = char_data['tag'].lower()
        full_name = char_data['name']
        color = char_data.get('color', '#ffffff') 
        
        char_object = renpy.store.Character(
            full_name, 
            color=color, 
            image=short_name,
            what_with=None,
            type='chara',
            what_args={'default_expr': 'normal'}
        )
        setattr(renpy.store, short_name, char_object)
        
        found_any = False
        for tag in standard_expressions:
            image_tag = short_name + " " + tag            
            target_filename = short_name + "_" + tag + ".png" 
            
            if target_filename in sprite_map:
                renpy.image(image_tag, sprite_map[target_filename])
                found_any = True
        
        if not found_any:
            print(f"WARNING: Tidak ada sprite ditemukan untuk '{short_name}'. Cek nama file!")

    def SetupAllCharacters(character_list):
        for data in character_list:
            SetupCharacter(data)

label setExpr(characters=[], expression="normal", isTalking=False):
    $ setExpr_logic(characters, expression, isTalking)
    return

label talk(character_tag, dialogue_text, expression="normal"):
    call setExpr([character_tag], expression, True)
    
    $ renpy.say(getattr(renpy.store, character_tag), dialogue_text) 

    call setExpr([character_tag], expression, False)
    return

label narator(text_to_display, duration=5.0, transition=Dissolve(0.5)):
    show screen narator_screen(text_to_display, duration=duration) with transition
    
    call screen narator_screen(text_to_display, duration=duration)
    
    hide screen narator_screen with transition 
    return
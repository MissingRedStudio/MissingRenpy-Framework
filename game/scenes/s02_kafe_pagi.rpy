label s02_kafe_pagi:
    call play_ambience("audio/restaurant_ambience.mp3", volume=0.1, fade_time = 3.0)
    call play_music("audio/find your cafein_bgm.mp3", fade_time = 2.0)

    scene kafe_siang 
    
    # SETUP AWAL SCENE
    show bulan normal at pos_left_f
    show senja normal at pos_right
    
    call setExpr(['senja', 'bulan'], 'normal') 
    
    call talk('bulan', 'Halo Senjaa :DD', 'happy')

    call setExpr(['bulan'], 'sad')
    call talk('senja', 'ehhh ko kamu ada disini', 'shock')

    call talk('bulan', 'emang kenapa gitu?', 'angry')

    call setExpr(['bulan'], 'shock')
    call talk('senja', 'enggaa, kita kaget aja loh', 'sad')
    call talk('senja', 'bukannya kamu udah engga kuliah ya?', 'sad')

    menu:
        "tau dari mana?":
            jump s02_tauDarimana
        "engga ko":
            jump s02_enggaKo

label s02_tauDarimana:
    call setExpr(['senja'], 'sad')
    call talk('bulan', 'tau dari mana kamu?', 'sad')

    jump endGame

label s02_enggaKo:
    call setExpr(['senja'], 'happy')
    call talk('bulan', 'engga koo', 'happy')

    show bulan normal at pos_center
    show senja normal at pos_far_right 
    with chara_move_transition
    show hari normal at pos_far_left_f with default_chara_transition
    
    call setExpr(['bulan', 'senja'], 'normal')
    call talk('hari', "HALO GESS", 'happy')

    call talk('senja', "halooo", 'happy')
    call talk('bulan', "ada apa luwh?", 'happy')

    call setExpr(['senja', 'bulan'], 'shock')
    call talk('hari', 'mau jajan gw, GAS IKUT?', 'happy')

    call setExpr(['senja', 'bulan', 'hari'], 'happy', True)
    all "GAS!!!"

    show bulan shock at pos_center_f
    call setExpr(['hari', 'bulan'], 'shock')
    call talk('senja', 'ehh, aku udah dijemput ternyata...', 'sad')

    call talk('hari', 'yasudahlah, gimana lagii', 'normal')
    call talk ('bulan', 'tiati yaa, senja', 'happy')

    call talk('senja', 'iyaaa, aku duluan yaaa', 'happy')

    hide senja with default_chara_transition
    
    show hari normal at pos_left_f
    show bulan normal at pos_right
    with chara_move_transition

    call talk('hari', 'yaudah, kita berdua aja gas?', 'happy')
    call talk('bulan', 'GAS!', 'happy')

    jump endGame

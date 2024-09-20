from random import choice, randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Görünüşe göre bayağı sessiz birisisin...'
    elif 'selam' in lowered:
        return 'Selam!'
    elif 'nasılsın' in lowered:
        return 'Çok iyiyim teşekkürler!'
    elif 'görüşürüz' in lowered:
        return 'Görüşürüz!'
    elif 'zar at' in lowered:
        return f'Zarlandın: {randint(1, 6)}!'
    else:
        return choice(['Bunu çözemiyorum...',
                       'Başka bir şey mi demek istedin?',
                       'Anlayamadım...'])
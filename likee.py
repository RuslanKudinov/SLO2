from PIL import Image

def make_logo_white(input_path, output_path):
    # Открываем изображение с альфа-каналом
    img = Image.open(input_path).convert('RGBA')
    pixels = img.load()
    
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Если пиксель непрозрачный (альфа > 0) – делаем белым
            if a > 0:
                pixels[x, y] = (255, 255, 255, a)
            # иначе оставляем прозрачным
    img.save(output_path, 'PNG')
    print(f'Готово! Файл сохранён как {output_path}')

# Использование: укажи путь к исходному файлу и имя для нового
make_logo_white('l_old.png', 'likee_white.png')
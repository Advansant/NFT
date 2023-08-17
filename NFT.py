from PIL import Image, ImageDraw, ImageChops
import random

def mudar_cor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def entre_cores(inicio_cor, final_cor, factor: float):
    result = 1 - factor
    return (
        int(inicio_cor[0] * result + final_cor[0] * factor),
        int(inicio_cor[1] * result + final_cor[1] * factor),
        int(inicio_cor[2] * result + final_cor[2] * factor),
    )

def criar(path: str):
    print("Sistema funcionando corretamente")
    img_size_px = 128
    padding_px = 16
    img_color = (0, 0, 0)

    inicio_cor = mudar_cor()
    final_cor = mudar_cor()

    image = Image.new("RGB", size=(img_size_px, img_size_px), color=img_color)

    draw = ImageDraw.Draw(image)

    pontos = []

    for _ in range(10):
        random_ponto = (
            random.randint(padding_px, img_size_px - padding_px),
            random.randint(padding_px, img_size_px - padding_px),
        )
        pontos.append(random_ponto)

    min_x = min([p[0] for p in pontos])
    max_x = max([p[0] for p in pontos])
    min_y = min([p[1] for p in pontos])
    max_y = max([p[1] for p in pontos])

    delta_x = min_x - (img_size_px - max_x)
    delta_y = min_y - (img_size_px - max_y)

    for i, ponto in enumerate(pontos):
        pontos[i] = (ponto[0] - delta_x // 2, ponto[1] - delta_y // 2)

    thickness = 5
    n_pontos = len(pontos) - 1

    for i, ponto in enumerate(pontos):
        sobrepor_image = Image.new("RGB", size=(img_size_px, img_size_px), color=img_color)
        sobrepor_draw = ImageDraw.Draw(sobrepor_image)

        ponto1 = ponto

        if i == n_pontos:
            ponto2 = pontos[0]
        else:
            ponto2 = pontos[i + 1]
        
        line_xy = (ponto1, ponto2)
        color_factor = i / n_pontos
        line_color = entre_cores(inicio_cor, final_cor, color_factor)
        thickness += 1
        sobrepor_draw.line(line_xy, fill=line_color, width=thickness)
        image = ImageChops.add(image, sobrepor_image)

    image.save(path)

if __name__ == "__main__":
    for i in range(5):
        criar(f"NFT_Image_{i}.png")

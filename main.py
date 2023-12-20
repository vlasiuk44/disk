import cv2 as cv
import numpy as np

MAP_SIZE = (600, 600, 3)
CENTER = (MAP_SIZE[0] // 2, MAP_SIZE[1] // 2)
RADIUS = MAP_SIZE[0] // 2
DELTA_ANGLE = 8
DELTA = 360 // DELTA_ANGLE


def get_colors():
    return [
        (255, 0, 0),     # Red
        (0, 255, 0),     # Green
        (0, 0, 255),     # Blue
        (255, 255, 0),   # Yellow
        (255, 0, 255),   # Magenta
        (0, 255, 255),   # Cyan
        (128, 128, 128)  # Gray
    ]


def get_alphabet_colors():
    colors = get_colors()
    num_colors = len(colors)

    alphabet_colors = {
        chr(i): (
            (colors[num_colors - i // num_colors - 1]),
            (colors[i % num_colors])
        ) for i in range(65, 91)
    }
    alphabet_colors[" "] = ((255, 255, 255), (255, 255, 255))

    return alphabet_colors


def draw_code(image, message, symbol_colors):
    angle_message = DELTA_ANGLE * len(message)

    for angle in range(0, 360, DELTA):
        current_color = symbol_colors.get(
            message[angle % angle_message // DELTA_ANGLE], (0, 0, 0))[0]
        image = cv.ellipse(
            image, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, current_color, -1)

        current_color = symbol_colors.get(
            message[(angle - DELTA) % angle_message // DELTA_ANGLE], (0, 0, 0))[1]
        image = cv.ellipse(
            image, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, current_color, -1)

    return image


def create_image():
    image = np.zeros(shape=MAP_SIZE, dtype='uint8')
    image = cv.rectangle(
        image, (0, 0), (MAP_SIZE[0], MAP_SIZE[1]), (220, 200, 200), -1)
    image = cv.circle(image, CENTER, RADIUS, (255, 255, 255), -1)
    return image


def save_and_display_image(image):
    cv.imwrite("cypher.png", image)

    cv.namedWindow("Image")
    cv.imshow("Image", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def main():
    message = "TestText"
    symbol_colors = get_alphabet_colors()

    print("Symbol Colors:", symbol_colors)

    image = create_image()
    image = draw_code(image, message.upper(), symbol_colors)

    save_and_display_image(image)


if __name__ == "__main__":
    main()

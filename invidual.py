from PIL import Image, ImageDraw, ImageFilter
import numpy as np
import random

class Invidual:
    def __init__(self, width=600, height=600, invidual_size=20):
        self.width = width
        self.height = height
        self.size = invidual_size
        self.fitness = 0
        self.shapes = [self.generate_random_shape() for _ in range(self.size)]

    def generate_random_shape(self):
        shape_type = random.choice(['rectangle', 'ellipse'])
        x0, y0 = random.randint(0, self.width), random.randint(0, self.height)
        x1, y1 = random.randint(x0, x0+50), random.randint(y0, y0+50)
        color = tuple(random.randint(0, 255) for _ in range(3))
        return {'type': shape_type, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'color': color}
    
    def draw(self):
        img = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        for shape in self.shapes:
            if shape['type'] == 'rectangle':
                draw.rectangle([shape['x0'], shape['y0'], shape['x1'], shape['y1']], fill=shape['color'])
            elif shape['type'] == 'ellipse':
                draw.ellipse([shape['x0'], shape['y0'], shape['x1'], shape['y1']], fill=shape['color'])
        return img

    def calculate_fitness(self, target_image):
        generated_pixels = np.array(self.draw())
        target_pixels = np.array(target_image)
        self.fitness = np.sum(np.abs(target_pixels - generated_pixels))

    def copy(self):
        new_invidual = Invidual(width=self.width, height=self.height, invidual_size=self.size)
        new_invidual.shapes = self.shapes.copy()
        return new_invidual

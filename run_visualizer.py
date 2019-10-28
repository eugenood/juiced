import json
import sys

from PIL import Image, ImageTk
from tkinter import Frame, Label, Tk

from juiced.metadata import Metadata
from juiced.env import JuicedEnv

from model.agent import LaurelAgent


class Visualizer:

    def __init__(self, level_id, model_path):

        self.env = JuicedEnv(level_id)

        self.state = self.env.reset()

        self.agent = LaurelAgent(self.env)
        self.agent.initialize_network(model_path)
        self.agent.initialize_testing()

        self.state = self.agent.convert_state(self.state)

        self.height = self.env.observation_space.shape[0]
        self.width = self.env.observation_space.shape[1]

        self.metadata = Metadata.get_instance()
        self.root = Tk()

        self._initialize_frame()
        self._initialize_grid()

        self._refresh()
        self.root.title("Juiced Visualizer")
        self.root.mainloop()

    def _initialize_frame(self):

        def handle_keyboard_event(_):

            action = self.agent.act(self.state)
            self.state, _, done, _ = self.env.step((action.item(), 0))
            self.state = self.agent.convert_state(self.state)

            if done:

                self.root.destroy()
                return

            self._refresh()

        self.frame = Frame(self.root)
        self.frame.bind("<KeyPress>", handle_keyboard_event)
        self.frame.focus_set()
        self.frame.pack()

    def _initialize_grid(self):

        self.grid = [[None for _ in range(self.width)] for _ in range(self.height)]

        for x in range(self.height):

            for y in range(self.width):

                image = Image.open("juiced/assets/misc/ground.png").convert("RGBA")
                image = image.resize((40, 40))
                image = ImageTk.PhotoImage(image)

                self.grid[x][y] = Label(self.frame, image=image, width=40, height=40, borderwidth=0)
                self.grid[x][y].grid(row=x, column=y)
                self.grid[x][y].image = image

    def _refresh(self):

        for x in range(self.height):

            for y in range(self.width):

                item = self.env.stage.get(x, y)
                image = self._get_image(item)

                self.grid[x][y].configure(image=image)
                self.grid[x][y].image = image

    def _get_image(self, entity):

        metadata = self.metadata[entity]

        image_ground = Image.open("juiced/assets/misc/ground.png").convert("RGBA")
        image_ground = image_ground.resize((40, 40))

        image = Image.open("juiced/assets/" + metadata.url).convert("RGBA")
        image = image.resize((40, 40))

        image_ground.paste(image, (0, 0), image)

        return ImageTk.PhotoImage(image_ground)


if __name__ == "__main__":

    Visualizer(sys.argv[1], sys.argv[2])

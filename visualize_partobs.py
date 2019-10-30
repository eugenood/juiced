import json
import random
import sys

import torch
import torch.nn.functional as F

from PIL import Image, ImageTk
from tkinter import Frame, Label, Tk

from juiced.metadata import Metadata

from model.agent import LaurelAgentV1
from model.env import JuicedEnv


class Visualizer:

    def __init__(self, human_model_path, robot_model_path, intention_net_path):

        self.env = JuicedEnv()

        self.agent = LaurelAgentV1(self.env)
        self.agent.initialize_policy_network(human_model_path, robot_model_path)
        self.agent.initialize_intention_network(intention_net_path)
        self.agent.initialize_policy_testing()
        self.agent.initialize_intention_testing()

        self.state, self.intention = self.env.reset()
        self.state = self.agent.convert_state(self.state)
        self.intention = self.agent.convert_intention(self.intention)

        self.prev_human_action = None

        print(self.intention)

        self.height = self.env.dim_state[1]
        self.width = self.env.dim_state[2]

        self.metadata = Metadata.get_instance()
        self.root = Tk()

        self._initialize_frame()
        self._initialize_grid()

        self._refresh()
        self.root.title("Juiced Visualizer")
        self.root.mainloop()

    def _initialize_frame(self):

        def handle_keyboard_event(_):

            if self.prev_human_action is not None:
                predicted_intention = self.agent.intention_net(self.state, self.prev_human_action)

            else: predicted_intention = torch.tensor([0.5, 0.5]).cuda()

            print(predicted_intention)
            print(self.agent.human_policy_net(self.state, self.intention))
            print(self.agent.robot_policy_net(self.state, predicted_intention))
            print("======================================")

            human_action = self.agent.human_act(self.state, self.intention)
            robot_action = self.agent.robot_act(self.state, predicted_intention)

            self.prev_human_action = F.one_hot(human_action, self.agent.dim_action).float()

            self.state, _, done = self.env.step(human_action.item(), robot_action.item())
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

    Visualizer(sys.argv[1], sys.argv[2], sys.argv[3])

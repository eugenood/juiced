import json
import sys

from PIL import Image, ImageTk
from tkinter import Frame, Label, Tk

from juiced.metadata import Metadata
from juiced.stage import Stage


class Replayer:

    def __init__(self, trajectory):

        self.room_id = trajectory["room_id"]
        self.level = trajectory["level"]

        self.human_username = trajectory["human_username"]
        self.robot_username = trajectory["robot_username"]

        self.human_actions = trajectory["human_actions"]
        self.robot_actions = trajectory["robot_actions"]

        self.current_action_index = 0

        self.metadata = Metadata.get_instance()
        self.stage = Stage(self.level)
        self.root = Tk()

        self._initialize_frame()
        self._initialize_grid()

        self._refresh()
        self.root.title("Juiced Replayer")
        self.root.mainloop()

    def _initialize_frame(self):

        def handle_keyboard_event(_):

            if self.current_action_index == len(self.human_actions):

                self.root.destroy()
                return

            human_action = self.human_actions[self.current_action_index]
            robot_action = self.robot_actions[self.current_action_index]

            self.stage.human.act(human_action)
            self.stage.robot.act(robot_action)

            self.current_action_index = self.current_action_index + 1

            self._refresh()

        self.frame = Frame(self.root)
        self.frame.bind("<KeyPress>", handle_keyboard_event)
        self.frame.focus_set()
        self.frame.pack()

    def _initialize_grid(self):

        self.grid = [[None for _ in range(self.stage.width)] for _ in range(self.stage.height)]

        for x in range(self.stage.height):

            for y in range(self.stage.width):

                image = Image.open("juiced/assets/misc/ground.png").convert("RGBA")
                image = image.resize((40, 40))
                image = ImageTk.PhotoImage(image)

                self.grid[x][y] = Label(self.frame, image=image, width=40, height=40, borderwidth=0)
                self.grid[x][y].grid(row=x, column=y)
                self.grid[x][y].image = image

    def _refresh(self):

        for x in range(self.stage.height):

            for y in range(self.stage.width):

                item = self.stage.get(x, y)
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

    trajectory_filename = sys.argv[1]
    trajectory_file = open(trajectory_filename)
    trajectory = json.loads(trajectory_file.read())
    replayer = Replayer(trajectory)

from resources.robot_driver import RobotDriver


class BaseController:

    def __init__(self):
        self.robot_driver = RobotDriver()

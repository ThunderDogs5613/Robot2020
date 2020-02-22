from robotpy_ext.autonomous import StatefulAutonomous, timed_state


class Sim_Field(StatefulAutonomous):
    MODE_NAME = "Sim_Field"

    def init(self):
        pass

    def initialize(self):
        pass

    @timed_state(duration=0.3, next_state="Arc_Right", first=True)
    def Sharp_left(self):
        self.drive.arcadeDrive(0, 1, squareInputs=False)

    @timed_state(duration=4.5, next_state="Sharp_Right")
    def Arc_Right(self):
        self.drive.arcadeDrive(-0.91, -0.09, squareInputs=False)

    @timed_state(duration=0.345, next_state="Drive_Forward")
    def Sharp_Right(self):
        self.drive.arcadeDrive(0, -1, squareInputs=False)

    @timed_state(duration=2.5, next_state="Sharp_Left_2")
    def Drive_Forward(self):
        self.drive.arcadeDrive(-1, 0, squareInputs=False)

    @timed_state(duration=0.32, next_state="Short_Forward")
    def Sharp_Left_2(self):
        self.drive.arcadeDrive(0, 1, squareInputs=False)

    @timed_state(duration=1.7, next_state="Sharp_Left_3")
    def Short_Forward(self):
        self.drive.arcadeDrive(-1, 0, squareInputs=False)

    @timed_state(duration=0.3, next_state="Final_Forward")
    def Sharp_Left_3(self):
        self.drive.arcadeDrive(0, 1, squareInputs=False)

    @timed_state(duration=2.5, next_state="End")
    def Final_Forward(self):
        self.drive.arcadeDrive(-1, 0, squareInputs=False)

    @timed_state(duration=60, next_state="End")
    def End(self):
        self.drive.arcadeDrive(0, 0, squareInputs=False)

from robotpy_ext.autonomous import StatefulAutonomous, timed_state
import wpilib
from wpilib.drive import DifferentialDrive

class SimField(StatefulAutonomous):

    MODE_NAME = "Sim_Field"

    def initialize(self):


    def drive_backwards(self):
        self.drive.setSafetyEnabled(True)
        clock = wpilib.Timer()
        clock.start()

        while self.isAutonomous() and self.isEnabled():
            if clock.get() < 0.5:
                forward = 0
                side = 0.7
            elif clock.get() < 4.5:
                forward = -1
                side = -0.2
            elif clock.get() < 5.5:
                forward = -0.5
                side = -0.45
            elif clock.get() < 6.5:
                forward = -0.95
                side = -0.05
            elif clock.get() < 7.5:
                forward = -1
                side = 0
            elif clock.get() < 11.5:
                forward = -0.7
                side = 0.25
            elif clock.get() < 12.5:
                forward = -0.9
                side = 0.1
            elif clock.get() < 15:
                forward = -1
                side = 0
            else:
                forward = 0
                side = 0

            self.drive.arcadeDrive(
                forward,
                side,
                squareInputs=False
            )

    @timed_state(duration=15, next_state="none", first=False)
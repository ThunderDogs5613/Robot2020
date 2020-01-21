"""
    This is the 2020 simulator code for the FRC team 5613 Thunderdogs. It shows an example of how the robot works.
    We used the robotpy_ext autonomous for multiple autonomous modes to use at the competition.
    We are using the TimedRobot class which inherits from the IterativeRobot base. That means that we can use the
    autonomous selector like it would normally be used on the IterativeRobot class.
"""
from robotpy_ext import autonomous
from wpilib import TimedRobot, Spark, Joystick, SpeedControllerGroup
import wpilib


class MyRobot(TimedRobot):
    # Defines the channels that are used on the inputs. In the simulator, they have to match up with the physics.py file
    # This is really useful when you have a variable used hundreds of times and you want to have it set so you can
    # change it all in one go.

    RLMotorChannel = 2
    RRMotorChannel = 4
    FLMotorChannel = 1
    FRMotorChannel = 3

    DriveStickChannel = 0

    def robotInit(self):
        # Initializing the motors and putting them into groups for the drive function.
        RLMotor = Spark(self.RLMotorChannel)
        RRMotor = Spark(self.RRMotorChannel)
        FLMotor = Spark(self.FLMotorChannel)
        FRMotor = Spark(self.FRMotorChannel)

        self.Left = SpeedControllerGroup(RLMotor, FLMotor)
        self.Right = SpeedControllerGroup(RRMotor, FRMotor)

        # Initializing the Joystick to drive the robot.
        self.DriveStick = Joystick(self.DriveStickChannel)

        # Initializing the drive function for use in the simulator. This is the same as our normal robot.
        self.drive = wpilib.drive.DifferentialDrive(self.Left, self.Right)

        # Sets the right side motors to be inverted so the simulated robot can drive strait.
        self.drive.setRightSideInverted(rightSideInverted=True)

        # Turns the drive off after .1 seconds of inactivity.
        self.drive.setExpiration(0.1)

        # Components is a dictionary that contains any variables you want to put into it. All of the variables put into
        # components dictionary is given to the autonomous modes
        self.components = {"drive": self.drive}

        # Sets up the autonomous mode selector by telling it where the autonomous modes are at and what the autonomous
        # modes should inherit
        self.automodes = autonomous.AutonomousModeSelector("Sim_Autonomous", self.components)

    def autonomousPeriodic(self):
        # runs the autonomous modes when Autonomous is activated.
        self.automodes.run()

    def teleopPeriodic(self):

        # Turns on drive safety
        self.drive.setSafetyEnabled(True)
        if self.isOperatorControl() and self.isEnabled():
            self.drive.arcadeDrive(
                self.DriveStick.getY(),
                -self.DriveStick.getX(),
                squareInputs=False
            )


if __name__ == "__main__":
    wpilib.run(MyRobot)

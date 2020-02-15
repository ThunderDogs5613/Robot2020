"""
    This is the 2020 simulator code for the FRC team 5613 Thunderdogs. It shows an example of how the robot works.
    We used the robotpy_ext autonomous for multiple autonomous modes. Note how the directory we get the Autonomous
    modes from is different than the one used in the the robot.py file.
    We are using the TimedRobot class which inherits from the IterativeRobot base. That means that we can use the
    autonomous selector like it would normally be used on the IterativeRobot class.
    If there are issues check the Sim_Autonomous directory and make sure there is an __init__.py file.
"""
import wpilib
from robotpy_ext import autonomous
from wpilib import TimedRobot, Spark, Joystick, SpeedControllerGroup, run
from wpilib.drive import DifferentialDrive


class MyRobot(TimedRobot):
    # Defines the channels that are used on the inputs. In the simulator, they have to match up with the physics.py file
    # This is really useful when you have a variable used hundreds of times and you want to have it set so you can
    # change it all in one go.

    RLMotorChannel = 2
    RRMotorChannel = 0
    FLMotorChannel = 3
    FRMotorChannel = 4

    DriveStickChannel = 0

    # RobotInit is where all of the things we are using is initialized.
    def robotInit(self):
        # Note the lack of the camera server initialization here.

        # Initializing drive motors
        RLMotor = Spark(self.RLMotorChannel)
        RRMotor = Spark(self.RRMotorChannel)
        FLMotor = Spark(self.FLMotorChannel)
        FRMotor = Spark(self.FRMotorChannel)

        # Grouping drive motors into left and right.
        self.Left = SpeedControllerGroup(RLMotor, FLMotor)
        self.Right = SpeedControllerGroup(RRMotor, FRMotor)

        # Initializing drive Joystick.
        self.DriveStick = Joystick(self.DriveStickChannel)

        # Initializing drive function.
        self.drive = DifferentialDrive(self.Left, self.Right)

        # Sets the right side motors to be inverted.
        self.drive.setRightSideInverted(rightSideInverted=True)

        # Turns the drive off after .1 seconds of inactivity.
        self.drive.setExpiration(0.1)

        # Components is a dictionary that contains any variables you want to put into it. All of the variables put into
        # components dictionary is given to the autonomous modes.
        self.components = {"drive": self.drive}

        # Sets up the autonomous mode selector by telling it where the autonomous modes are at and what the autonomous
        # modes should inherit.
        self.automodes = autonomous.AutonomousModeSelector("Sim_Autonomous", self.components)

        # Autonomous and teleop periodic both run the code on a fixed loop time. A part of TimedRobot.
    def autonomousPeriodic(self):
        # runs the autonomous modes when Autonomous is activated.
        self.automodes.run()

    def teleopPeriodic(self):
        # Turns on drive safety and checks to se if operator control and the robot is enabled.
        self.drive.setSafetyEnabled(True)
        if self.isOperatorControl() and self.isEnabled():
            # Drives the robot with controller inputs. You can use buttons with self.DriveStick.getRawButton(ButtonNum).
            self.drive.arcadeDrive(
                self.DriveStick.getY(),
                -self.DriveStick.getX(),
                squareInputs=False
            )


# Runs you robot class.
if __name__ == "__main__":
    run(MyRobot)

"""
    This is the 2020 drive code for the FRC team 5613 Thunderdogs.
    We used the robotpy_ext autonomous for multiple autonomous modes. Note how the directory we get the Autonomous
    modes from is different than the one used in the the SimRobot.py file.
    We are using the TimedRobot class which inherits from the IterativeRobot base. That means that we can use the
    autonomous selector like it would normally be used on the IterativeRobot class.
    If there are issues check the autonomous directory and make sure there is an __init__.py file. Not having one causes
    issues because it is meant to be a package and you have to have it as a placeholder, even if there is nothing in it.
"""
import wpilib
from wpilib.drive import DifferentialDrive
from robotpy_ext import autonomous
from networktables import NetworkTables
from numpy import tan
import ctre
# from rev.color import ColorSensorV3


class MyRobot(wpilib.IterativeRobot):
    # Defines the channels that are used on the inputs.This is really useful when you have a variable used hundreds
    # of times and you want to have it set so you can change it all in one go.

    FLChannel = 4
    FRChannel = 2
    RLChannel = 3
    RRChannel = 1

    DriveStickChannel = 0

    # ExtraStickChannel = 1

    # RobotInit is where everything is initialized.
    def robotInit(self):
        # Initializes the network table
        # NetworkTables.initialize(server="10.56.13.2")
        # self.table = NetworkTables.getTable("limelight")
        # f is a control constant that will be used to change variable values quickly
        # self.f = 1
        # self.ControlConstant = -0.1 * self.f
        # self.minCommand = -0.05 * self.f

        # self.Blue = (RGB value or blue color)
        # self.Green = (RGB value of green color)
        # self.Red = (RGB value of red color)
        # self.Yellow = (RGB value of Yellow color)

        # Defines the Joystick that we will be using for driving.
        self.DriveStick = wpilib.Joystick(self.DriveStickChannel)

        # Initializing drive motors
        self.FLMotor = wpilib.Spark(self.FLChannel)
        self.FRMotor = wpilib.Spark(self.FRChannel)

        self.RLMotor = wpilib.Spark(self.RLChannel)
        self.RRMotor = wpilib.Spark(self.RRChannel)

        self.LoaderGrab = ctre.VictorSPX(1)

        # Puts the motors into groups so that they fit the parameters of the function.
        self.LMG = wpilib.SpeedControllerGroup(self.FLMotor, self.RLMotor)
        self.RMG = wpilib.SpeedControllerGroup(self.FRMotor, self.RRMotor)

        # The drive function that tells the computer what kind of drive to use and where the motors are.
        self.drive = DifferentialDrive(self.LMG, self.RMG)

        # self.ColorSensor = ColorSensorV3(wpilib.I2C.Port.kOnboard)

        # Components is a dictionary that contains any variables you want to put into it. All of the variables put into
        # components dictionary is given to the autonomous modes.
        # self.components = {"drive": self.drive}

        # Sets up the autonomous mode selector by telling it where the autonomous modes are at and what the autonomous
        # modes should inherit.
        # self.automodes = autonomous.AutonomousModeSelector("autonomous", self.components)

        self.timer = wpilib.Timer()

    # def autonomousPeriodic(self):
        # Runs the autonomous mode selector.
        # self.automodes.run()

    def operatorControl(self):

        self.drive.setSafetyEnabled(True)

        while self.isOperatorControlEnabled():

            # Checks to see if you are holding button 2 and if so automatically aims the robot. Else, normal drive.
            # if self.DriveStick.getrawButton(2):

            # Tx and Ty are variables marking the angle to the target.
            # If they are 0 then the calibrated crosshair is right on the target.
            # tx = self.table.getNumber("tx")
            # ty = self.table.getNumber("ty")

            # Angle to the target based off of the angle the camera is mounted at and the angle the camera measures.
            # targetAngle = 20 + ty
            # Distance from the target as calculated off of the equation
            # (TargetHeight - CameraHeight) / Tan(MountAngle + TargetAngle) = D
            # For a more in-depth explanation look a the limelight docs at docs.limelightvision.io
            # distance = 8 / tan(targetAngle)

            # The error in your robot's heading based off of the angle to the target.
            # headingError = tx
            # SteerAdjust = 0

            # Turns the robot if it is more than one degree off.
            # if tx > 1.0:
            # SteerAdjust = self.ControlConstant * headingError + self.minCommand
            # elif tx < -1.0:
            # SteerAdjust = self.ControlConstant * headingError - self.minCommand

            # Uses the calculations to turn the robot.
            # self.drive.tankDrive(
            # SteerAdjust,
            # -SteerAdjust,
            # squareInputs=False
            # )

            # else:
            # drives the robot with the arcade drive, which uses one joystick and is a bit easier to use. It is a
            # part of DifferentialDrive
            self.drive.arcadeDrive(
                self.DriveStick.getY(),
                self.DriveStick.getX(),
                squareInputs=True
            )

        wpilib.Timer.delay(.005)


# Runs the class MyRobot.
if __name__ == '__main__':
    wpilib.run(MyRobot)

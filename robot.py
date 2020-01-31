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
import numpy


class MyRobot(wpilib.TimedRobot):
    # Defines the channels that are used on the inputs.This is really useful when you have a variable used hundreds
    # of times and you want to have it set so you can change it all in one go.

    FLChannel = 0
    FRChannel = 1
    RLChannel = 2
    RRChannel = 3

    DriveStickChannel = 0

    # ExtraStickChannel = 1

    # RobotInit is where everything is initialized.
    def robotInit(self):

        # Initializes the network table
        NetworkTables.initialize(server="roborio-XXX-frc.local")
        self.table = NetworkTables.getTable("limelight")
        # f is a control constant that will be used to change variable values quickly
        self.f = 1
        self.ControlConstant = -0.1 * self.f
        self.minCommand = -0.05 * self.f

        # Initializing drive motors
        self.FLMotor = wpilib.Spark(self.FLChannel)
        self.FRMotor = wpilib.Spark(self.FRChannel)
        self.RLMotor = wpilib.Spark(self.RLChannel)
        self.RRMotor = wpilib.Spark(self.RRChannel)

        # Puts the motors into groups so that they fit the parameters of the function.
        self.LMG = wpilib.SpeedControllerGroup(self.FLMotor, self.RLMotor)
        self.RMG = wpilib.SpeedControllerGroup(self.FRMotor, self.RRMotor)

        # The drive function that tells the computer what kind of drive to use and where the motors are.
        self.drive = DifferentialDrive(self.LMG, self.RMG)

        # Tells the computer how long to wait without input to turn off the motors
        self.drive.setExpiration(0.1)

        # Defines the Joystick that we will be using for driving.
        self.DriveStick = wpilib.Joystick(self.DriveStickChannel)

        # Components is a dictionary that contains any variables you want to put into it. All of the variables put into
        # components dictionary is given to the autonomous modes.
        self.components = {"drive": self.drive}

        # Sets up the autonomous mode selector by telling it where the autonomous modes are at and what the autonomous
        # modes should inherit.
        self.automodes = autonomous.AutonomousModeSelector("autonomous", self.components)

    def autonmousPeriodic(self):
        # Runs the autonomous mode selector.
        self.automodes.run()

    def teleopPeriodic(self):
        # Enables the safety on the drive. Very important. DO NOT FORGET!
        self.drive.setSafetyEnabled(True)
        # Checks to see if the robot is activated and that operator control is active, so your robot does not move
        # when it is not supposed to.
        while self.isOperatorControl() and self.isEnabled():

            if self.DriveStick.getrawButton(2):

                tx = self.table.getNumber("tx")
                ty = self.table.getNumber("ty")

                targetAngle = 20 + ty
                distance = 8 / numpy.tan(targetAngle)

                headingError = tx
                SteerAdjust = 0 * self.f

                if tx > 1.0:
                    SteerAdjust = self.ControlConstant * headingError + self.minCommand
                elif tx < -1.0:
                    SteerAdjust = self.ControlConstant * headingError - self.minCommand

                self.drive.tankDrive(
                    SteerAdjust,
                    -SteerAdjust,
                    squareInputs=False
                )

            # drives the robot with the arcade drive, which uses one joystick and is a bit easier to use. It is a
            # part of DifferentialDrive
            self.drive.arcadeDrive(
                self.DriveStick.getY(),
                self.DriveStick.getX(),
                squareInputs=True
            )


# Runs the class MyRobot.
if __name__ == '__main__':
    wpilib.run(MyRobot)

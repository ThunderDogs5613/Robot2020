# Imports the packages so they can be used to run the robot. You can import a package from a package to avoid having
# to type in a lengthy string such as wpilib.drive.DifferentialDrive.
import wpilib
from wpilib.drive import DifferentialDrive
# ctre lets you use the can bus on the RoboRio.


class MyRobot(wpilib.TimedRobot):

    # Defines the channels on the RoboRio that the motors are plugged into. There can be up to eight.
    FLChannel = 0
    FRChannel = 1
    RLChannel = 2
    RRChannel = 3

    # Defines the order that the sticks that are plugged in are assigned.
    DriveStickChannel = 0
    # ExtraStickChannel = 1

    def robotInit(self):

        # Launches the camera server so that we can have video through any cameras on the robot.
        wpilib.CameraServer.launch()

        # Defines the motors that will actually be on the robot for use in the drive function.
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

    def operatorControl(self):

        # Enables the safety on the drive. Very important. DO NOT FORGET!
        self.drive.setSafetyEnabled(True)
        # Checks to see if the robot is activated and that operator control is active, so your robot does not move
        # when it is not supposed to.
        while self.isOperatorControl() and self.isEnabled():

            # drives the robot with the arcade drive, which uses one joystick and is a bit easier to use. It is a
            # part of DifferentialDrive
            self.drive.arcadeDrive(
                self.DriveStick.getY(),
                self.DriveStick.getX(),
                squareInputs=True
            )

        # Keeps the robot from constantly bombarding your computer for inputs, saving some CPU time for changing
        # control modes or turning off the robot


if __name__ == '__main__':
    wpilib.run(MyRobot)

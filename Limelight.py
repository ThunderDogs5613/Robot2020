# Python file to store the unfinished limelight code.
import wpilib
import networktables
import numpy

float.table = networktables.NetworkTable.getTable("limelight")
float.tx = float.table.getNumber("tx")
float.ty = float.table.getNumber("ty")


class estimateDistance(float.ty):
    mountAngle = 20
    targetAngle = 20 + float.ty
    botHeight = 2
    targetHeight = 10

    d = ((targetHeight - botHeight) / numpy.tan(targetAngle))


# Steering factor for changing the entire system in one go.
f = 1

# Controls the maximum motor output and the minimum command that can go to the motors
controlConstant = -0.1 * f
minCommand = -0.05 * f

"""
if self.DriveStick.getRawButton(2):
    
    wpilib.run(estimateDistance)
    
    float.headingError = float.tx
    float.steerAdjust = 0*f

    if float.tx > 1.0
        float.steerAdjust = kp*float.headingError + minCommand
    elif float.tx < -1.0
        self.steerAdjust = kp*float.headingError - minCommand
    
    leftDrive = float.steerAdjust
    rightDrive = -float.steerAdjust
    
    self.drive.tankDrive(
    leftDrive,
    rightDrive,
    squareInputs=False
    )
"""

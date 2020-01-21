from pyfrc.physics import drivetrains


class PhysicsEngine:

    def __init__(self, physics_controller):
        self.physics_controller = physics_controller
        self.drive = drivetrains.FourMotorDrivetrain()

    def update_sim(self, hal_data, now, tm_diff):
        lr_motor = hal_data["pwm"][2]["value"]
        rr_motor = hal_data["pwm"][4]["value"]
        lf_motor = hal_data["pwm"][1]["value"]
        rf_motor = hal_data["pwm"][3]["value"]

        speed, rotation = self.drive.get_vector(lr_motor, rr_motor, lf_motor, rf_motor)
        self.physics_controller.drive(speed, rotation, tm_diff)


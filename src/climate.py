class ClimateStatus:

    @staticmethod
    def temperature_state(value):

        if value < 18:
            return "Cold"

        if value > 28:
            return "Hot"

        return "Optimal"

    @staticmethod
    def humidity_state(value):

        if value < 45:
            return "Dry"

        if value > 70:
            return "Wet"

        return "Optimal"

    @staticmethod
    def light_state(value):

        if value < 250:
            return "Low"

        if value > 900:
            return "High"

        return "Optimal"

    @staticmethod
    def co2_state(value):

        if value < 400:
            return "Low"

        if value > 1000:
            return "High"

        return "Optimal"

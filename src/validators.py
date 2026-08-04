from config import CLIMATE_LIMITS


class ClimateValidator:

    @staticmethod
    def validate(data):

        errors = []

        for metric, limits in CLIMATE_LIMITS.items():

            value = data.get(metric)

            if value is None:
                errors.append(f"{metric} is missing")
                continue

            if value < limits["min"] - 100:
                errors.append(f"{metric} value is unrealistic")

            if value > limits["max"] + 1000:
                errors.append(f"{metric} value is unrealistic")

        return errors

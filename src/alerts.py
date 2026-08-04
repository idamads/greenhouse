from config import CLIMATE_LIMITS


class AlertManager:

    def evaluate(self, values):

        alerts = []

        for metric, limits in CLIMATE_LIMITS.items():

            value = values[metric]

            if value < limits["min"]:
                alerts.append({
                    "metric": metric,
                    "level": "low",
                    "value": value
                })

            elif value > limits["max"]:
                alerts.append({
                    "metric": metric,
                    "level": "high",
                    "value": value
                })

        return alerts

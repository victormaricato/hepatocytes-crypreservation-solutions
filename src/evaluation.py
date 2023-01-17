from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score


class Evaluation:
    def report(self, y_true, y_pred):
        mse, mae, r2 = self.evaluate(y_true, y_pred)

        print(f"Mean Squared Error: {mse}")
        print(f"Mean Absolute Error: {mae}")
        print(f"R2 Score: {r2}")

    def evaluate(self, y_true, y_pred):
        mse = mean_squared_error(y_true, y_pred)
        mae = mean_absolute_error(y_true, y_pred)
        r2 = r2_score(y_true, y_pred)
        return mse, mae, r2

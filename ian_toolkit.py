from datetime import datetime, timedelta


def date_from_days_since_2005(days):
    """
    Returns the date string corresponding to the given number of days since 2005-01-01.

    :param days: Number of days since 2005-01-01.
    :return: Date string in 'YYYY-MM-DD' format.
    """
    reference_date = datetime(2005, 1, 1)
    target_date = reference_date + timedelta(days=days - 1)
    return target_date.strftime("%Y-%m-%d")


def days_since_2005(input_date_str):
    """
    Calculates the number of days between the given date and 2005-01-01.

    :param input_date_str: A date string in 'YYYY-MM-DD' format.
    :return: The difference in days as an integer.
    """
    try:
        input_date = datetime.strptime(input_date_str, "%Y-%m-%d").date()
        reference_date = datetime(2005, 1, 1).date()
        return (input_date - reference_date).days + 1
    except ValueError:
        raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.")


# Example usage
print(days_since_2005("2025-03-09"))  # Outputs the number of days since 2005-01-01
print(date_from_days_since_2005(7359))  # Returns the date 7000 days after 2005-01-01
print(date_from_days_since_2005(7400))  # Returns the date 7000 days after 2005-01-01

# Day 16 - API Error Handling

def call_api(status_code):
    try:
        if status_code == 200:
            return "Success: API response received."

        elif status_code == 401:
            raise PermissionError("Authentication failed.")

        elif status_code == 429:
            raise RuntimeError("Rate limit exceeded.")

        elif status_code == 500:
            raise ConnectionError("Server error occurred.")

        else:
            raise ValueError("Unexpected status code.")

    except PermissionError as error:
        return f"Authentication Error: {error}"

    except RuntimeError as error:
        return f"Rate Limit Error: {error}"

    except ConnectionError as error:
        return f"Server Error: {error}"

    except ValueError as error:
        return f"Other Error: {error}"


# Test different API responses
status_codes = [200, 401, 429, 500]

for code in status_codes:
    print(f"\nStatus Code: {code}")
    print(call_api(code))
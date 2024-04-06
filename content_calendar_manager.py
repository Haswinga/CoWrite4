import json

def load_content_calendar():
  try:
    with open("content_calendar.json", "r") as f:
      return json.load(f)
  except FileNotFoundError:
    return []

def save_content_calendar(content_calendar):
  with open("content_calendar.json", "w") as f:
    json.dump(content_calendar, f)

def add_to_content_calendar(content_item):
  content_calendar = load_content_calendar()
  content_calendar.append(content_item)
  save_content_calendar(content_calendar)

def get_content_from_calendar():
  content_calendar = load_content_calendar()
  # Implement logic to get the next content item based on your scheduling logic
  # For example, you can return the first item or the item with the closest publish date
  return content_calendar[0]

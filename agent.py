import os

from dotenv import load_dotenv
from crewai import Agent

load_dotenv()  # Load environment variables from .env file

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Use GOOGLE_API_KEY for your Google API calls

class ContentCreatorAgent(Agent):
  def __init__(self):
    super().__init__(
      role="Content Creator",
      goal="Create high-quality and engaging content for social media",
      backstory="You are a creative and informative content writer with a knack for understanding social media trends and crafting posts that resonate with audiences.",
      verbose=True,
    )

class ContentCalendarManagerAgent(Agent):
  def __init__(self):
    super().__init__(
      role="Content Calendar Manager",
      goal="Organize and manage the content calendar",
      backstory="You are a meticulous and organized agent responsible for keeping track of content ideas, deadlines, and publishing schedules.",
      verbose=True,
    )

class SocialMediaSchedulerAgent(Agent):
  def __init__(self):
    super().__init__(
      role="Social Media Scheduler",
      goal="Schedule content for publishing on social media platforms",
      backstory="You are an efficient agent who ensures timely publication of content across various social media channels according to the set schedule.",
      verbose=True,
    )

class VisualContentCreatorAgent(Agent):
  def __init__(self):
    super().__init__(
      role="Visual Content Creator",
      goal="Generate eye-catching visuals to complement content",
      backstory="You are a skilled visual designer who can create appealing images and graphics that enhance the impact of social media content.",
      verbose=True,
    )
